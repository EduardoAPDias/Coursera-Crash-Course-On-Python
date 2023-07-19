# Skill Group 1
# Use a for loop to modify elements of a list.
# Use the list.append(old,new) method.
# Use the string.endswith() and string.replace() methods to modify the elements within a list.

years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

updated_years = []

for year in years:
    if year.endswith("2023"):
        new = year.replace("2023","2024")
        updated_years.append(new)
    else:
        updated_years.append(year)
        
print(updated_years)


# Skill Group 2
# Use a list comprehension to return values

def squares(start, end):
    return [n*n for n in range(start,end+1)]

print(squares(2, 3))  
print(squares(1, 5))  
print(squares(0, 10))

# Skill Group 3
# Use the string[index] method within a list comprehension.  
# Use a list comprehension to modify elements of a list.
# Use the string.replace() method within a list comprehension.

years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

updated_years = [year.replace("2023","2024") if year[-4:] == "2023" else year for year in years]

print(updated_years)

# Skill Group 4
# Use the string.split() method to separate a string into a list of individual words.
# Iterate over the new list using a for loop.
# Modify each element in the list by slicing the element’s string at a given [1:] index position and appending the 
# substring to the end of the element.
# Convert a list back into a string.

def change_string(given_string):
    
    new_string = ""
    new_list = given_string.split()
    
    for element in new_list:
        new_string += element[1:] + "-" + element[0] + " "
        
    return new_string
    
print(change_string("1one 2two 3three 4four 5five"))

# Skill Group 5  
#  Use the string.join() method to concatenate a string that provides a list name and its elements

def list_elements(list_name, elements):
    
    return "The " + list_name + " list includes:" + ", ".join(elements)

print(list_elements("Printers", ["Color Printer", "Black and White Printer", "3-D Printer"])) 