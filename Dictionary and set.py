#Dictionary(MUTABLE (can add))
#key:value
info = {
    "Key" : "value",
    "name" : "Sinchana",
    "learning" : "Coding"}
print(info)    
null_dict = {}
print(null_dict)


#Nested dictionary 
student = {
    "name" : "awhan",
    "subjects" : {
        "phy" : 63,
        "chem" : 69,
        "math" : 78
    }
}
print(student["subjects"]["chem"])


#Dictinary methods
student.keys()
student.len()
student.update({"city"})

#Sets in python
null_set = set()
set.union(set2)
set.intersection(set2)


