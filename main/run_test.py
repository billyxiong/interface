#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import json
sys.path.append("F:/v2iuyg")
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependdentData
from util.send_email import SendEmail
from util.operation_header import OperationHeader
from util.operation_json import OperetionJson
from util.insert_bug import Add_bug
class RunTest:
	def __init__(self):
		self.run_method = RunMethod()
		self.data = GetData()
		self.com_util = CommonUtil()
		self.send_mai = SendEmail()


	#程序执行的
	def go_on_run(self):
		res = None
		pass_count = []
		fail_count = []
		userName="coolead"
		#10  0,1,2,3
		rows_count = self.data.get_case_lines()
		header = {"Content-Type":"application/json;charset=UTF-8"}
		for i in range(1,rows_count):
			is_run = self.data.get_is_run(i)
			if is_run:
				url = self.data.get_request_url(i)
				method = self.data.get_request_method(i)
				request_data =None
				if (method =="Post"):
					request_data = self.data.get_data_for_json(i)
#				expect = self.data.get_expcet_data_for_mysql(i)
				expect = self.data.get_expcet_data(i)
#				header = self.data.is_header(i)
				depend_case = self.data.is_depend(i)
				if depend_case != None:
					self.depend_data = DependdentData(depend_case)
					#获取的依赖响应数据
					depend_response_data = self.depend_data.get_data_for_key(i,header)
					#获取依赖的key
					depend_key = self.data.get_depend_field(i)
					request_data[depend_key] = depend_response_data
				# if header == 'write':
				# 	res = self.run_method.run_main(method,url,request_data)
				# 	op_header = OperationHeader(res)
				# 	op_header.write_cookie()
                #
				# elif header == 'yes':
				# 	op_json = OperetionJson('../dataconfig/cookie.json')
				# 	cookie = op_json.get_data('apsid')

				# 	cookies = {
				# 		'apsid':cookie
				# 	}
				# 	res = self.run_method.run_main(method,url,request_data,cookies)
				# else:
				res = self.run_method.run_main(method,url,request_data,header)
				if(i==1):
					header["X-Coolead-Token"]=json.loads(res)["result"]["refreshToken"]
					userName=request_data["userName"];
#				print   json.loads(res)
#	 			self.data.write_result(i,json.loads(res)["statusCode"])
	 			if self.com_util.is_equal_dict(expect, json.loads(res)["statusCode"]) == 0:
	 				self.data.write_result(i,'pass')
	 				pass_count.append(i)
	 			else:
	 				self.data.write_result(i, res)
	 				fail_count.append(i)
					bug_des ='<br/><span style="color:red">请求地址：</span>'+ str(self.data.get_request_url(i)) +\
							 '<br/><span style="color:red">请求数据：</span>' +str(self.data.get_data_for_json(i)) + \
							 '<br/><span style="color:red">返回结果：</span>'+ str(res)+\
							 '<br/><span style="color:red">测试帐户：</span>'+str(userName)
					code=str(self.data.get_request_url(i))+str(self.data.get_data_for_json(i))+str(userName)
					bug_des=bug_des.replace("'","\\'")
					sql = '''
        insert into zt_bug(  `product`  ,
      `module` ,
      `project`,
      `plan`,
      `story` ,
      `storyVersion`,
      `task`,
      `toTask` ,
      `toStory`,
      `title` ,
      `keywords`,
      `severity`,
      `pri`,
      `type`,
      `os`,
      `browser`,
      `hardware`,
      `found`,
      `steps`,
      `status`,
      `confirmed` ,
      `activatedCount`,
      `mailto`,
      `openedBy`,
      `openedDate`,
      `openedBuild`,
      `assignedTo`,
      `assignedDate`,
      `resolvedBy`,
      `resolution`,
      `resolvedBuild`,
      `resolvedDate`,
      `closedBy`,
      `closedDate`,
      `duplicateBug`,
      `linkBug`,
      `case`,
      `caseVersion`,
      `result`,
      `testtask`,
      `lastEditedBy`,
      `lastEditedDate`,
      `deleted`)
    values('1', '0', '23', '0', '0', '1', '0', '0', '0',\
     '接口问题',\
      '', '3', '3', 'codeerror', 'win7', 'chrome', '', '', \

    '%s' , \

    'active', '1', '0', '', '', '', 'trunk', 'open', '', 'hezm', 'active', 'trunk', '', '', '', '0', '', '0', '0', '0', '0', '', '', '0')
        '''%bug_des
#					print sql
					add_bug = Add_bug()
					query_sql = "select count(*) from zt_bug where steps = '%s'" %bug_des
					count =  add_bug.query_count(query_sql)['count(*)']
#					print query_sql
#					print count
					if count == 0:
						add_bug.insert_one(sql)

	 	self.send_mai.send_main(pass_count,fail_count)
	# #将执行判断封装
	# #def get_cookie_run(self,header):


if __name__ == '__main__':
	run = RunTest()
	run.go_on_run()