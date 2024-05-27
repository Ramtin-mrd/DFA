import xml.etree.cElementTree as ET

try:
    data = ET.parse('xml.xml')
    root = data.getroot()
except ET.ParseError as e:
    print(f"Error parsing XML: {e}")
    exit(1)
except FileNotFoundError:
    print("Error: file was not found.")
    exit(1)

def xmlReader(root):
    initialState = root.find('.//initialState').get('name')
    finalState = {state.get('name') for state in root.findall('.//finalState')}
    transition = {(trans.get('source'), trans.get('label')): trans.get('destination') for trans in root.findall('.//transition')}
    return initialState, finalState, transition

initialState, finalState, transition = xmlReader(root)

def checkString(finalState, initialState, transition, string):
    selectedState = initialState
    for char in string:
        if (selectedState, char) in transition:
            selectedState = transition[(selectedState, char)]
        else:
            return False
    return selectedState in finalState

print("Enter a string like aab, aba, bbbb, ...: \n" + "Enter end to break")

while(True) :
    String = input( "String = ")
    if (String == "end") : break
    if checkString(finalState, initialState, transition, String):
        print("Accept")
    else:
        print("Reject")

