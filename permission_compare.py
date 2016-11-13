import xml.etree.ElementTree as ET

tree1 = ET.parse('TorchAndroidManifest.xml')
root1 = tree1.getroot()

print

print "The first application requests the following permission:"

array1 = []

for child in root1.iter('uses-permission'):
		# print child.tag, child.attrib
		array1.append(child.get('{http://schemas.android.com/apk/res/android}name'))
		print child.get('{http://schemas.android.com/apk/res/android}name')

tree2 = ET.parse('TorchMalwareAndroidManifest.xml')
root2 = tree2.getroot()

print 

print "The second application requests the following permission:"

array2 = []

for child in root2.iter('uses-permission'):
		# print child.tag, child.attrib
		array2.append(child.get('{http://schemas.android.com/apk/res/android}name'))
		print child.get('{http://schemas.android.com/apk/res/android}name')

print

for permission in array2:
	if permission not in array1:
		print "The permission ", permission, " is not requested by the first application"