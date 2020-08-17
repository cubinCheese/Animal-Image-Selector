README
========
System:
	Python 3.8.2
	Windows 10
	
================
Description:
================

	A webscrapping program that downloads and shows an image of a cute animal, based on user selection. Meant to relieve stress, and bring the user joy.

================
Requirements:
================

	Chromedriver needs to be installed. 
	Chromedriver location must be located as follows: "C:\Program Files (x86)\chromedriver.exe"
	User may also change the target of chromedriver path within the script itself, simply re-assign "ChromeDriver_Path" with your selected absolute path. 

	Chromedriver Installation:
		https://chromedriver.chromium.org/
		Follow download instructions on page.
================
How to Use:
================

	Call the script "Image_Random.py" as the program is named into the command line.

		Example : >>> [py Image_Random.py] 

	You will then see instructions in the command line.

================
Additional Notes:
================

	There are some personal notes/ideas written in the code itself, you may ignore them as they don't affect usage.
	
	Potential (later) additions:
		* add more options for animals apply
		* runs a bit slow, look into optimization
		* implement error handling (currently lacking)
		* remove unwanted messages in command line
		* perhaps create a search function so that chromedriver doesn't have to be downloaded to some specific folder
		* implement a GUI for the user, instead of command-line entry.
		* write some installation instructions for chromedriver