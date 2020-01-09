# codes = ["ASIA", "ASIA", "ATA", "AUTO", "BM", "BIS", "CHE", "CHEM", "STS", "CE", "ENGG", "COGS", "CSE", "CET", "CMPE", "ENG", "INT", "CEM", "CCS", "EQE", "EC", "EF", "ED", "CET", "EE", "ETM", "ESC", "ESC", "ADEX", "FE", "PA", "FLED", "GED", "GPH", "ED", "CHIN", "GR", "HIST", "JP", "LAT", "HUM", "IE", "INCT", "MIR", "MIR", "INTT", "INTT", "LS", "CAU", "LING", "TID", "AD", "MIS", "MATH", "SCED", "ME", "MECA", "BIO", "PHIL", "PE", "PHYS", "STS", "POLS", "PRED", "PSY", "AE", "ARM", "FR", "GER", "GR", "ITA", "KR", "POR", "RUS", "SFL", "SPA", "SCED", "SPL", "SOC", "SWE", "SWE", "TRM", "SCO", "TRM", "TR", "INT", "TR", "TK", "PER", "TKF", "TKL", "AL", "AS", "CL", "EL", "ENGL", "FA", "LIT"]

import requests
import urllib.request
import time
import sys
from bs4 import BeautifulSoup

departments = ["MANAGEMENT", "ASIAN+STUDIES", "ASIAN+STUDIES+WITH+THESIS", "ATATURK+INSTITUTE+FOR+MODERN+TURKISH+HISTORY", "AUTOMOTIVE+ENGINEERING", "MOLECULAR+BIOLOGY+%26+GENETICS", "BUSINESS+INFORMATION+SYSTEMS", "BIOMEDICAL+ENGINEERING", "CRITICAL+AND+CULTURAL+STUDIES", "CIVIL+ENGINEERING", "CONSTRUCTION+ENGINEERING+AND+MANAGEMENT", "COMPUTER+EDUCATION+%26+EDUCATIONAL+TECHNOLOGY", "EDUCATIONAL+TECHNOLOGY", "CHEMICAL+ENGINEERING", "CHEMISTRY", "COMPUTER+ENGINEERING", "COGNITIVE+SCIENCE", "COMPUTATIONAL+SCIENCE+%26+ENGINEERING", "ECONOMICS", "EDUCATIONAL+SCIENCES", "ELECTRICAL+%26+ELECTRONICS+ENGINEERING", "ECONOMICS+AND+FINANCE", "ENVIRONMENTAL+SCIENCES", "ENVIRONMENTAL+TECHNOLOGY", "EARTHQUAKE+ENGINEERING", "ENGINEERING+AND+TECHNOLOGY+MANAGEMENT", "FINANCIAL+ENGINEERING", "FOREIGN+LANGUAGE+EDUCATION", "GEODESY", "GEOPHYSICS", "GUIDANCE+&+PSYCHOLOGİCAL+COUNSELING", "HISTORY", "HUMANITIES+COURSES+COORDINATOR", "INDUSTRIAL+ENGINEERING", "INTERNATIONAL+COMPETITION+AND+TRADE", "CONFERENCE+INTERPRETING", "INTERNATIONAL+TRADE", "INTERNATIONAL+TRADE+MANAGEMENT", "LINGUISTICS", "WESTERN+LANGUAGES+%26+LITERATURES", "LEARNING+SCIENCE", "MATHEMATICS", "MECHANICAL+ENGINEERING", "MECHATRONICS+ENGINEERING", "INTERNATIONAL+RELATIONS%3aTURKEY%2cEUROPE+AND+THE+MIDDLE+EAST", "INTERNATIONAL+RELATIONS%3aTURKEY%2cEUROPE+AND+THE+MIDDLE+EAST+WITH+THESIS", "MANAGEMENT+INFORMATION+SYSTEMS", "FINE+ARTS", "PHYSICAL+EDUCATION", "PHILOSOPHY", "PHYSICS", "POLITICAL+SCIENCE%26INTERNATIONAL+RELATIONS", "PRIMARY+EDUCATION", "PSYCHOLOGY", "MATHEMATICS+AND+SCIENCE+EDUCATION", "SECONDARY+SCHOOL+SCIENCE+AND+MATHEMATICS+EDUCATION", "SYSTEMS+%26+CONTROL+ENGINEERING", "SOCIOLOGY", "SOCIAL+POLICY+WITH+THESIS", "SOFTWARE+ENGINEERING", "SOFTWARE+ENGINEERING+WITH+THESIS", "TURKISH+COURSES+COORDINATOR", "TURKISH+LANGUAGE+%26+LITERATURE", "TRANSLATION+AND+INTERPRETING+STUDIES", "SUSTAINABLE+TOURISM+MANAGEMENT", "TOURISM+ADMINISTRATION", "TRANSLATION", "EXECUTIVE+MBA", "SCHOOL+OF+FOREIGN+LANGUAGES"]
codes = ["AD", "ASIA", "ASIA", "ATA", "AUTO", "BIO", "BIS", "BM", "CCS", "CE", "CEM", "CET", "CET", "CHE", "CHEM", "CMPE", "COGS", "CSE", "EC", "ED", "EE", "EF", "ENV", "ENVT", "EQE", "ETM", "FE", "FLED", "GED", "GPH", "GUID", "HIST", "HUM", "IE", "INCT", "INT", "INTT", "INTT","LING", "LL", "LS", "MATH", "ME", "MECA", "MIR", "MIR", "MIS", "PA", "PE", "PHIL", "PHYS", "POLS", "PRED", "PSY", "SCED", "SCED", "SCO", "SOC", "SPL", "SWE", "SWE", "TK", "TKL", "TR", "TRM", "TRM", "WTR", "XMBA", "YADYOK"]
start = sys.argv[1]
end = sys.argv[2]
start_year = int(start[0:4])
start_semester = start[5:]
end_year = int(end[0:4])
end_semester = end[5:]
urls = []
base_urls = []
number_of_semesters = 0


