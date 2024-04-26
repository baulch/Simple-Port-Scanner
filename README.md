# Simple-Port-Scanner
Created for proof of concept. To better understand how port scanner scripts are created and used.

The port range for the scan is 50-85, anything more would be inefficient or too long.
There are some changes that can be made including:
valid ip range i.e. each octet needs to be in the range of 1-254, this can be done using regular expression, and splitting the ip up using '.' as a separator. Overall, it is possible to refine this program into a more professional port scanner, but it is perfect for learning the socket module.
