import datetime
import logging
import sys
import urllib
from urllib.request import urlretrieve

import xlrd

from margin.base import MarginBase

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class SzListSpider(MarginBase):
    def __init__(self):
        # 主页链接
        # self.web_url = 'http://www.szse.cn/disclosure/margin/object/index.html'
        # 有数据存在的起始时间
        self.start_dt = datetime.datetime(2010, 3, 29)
        # 文件下载链接  eg. 2020-05-07 random.random
        # 'http://www.szse.cn/api/report/ShowReport?SHOWTYPE=xlsx&CATALOGID=1834_xxpl&txtDate=2020-05-08&random=0.5377421243834375&TABKEY=tab1'
        self.base_file_url = 'http://www.szse.cn/api/report/ShowReport?SHOWTYPE=xlsx&CATALOGID=1834_xxpl&txtDate={}&random={}&TABKEY=tab1'
        # api 接口
        # self.base_api_url = 'http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1834_xxpl&txtDate=2010-04-01&tab1PAGENO=1&random=0.483243785962155'

    def read_xls(self):
        wb = xlrd.open_workbook('/Users/furuiyang/gitzip/JustSimpleSpider/margin/融资融券标的证券信息0508.xlsx')
        detail = wb.sheet_by_name("融资融券标的证券信息")
        # 总数据量
        rows = detail.nrows - 1
        # 表头信息
        heads = detail.row_values(0)
        print(heads)
        # ['证券代码', '证券简称', '融资标的', '融券标的', '当日可融资', '当日可融券', '融券卖出价格限制']
        # | id | SecuMarket | InnerCode | SecuCode | SecuAbbr | SerialNumber | ListDate            | TargetCategory | CREATETIMEJZ        | UPDATETIMEJZ
        # 数据
        items = []
        # list_date = datetime.datetime.strptime(str(dt), "%Y%m%d")
        # fields = ["SecuMarket", "InnerCode", 'SecuCode', 'SecuAbbr', 'SerialNumber', 'ListDate', 'TargetCategory', ]
        # for i in range(1, rows+1):
        #     data = detail.row_values(i)
        #     item = dict()
        #     item['SecuMarket'] = 83
        #     secu_code = data[0]
        #     item['SecuCode'] = secu_code
        #     item['InnerCode'] = self.get_inner_code(secu_code)
        #     item['SecuAbbr'] = data[1]
        #     item['SerialNumber'] = i
        #     item['ListDate'] = list_date
        #     item['TargetCategory'] = None
        #     # print(data)
        #     # print(item)
        #     client = self._init_pool(self.spider_cfg)
        #     self._save(client, item, self.detail_table_name, fields)
        #     items.append(item)
        #     try:
        #         client.dispose()
        #     except:
        #         logger.warning("dispose error")

    # def callbackfunc(self, blocknum, blocksize, totalsize):
    #     """
    #     回调函数
    #     :param blocknum: 已经下载的数据块
    #     :param blocksize:  数据块的大小
    #     :param totalsize: 远程文件的大小
    #     :return:
    #     """
    #     percent = 100.0 * blocknum * blocksize / totalsize
    #     if percent > 100:
    #         percent = 100
    #     sys.stdout.write("\r%6.2f%%" % percent)
    #     sys.stdout.flush()
    #
    # def load_xlsx(self, dt: datetime.datetime):
    #     """
    #     下载某一天的明细文件
    #     :param dt: eg.20200506
    #     :return:
    #     """
    #     dt = dt.strftime("%Y%m%d")
    #     url = self.csv_url.format(dt)
    #     # print(">>>>>>>", url)
    #     try:
    #         urlretrieve(url, "./data_dir/{}/{}.xls".format(self.year, dt), self.callbackfunc)
    #     except urllib.error.HTTPError:
    #         logger.warning("不存在这一天的数据{}".format(dt))
    #     except TimeoutError:
    #         logger.warning("超时 {} ".format(dt))
    #     except Exception as e:
    #         logger.warning("下载失败 : {}".format(e))
    #         raise Exception


if __name__ == "__main__":
    SzListSpider().read_xls()


    pass