if start == end:
	pass
elif start_semester == "Fall":
	if end_semester == "Fall":
		number_of_semesters = (end_year - start_year) * 3 + 1
		for i in range(len(departments)):
			for year in range(start_year, end_year):
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-1&kisaadi=" + codes[i] + "&bolum=" +departments[i])
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-2&kisaadi=" + codes[i] + "&bolum=" +departments[i])
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-3&kisaadi=" + codes[i] + "&bolum=" +departments[i])
			urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(end_year) + "/" + str(end_year + 1) + "-1&kisaadi=" + codes[i] + "&bolum=" +departments[i])
	elif end_semester == "Spring":
		number_of_semesters = (end_year - start_year) * 3 - 1
		for i in range(len(departments)):
			for year in range(start_year, (end_year - 1)):
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-1&kisaadi=" + codes[i] + "&bolum=" +departments[i])
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-2&kisaadi=" + codes[i] + "&bolum=" +departments[i])
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-3&kisaadi=" + codes[i] + "&bolum=" +departments[i])
			urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(end_year - 1) + "/" + str(end_year) + "-1&kisaadi=" + codes[i] + "&bolum=" +departments[i])
			urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(end_year - 1) + "/" + str(end_year) + "-2&kisaadi=" + codes[i] + "&bolum=" +departments[i])
	else:
		number_of_semesters = (end_year - start_year) * 3
		for i in range(len(departments)):
			for year in range(start_year, end_year):
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-1&kisaadi=" + codes[i] + "&bolum=" +departments[i])
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-2&kisaadi=" + codes[i] + "&bolum=" +departments[i])
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-3&kisaadi=" + codes[i] + "&bolum=" +departments[i])
elif start_semester == "Spring":
	if end_semester == "Fall":
		number_of_semesters = (end_year - start_year) * 3 + 3
		for i in range(len(departments)):
			urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(start_year - 1) + "/" + str(start_year) + "-2&kisaadi=" + codes[i] + "&bolum=" +departments[i])
			urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(start_year - 1) + "/" + str(start_year) + "-3&kisaadi=" + codes[i] + "&bolum=" +departments[i])
			for year in range((start_year + 1), end_year):
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-1&kisaadi=" + codes[i] + "&bolum=" +departments[i])
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-2&kisaadi=" + codes[i] + "&bolum=" +departments[i])
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-3&kisaadi=" + codes[i] + "&bolum=" +departments[i])
			urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(end_year) + "/" + str(end_year + 1) + "-1&kisaadi=" + codes[i] + "&bolum=" +departments[i])
	elif end_semester == "Spring":
		number_of_semesters = (end_year - start_year) * 3 + 1
		for i in range(len(departments)):
			urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(start_year - 1) + "/" + str(start_year) + "-2&kisaadi=" + codes[i] + "&bolum=" +departments[i])
			urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(start_year - 1) + "/" + str(start_year) + "-3&kisaadi=" + codes[i] + "&bolum=" +departments[i])
			for year in range(start_year, (end_year - 1)):
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-1&kisaadi=" + codes[i] + "&bolum=" +departments[i])
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-2&kisaadi=" + codes[i] + "&bolum=" +departments[i])
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-3&kisaadi=" + codes[i] + "&bolum=" +departments[i])
			urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(end_year - 1) + "/" + str(end_year) + "-1&kisaadi=" + codes[i] + "&bolum=" +departments[i])
			urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(end_year - 1) + "/" + str(end_year) + "-2&kisaadi=" + codes[i] + "&bolum=" +departments[i])
	else:
		number_of_semesters = (end_year - start_year) * 3 + 2
		for i in range(len(departments)):
			urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(start_year - 1) + "/" + str(start_year) + "-2&kisaadi=" + codes[i] + "&bolum=" +departments[i])
			urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(start_year - 1) + "/" + str(start_year) + "-3&kisaadi=" + codes[i] + "&bolum=" +departments[i])
			for year in range(start_year, end_year):
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-1&kisaadi=" + codes[i] + "&bolum=" +departments[i])
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-2&kisaadi=" + codes[i] + "&bolum=" +departments[i])
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-3&kisaadi=" + codes[i] + "&bolum=" +departments[i])
else:
	if end_semester == "Fall":
		number_of_semesters = (end_year - start_year) * 3 + 2
		for i in range(len(departments)):
			urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(start_year - 1) + "/" + str(start_year) + "-3&kisaadi=" + codes[i] + "&bolum=" +departments[i])
			for year in range((start_year + 1), end_year):
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-1&kisaadi=" + codes[i] + "&bolum=" +departments[i])
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-2&kisaadi=" + codes[i] + "&bolum=" +departments[i])
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-3&kisaadi=" + codes[i] + "&bolum=" +departments[i])
			urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(end_year) + "/" + str(end_year + 1) + "-1&kisaadi=" + codes[i] + "&bolum=" +departments[i])
	elif end_semester == "Spring":
		number_of_semesters = (end_year - start_year) * 3 
		for i in range(len(departments)):
			urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(start_year - 1) + "/" + str(start_year) + "-3&kisaadi=" + codes[i] + "&bolum=" +departments[i])
			for year in range(start_year, (end_year - 1)):
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-1&kisaadi=" + codes[i] + "&bolum=" +departments[i])
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-2&kisaadi=" + codes[i] + "&bolum=" +departments[i])
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-3&kisaadi=" + codes[i] + "&bolum=" +departments[i])
			urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(end_year - 1) + "/" + str(end_year) + "-1&kisaadi=" + codes[i] + "&bolum=" +departments[i])
			urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(end_year - 1) + "/" + str(end_year) + "-2&kisaadi=" + codes[i] + "&bolum=" +departments[i])
	else:
		number_of_semesters = (end_year - start_year) * 3 + 1
		for i in range(len(departments)):
			urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(start_year - 1) + "/" + str(start_year) + "-3&kisaadi=" + codes[i] + "&bolum=" +departments[i])
			for year in range(start_year, end_year):
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-1&kisaadi=" + codes[i] + "&bolum=" +departments[i])
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-2&kisaadi=" + codes[i] + "&bolum=" +departments[i])
				urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=" + str(year) + "/" + str(year + 1) + "-3&kisaadi=" + codes[i] + "&bolum=" +departments[i])

