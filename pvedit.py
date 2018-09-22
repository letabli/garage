
# 유로파 프로빈스 파일 불러오기
import os
path_dir = 'E:\SteamLibrary\steamapps\common\Europa Universalis IV\history\provinces'
file_list = os.listdir(path_dir)

# 프로빈스 파일 리스트에서 이름 리스트 만들기
province_list = []
for file in file_list:
	province = ""
	file = file[:-4]
	for cha in file:
		if cha.isalpha() == True:
			province += cha
	province_list.append(province)
	setattr(

	write_path = "D:\Documents\provinces.py"
	
	province_file = open(write_path, 'w')
	for i in province_list:
		province_file.write(i + "\n")
		province_file.close()
	
	



print(province_list)


with open(write_path, 'r') as f:
	for j in f:
		print(j)

