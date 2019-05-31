
ID = input("Enter your 11 digit account number:")  # 04230647978

encry = "*" * 5
start_ID = ID[0:4]
end_ID = ID[9:]
final_ID = start_ID + encry + end_ID
print(final_ID)