for i in range(len(departments)):
	base_urls.append("https://registration.boun.edu.tr/scripts/sch.asp?donem=2018/2019-2&kisaadi=" + codes[i] + "&bolum=" +departments[i])
counter_for_url = 0
number_of_instructors = []
instructors_of_course = []
for y in range(len(codes)):
	r = requests.get(base_urls[y])
	soup = BeautifulSoup(r.content, "html.parser")
	lines = soup.find_all("tr", attrs = {"class":["schtd2", "schtd"]})
	base_course_codes = []
	base_course_names = []
	base_instructors = []


	# cds = soup.find_all("font", attrs = {"style":"font-size:12px"})
	base_count_u = 0
	base_count_g = 0
	for line in lines:
		tds = line.find_all("td")
		if str(tds[0]) != "<td>  </td>":
			code = str(tds[0].text)[:-4]
			if code not in base_course_codes:
				base_course_codes.append(code)
				if code[-3] == "1" or code[-3] == "2" or code[-3] == "3" or code[-3] == "4":
					base_count_u = base_count_u + 1
				else:
					base_count_g = base_count_g + 1
				base_course_names.append(str(tds[2].text)[:-1])
			#print(str(tds[0].text)[:-4])
			if str(tds[5]) != "<td>STAFF STAFF </td>":
				base_instructors.append(str(tds[5].text))
	#base_course_names = list(dict.fromkeys(base_course_names))
	base_instructors = list(dict.fromkeys(base_instructors))
	#print(len(base_instructors))
	"""
	for name in base_course_names:
		print(name)
	"""	
	#print(len(base_course_names))

	"""	
	for code in base_course_codes:
		print(code)"""

