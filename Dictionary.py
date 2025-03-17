#  dict ={} empty dictionary
Bio = {
  "name" : "Dev",
  "Age" : 20,
  "Gender" : "Male",
  "Bio" : "I am a developer"
}

# print(Bio);
# print(Bio["name"]);

# methods

# print(Bio.items())
# print(Bio.keys())
# print(Bio.values())

Bio.update({"name":"Divyanshu", "designation":"Software Developer"})
print(Bio)

# print(Bio.get("name2")) return None if key is not found
# print(Bio["name2"])  return error if key is not present