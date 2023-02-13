# introduction

This is a personal repo for any python scripts I have created to help with FHIR UKCore. Feel free to use any scripts at your own risk.

## Create_Codesystems 
This file is intended to create a CodeSystems expansion set for codes that reside on a website.

# Actions
Add a website to website.txt to run the following actions

## errorChecker
Checks for any html errors on a website. Will find all links on the target page and interate through them.

## linkChecker
Checks all links to ensue that tey work correctly
-r 2 *recursion level 2*
--check-extern *check external links are valid*
--no-status *do not show status apart from errors*
-f linkcheckerrc *use config file - setup so that it will check any pages <50mb in size* 

## spellChecker
https://www.gnu.org/software/wget/manual/wget.html#Option-Syntax
-nv *Turn off verbose without being completely quiet (use ‘-q’ for that), which means that error messages and basic information still get printed.* 
-O *The documents will not be written to the appropriate files, but all will be concatenated together and written to file. If ‘-’ is used as file, documents will be printed to standard output, disabling link conversion.*

TODO get personal dictinary working ###
