import sys
import os
import io
import subprocess
import shutil
from xml.dom import minidom
#########################################################################
##Function	: main()
##Purpose	: it all begins here
#########################################################################
def main():
	manifestClean = minidom.parse("AndroidManifest.xml")
	manifestMalware = minidom.parse("AndroidManifest-Malware.xml")
	cleanPermissions = manifestClean.getElementsByTagName('uses-permission')
	malwarePermissions = manifestMalware.getElementsByTagName('uses-permission')
	listOfExtraPermissions = [];
	bool = False
	for listItem in malwarePermissions:
		for listItem2 in cleanPermissions:
			if listItem2.attributes['android:name'].value == listItem.attributes['android:name'].value:
				bool = True
		if bool == False:
			listOfExtraPermissions.append(listItem.attributes['android:name'].value.replace("android.permission.",""))
		else:
			bool = False
	print("The suspicious application has the following extra permissions")
	for a in listOfExtraPermissions:
		print(a)
#Set the global variables here
if __name__ == '__main__':
	main()
