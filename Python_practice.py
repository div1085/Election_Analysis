print("hello world")
#create list
counties = ["Arapahoe","Denver","Jefferson"]
#splice cut list
counties[0:2]
#add to list and remove from list
counties.append("El Paso")
counties.insert(2,"El Paso")
counties.pop(4)
#count elements in list
len(counties)
#adding list of dict
voting_data=[]
voting_data.append({"county":"Arapahoe","Registered_Voters":422829})
voting_data.append({"county":"Denver","Registered_Voters":463353})
voting_data.append({"county":"Jefferson","Registered_Voters":432438})
print(voting_data)
# remove "Arapahoe"
voting_data.pop(0)
print(voting_data)
#adding "Arapahoe"
voting_data.append({"county":"Arapahoe","Registered_Voters":422839})
#Make “Denver” and its registered voters the third item in voting_data, but keep “Jefferson” 
# and its registered voters as the second item.
counties_order=[0,2,1,3]
counties=[counties[i] for i in counties_order]
print(counties)
counties.pop(0)
print(counties)
counties_order=[0,2,1]
counties=[counties[i] for i in counties_order]
print(counties)
counties.append("Arapahoe")
print(counties)
#adding tuple
counties_tuple=("Arapahoe","Denver","Jefferson")
print(counties_tuple)
counties_tuple[1]
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
voting_data[1]=({'county':'El Paso','Registered_Voters':461149})
print(voting_data)
print(counties)
for county in counties:
    print(county)
for i in range(len(counties)):
    print(counties[i])
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county, voters in counties_dict.items():
    print(county, voters)
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)