


def parse_list_first(doc):
    '''
<dl class="hotNews">
    <dt>
        <a href="http://kcb.stcn.com/2020/0225/15680344.shtml" target="_blank" title="包容性强 科创板成TMT企业IPO上市首选"><img src="http://upload.stcn.com/2019/0506/1557126325788.jpg"></a>
    </dt>
    <dd class="tit">
        <a href="http://kcb.stcn.com/2020/0225/15680344.shtml" target="_blank" title="包容性强 科创板成TMT企业IPO上市首选">包容性强 科创板成TMT企业IPO上市首选</a>
    </dd>
    <dd class="exp">
        近日，普华永道发布的《2019年下半年中国科技媒体通信行业（TMT）IPO回顾与前瞻》（下称报告，TMT代指科技、媒体及通讯行业）显示，科创板的设立以及注册制的试点为科创类企业创造了良好的市场环境。            </dd>
    <dd class="sj">2020-02-25<span>07:56</span></dd>
</dl>
    '''
    first = doc.xpath("//dl[@class='hotNews']")[0]
    title = first.xpath("//dt/a/@title")[0]
    link = first.xpath("//dt/a/@href")[0]
    pub_date = first.xpath("//dd[@class='sj']")[0].text_content()
    pub_date = '{} {}'.format(pub_date[:10], pub_date[10:])
    first = dict()
    first['title'] = title
    first['link'] = link
    first['pub_date'] = pub_date
    return first


def parse_list_items_1(doc):
    '''
<ul class="news_list" id="idData">
    <li>
        <p class="tit">
            <a href="http://finance.stcn.com/2020/0225/15680453.shtml" target="_blank" title="科技类ETF基金火爆 53只科技股获基金抱团持有">科技类ETF基金火爆 53只科技股获基金抱团持有</a>
        </p>
        <p class="exp"></p>
        <p class="sj">2020-02-25<span>08:38</span></p>
    </li>
    '''
    items = []
    columns = doc.xpath("//ul[@class='news_list']/li")
    num = 0
    for column in columns:
        num += 1
        title = column.xpath("./p[@class='tit']/a/@title")[0]
        link = column.xpath("./p[@class='tit']/a/@href")[0]
        pub_date = column.xpath("./p[@class='sj']")[0].text_content()
        pub_date = '{} {}'.format(pub_date[:10], pub_date[10:])
        item = dict()
        item['title'] = title
        item['link'] = link
        item['pub_date'] = pub_date
        items.append(item)
    print("all nums is {}".format(num))
    return items


def parse_list_items(doc):
    '''
<ul class="news_list">
    <li class="tit">
        <a href="http://kcb.stcn.com/2020/0225/15680310.shtml" target="_blank" title="科创板公司有序复产 办公方式各不同 ">科创板公司有序复产 办公方式各不同 </a>
        <span>2020-02-25<i>07:42</i></span>
        <dl>
            <dt><a href="http://kcb.stcn.com/2020/0225/15680310.shtml" target="_blank" title="科创板公司有序复产 办公方式各不同 "><img src="http://upload.stcn.com/2019/0729/thumb_108_72_1564367167535.png"></a></dt>
            <dd>眼下，科创板上市公司已开始有序复工复产。由于不同公司经营业务和性质不同，复工复产的进度以及应对方式也有所不同。</dd>
        </dl>
    </li>
    '''
    items = []
    columns = doc.xpath("//ul[@class='news_list']/li")
    num = 0
    for column in columns:
        num += 1
        # print(column.tag)
        title = column.xpath("./a/@title")[0]
        link = column.xpath("./a/@href")[0]
        pub_date = column.xpath("./span")[0].text_content()
        pub_date = '{} {}'.format(pub_date[:10], pub_date[10:])
        item = dict()
        item['title'] = title
        item['link'] = link
        item['pub_date'] = pub_date
        items.append(item)
    return items