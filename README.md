# Satellite_Tracker
While camping in the Tucson, AZ area, several satellites could be spotted overhead. I wanted to be able to track the names and times of these satellites for future reference.

### Overview
Using the Python library, Skyfield, as well as Celestrack's satellites API, I created a webpage that lists several common satellites that will fly overhead the following night. 
Currently, the location is only set for Tucson, AZ, but the coordinates can easily be changed and I may implement a dynamic settings option in the future.
I've used Flask as a quick way to set up the webpage as well as Bootstrap for some simple stylings.
The list, which is set from earliest to latest showings, inludes the satellite's name and the time of rising, culmination, and setting for each. The data also shows whether the satellite will be in the Earth's shadow or not, making it more difficult to be seen.