Home Assistant "MTA Service Status" python script

Overview

A python script to provide MTA Subway service statuses for Home Assistant. 

<img src="images/service.png">

The script from the offical MTA Service Status .txt feed and create 5 json files.

<img src="images/all_json_files.png">



Installation

Create "data" directory/folder in your Home Assistant configuration directory.

Copy all files from data folder to /config/data/

Full path: /config/data/

To install, copy the service_status.py to a directory called python_scripts in your Home Assistant configuration directory.

Full path: /config/python_scripts/

To install the MTA icons, copy the www/icons/mta directory and all files to your Home Assistant configuration directory.

Full path: /config/www/icons/mta/

Use "customize.yaml" in include directory to add "entity_picture" and "friendly_name".

Full path: /config/include/
