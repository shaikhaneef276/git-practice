students = [
    {"name": "Alice", "math": 85, "science": 90, "english": 88,"telugu":90},
    {"name": "Bob", "math": 78, "science": 74, "english": 80,"telugu":86},
    {"name": "Charlie", "math": 92, "science": 88, "english": 95,"telugu":90}
]
new_dict={}
for d in students:
    t=1
    c=0
    op={}
    for j in d.values():
        if type(j)== int:
            t+=1
            c+=j
        else:
            op[j]=0
        new_dict.update({j:round(c/(t-1),2) for j,k in op.items()})
print(new_dict)
li=[j for j in new_dict.values()]
s=max(li)
for i,j in new_dict.items():
    if j==s:
        print(f"Top Student: {i} with {j} average marks.")