#print(len(base_course_codes))
	out = []
	for i in range(len(base_course_codes)):
		s = "\t" + base_course_codes[i] + ", " + base_course_names[i] + ", "
		out.append(s)
	
	"""
	for i in range(len(urls)):	
	print(urls[i])"""
	total_u = 0
	total_g = 0
	total_instructors = []

	first_line = codes[y] + "(" + departments[y] + "), U" + str(base_count_u) + " G" + str(base_count_g) + ", , "
	for i in range(number_of_semesters):
		r = requests.get(urls[counter_for_url])
		counter_for_url = counter_for_url + 1
		soup = BeautifulSoup(r.content, "html.parser")
		lines = soup.find_all("tr", attrs = {"class":["schtd2", "schtd"]})
		course_codes = []
		course_names = []
		instructors = []
		number_of_instructors.clear()
		instructors_of_course.clear()

		# cds = soup.find_all("font", attrs = {"style":"font-size:12px"})
		for line in lines:
			tds = line.find_all("td")
			if str(tds[0]) != "<td>  </td>":
				code = str(tds[0].text)[:-4]
				if code not in course_codes:
					course_codes.append(code)
					course_names.append(str(tds[2].text)[:-1])
					if len(course_codes) != 1:
						number_of_instructors.append(len(instructors_of_course))
					instructors_of_course = []
					if str(tds[5]) != "<td>STAFF STAFF </td>":
						instructors_of_course.append(str(tds[5].text))
				else: 
					current_instructor = str(tds[5].text)
					if current_instructor not in instructors_of_course:
						instructors_of_course.append(str(tds[5].text))
				#print(str(tds[0].text)[:-4])
				if str(tds[5]) != "<td>STAFF STAFF </td>":
					instructors.append(str(tds[5].text))
					total_instructors.append(str(tds[5].text))
		number_of_instructors.append(len(instructors_of_course))
		#course_names = list(dict.fromkeys(course_names))
		instructors = list(dict.fromkeys(instructors))
		count = 0
		count_u = 0
		count_g = 0
		

		for i in range(len(base_course_codes)):
			current_code = base_course_codes[i]
			if current_code in course_codes:
				out[i] = out[i] + "x, "
				#print(current_code + str(len(current_code)))
				if current_code[-3] == "1" or current_code[-3] == "2" or current_code[-3] == "3" or current_code[-3] == "4":
						count_u = count_u + 1
				else:
						count_g = count_g + 1
				count = count + 1
			else:
				out[i] = out[i] + " , "
		
		total_u = total_u + count_u
		total_g = total_g + count_g
		first_line = first_line + "U" + str(count_u) + " G" + str(count_g) + " I" + str(len(instructors)) + ", "
	for i in range(len(out)):
		number = out[i].count(" x,")
		out[i] = out[i] + str(number) + "\\" 
	total_instructors = list(dict.fromkeys(total_instructors))
	first_line = first_line + "U" + str(total_u) + " G" + str(total_g) + " I" + str(len(total_instructors))
	print(first_line)
	for i in range(len(out)):
		print(out[i])
	
"""for code in course_codes:
	print(code)"""
"""
for i in range(len(urls)):	
	print(urls[i])"""
#print(len(course_codes))
#

	

"""	
print(count)
print(base_count_u)
print(base_count_g)
print(count_u)
print(count_g)"""
"""for i in range(len(number_of_instructors)):
	print(number_of_instructors[i])"""