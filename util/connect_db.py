#coding:utf-8
import MySQLdb.cursors
import json
class OperationMysql:
	def __init__(self):
		self.conn = MySQLdb.connect(
			host='192.168.0.234',
			port=3306,
			user='root',
			passwd='Szcoolead@2017',
			db='coolead20180118',
			charset='utf8',
			cursorclass=MySQLdb.cursors.DictCursor
			)
		self.cur = self.conn.cursor()

	#查询一条数据
	def search_one(self,sql):
		self.cur.execute(sql)
		result = self.cur.fetchone()
		result = json.dumps(result)
		return result

if __name__ == '__main__':
	op_mysql = OperationMysql()
	res = op_mysql.search_one("select id  from tb_work_plan where project_code = '440305P000005' and short_name='F'")
	print res
