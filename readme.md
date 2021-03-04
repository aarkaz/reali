#To Run
To run make sure you have python 3.x installed.
You can get it from homebrew:

`brew install python3`\
\
install dependencies:\
\
`pip3 install requests`\
`pip3 install flask`

To run execute this line from the same directory level as main.py:
`python3 main.py`

The api will be accessible from `127.0.0.1:5000/listings`

#Improvements

Given more time I would have implemented a true data store such as sql or mongo and used the built in query functionalities.  
My current implementation is storing data in an in memory map using ids as keys for lookup. Pagination would be the next feature I would build.  
The API result sets that are getting generated are quite big and pagination would greatly help manage this data
