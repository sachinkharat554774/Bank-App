#run this file using command given below on terminal
#python bankapp.py

from sqlite3 import *

w = input("Welcome to bank app.\nDo you want to create or update details y/n -> ")

while w == "Y" or w == "y":

	command = input()
	command = command.upper()
	r = command.split(" ")
	print(r)

	if r[0] == "CREATE":
		con = None
		try:
			con = connect("bank.db")
			cursor = con.cursor()
			sql = "insert into account values('%s','%s','%d')"
			id = r[1]
			name = r[2]
			balance = 0
			cursor.execute(sql % (id,name,balance))
			con.commit()
			print("record created ")
		except Exception as e:
			con.rollback()
			print("issue ",e)
		finally:
			if con is not None:
				con.close()

	elif r[0] == "DEPOSIT":
		con = None
		try:
			con = connect("bank.db")
			cursor = con.cursor()
			sql = "update account set balance = balance + '%d' where id = '%s'"
			id = r[1]
			balance = int(r[2])
			cursor.execute(sql % (balance,id))
			con.commit()
			print("record created ")
		except Exception as e:
			con.rollback()
			print("issue ",e)
		finally:
			if con is not None:
				con.close()

	elif r[0] == "WITHDRAW":
		con = None
		try:
			con = connect("bank.db")
			cursor = con.cursor()
			sql = "update account set balance = balance - '%d' where id = '%s'"
			id = r[1]
			balance = int(r[2])
			cursor.execute(sql % (balance,id))
			con.commit()
			print("record created ")
		except Exception as e:
			con.rollback()
			print("issue ",e)
		finally:
			if con is not None:
				con.close()

	elif r[0] == "SHOW":
		con = None
		try:
			con = connect("bank.db")
			cursor = con.cursor()
			sql = "select id, balance from account"
			cursor.execute(sql)
			res = cursor.fetchall()
			for i in res:
				for j in i:
					print(j)
				print()
		except Exception as e:
			print("issue ",e)
		finally:
			if con is not None:
				con.close()

	else:
		print("invalid input")

	w = input("\n\nDo you want to continue ?  ->  ")
