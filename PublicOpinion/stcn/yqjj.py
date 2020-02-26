import sys

from lxml import html

from PublicOpinion.stcn.base_stcn import STCN_Base
from PublicOpinion.stcn import stcn_utils as utils


class STCN_DJSJ(STCN_Base):
    # 独家数据
    def __init__(self):
        super(STCN_DJSJ, self).__init__()
        self.format_url = "http://yq.stcn.com/yqjj/{}.shtml"
        self.pages = True  # 是否需要翻页
        self.page_num = 21

    def _parse_list_body(self, body):
        '''
<div id="news_list2">
        <dl>
            <dt><a href="http://yq.stcn.com/2020/0217/15643794.shtml" target="_blank" title="中小企业，被“疫情”放大的“困境”和“自救之路”"><img src="2013/1216/1387175931959.jpg"></a></dt>
            <dd class="yq_tit"><a href="http://yq.stcn.com/2020/0217/15643794.shtml" target="_blank" title="中小企业，被“疫情”放大的“困境”和“自救之路”"><span>中小企业，被“疫情”放大的“困境”和“自救之路”</span>
            </a><em>2020-02-17 12:53</em></dd>
            <dd class="yq_exp">中小企业要开展“自救”首先要搞清楚这几年中小企业为什么会这么难？</dd>
        </dl>
        '''
        # print(body)
        # with open("hello.html", "w") as f:
        #     f.write(body)
        # sys.exit(0)
        doc = html.fromstring(body)
        items = utils.parse_list_items_4(doc)
        [self._add_article(item) for item in items]
        print(len(items))
        return items


if __name__ == "__main__":
    dj = STCN_DJSJ()
    dj._start()

    # detail_url = "http://yq.stcn.com/2017/0210/13044959.shtml"
    # page = dj._get(detail_url)
    # print(page)
    # ret = dj._parse_detail(page)
    # print(ret)