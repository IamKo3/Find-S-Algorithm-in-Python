# Find-S-Algorithm-in-Python
Program reads the data set from **data.txt**

* Data instances are stored in the form of list of lists.
* Data from data.txt is read as string.
* For example, if the data instance is: **['Sunny','Warm','Normal','Strong','Warm','Same','Yes']**.
 Now, if we try to fetch elment at the 0th index, we expect to get 'Sunny' but we get '[' instead.
Therefore, to read list as list itself from a file, we make use of <B>literal_eval</B> package in Python.

**Python Version**: 3.6
