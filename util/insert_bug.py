# --*-- coding= utf8 --*--
import  MySQLdb.cursors
import json
class Add_bug:
    def __init__(self):
        self.conn = MySQLdb.connect(
            host = '192.168.1.56',
            port = 3306,
            user = 'root',
            db = 'zentao',
            charset = 'utf8',
            cursorclass =  MySQLdb.cursors.DictCursor
        )
        self.cur = self.conn.cursor()

     #插入一条BUG
    def insert_one(self,sql):
		self.cur.execute(sql)
		result = self.cur.fetchone()
		result = json.dumps(result)

     #查询数据库
    def query_count(self,sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        return result

if __name__ == '__main__':
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
    '<p>1、进入商户单位信息列表功能页面</p>\r\n<p>2、点击新增添加一条商户单位信息</p>\r\n<p>3、页面刷新显示出多页</p>\r\n<p>4、点击搜索后页面恢复原状，需要定位下多页数据哪里来的</p>', \
    'active', '1', '0', '', '', '', 'trunk', 'open', '', 'hezm', 'active', 'trunk', '', '', '', '0', '', '0', '0', '0', '0', '', '', '0')
        '''
	op_mysql = Add_bug()
	res = op_mysql.insert_one(sql)
