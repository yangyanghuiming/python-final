
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.charts import Line,Bar,Tab,Map,Timeline
import plotly as py
import plotly.graph_objs as go
UPLOAD_FOLDER = './data/'  # 文件存放路径

def get_picture1():
    df2 = pd.read_csv(UPLOAD_FOLDER + 'market size.csv', encoding='utf-8')
    df2 = df2.set_index("时间")
    x轴=[k for k in df2.columns.values[-5:]]
    泛娱乐核心产业规模=list(df2.loc["泛娱乐核心产业规模"].values)[-5:]
    无线音乐=list(df2.loc["无线音乐"].values)[-5:]
    在线视频=list(df2.loc["在线视频"].values)[-5:]
    电竞游戏=list(df2.loc["电竞游戏"].values)[-5:]
    移动阅读=list(df2.loc["移动阅读"].values)[-5:]
    手机游戏=list(df2.loc["手机游戏"].values)[-5:]
    t = (
        Line(init_opts=opts.InitOpts(theme='white',bg_color='#cacfd0'))
        .add_xaxis(x轴)
        .add_yaxis("泛娱乐核心产业规模",泛娱乐核心产业规模)
        .set_global_opts(title_opts=opts.TitleOpts(title="2014年—2018年泛娱乐核心产业规模",pos_left='center',title_textstyle_opts=opts.TextStyleOpts(color='#624630')),
                         
                        legend_opts=opts.LegendOpts(pos_top="10%"),
                        xaxis_opts=opts.AxisOpts(name="年份"),
                        yaxis_opts=opts.AxisOpts(name="泛娱乐核心产业规模(亿元)")
                        
                        )
        
    )
    b1 = (
        Bar(init_opts=opts.InitOpts(theme='white',bg_color='#cacfd0'))
        .add_xaxis(x轴)
        .add_yaxis("无线音乐", 无线音乐,color='#f1a9a2', category_gap='50%')
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2014年—2018年无线音乐​市场规模",pos_left='center',title_textstyle_opts=opts.TextStyleOpts(color='#624630')),
            legend_opts=opts.LegendOpts(pos_top="10%"),
            xaxis_opts=opts.AxisOpts(name="年份"),
            yaxis_opts=opts.AxisOpts(name="无线音乐​市场规模(亿元)",max_=900)
        )
    )
    b2 = (
        Bar(init_opts=opts.InitOpts(theme='white',bg_color='#cacfd0'))
        .add_xaxis(x轴)
        .add_yaxis("在线视频", 在线视频,color='#f1a9a2', category_gap='50%')
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2014年—2018年在线视频​市场规模",pos_left='center',title_textstyle_opts=opts.TextStyleOpts(color='#624630')),
            legend_opts=opts.LegendOpts(pos_top="10%"),
            xaxis_opts=opts.AxisOpts(name="年份"),
            yaxis_opts=opts.AxisOpts(name="在线视频​市场规模(亿元)",max_=900)
        )   
    )
    b3 = (
        Bar(init_opts=opts.InitOpts(theme='white',bg_color='#cacfd0'))
        .add_xaxis(x轴)
        .add_yaxis("电竞游戏", 电竞游戏,color='#f1a9a2', category_gap='50%')
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2014年—2018年电竞游戏​市场规模",pos_left='center',title_textstyle_opts=opts.TextStyleOpts(color='#624630')),
            legend_opts=opts.LegendOpts(pos_top="10%"),
            xaxis_opts=opts.AxisOpts(name="年份"),
            yaxis_opts=opts.AxisOpts(name="电竞游戏​市场规模(亿元)",max_=900)
        )
    )
    b4 = (
        Bar(init_opts=opts.InitOpts(theme='white',bg_color='#cacfd0'))
        .add_xaxis(x轴)
        .add_yaxis("移动阅读", 移动阅读,color='#f1a9a2', category_gap='50%')
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2014年—2018年移动阅读​市场规模",pos_left='center',title_textstyle_opts=opts.TextStyleOpts(color='#624630')),
            legend_opts=opts.LegendOpts(pos_top="10%"),
            xaxis_opts=opts.AxisOpts(name="年份"),
            yaxis_opts=opts.AxisOpts(name="移动阅读​市场规模(亿元)",max_=900)
        )
    )
    b5 = (
        Bar(init_opts=opts.InitOpts(theme='white',bg_color='#cacfd0'))
        .add_xaxis(x轴)
        .add_yaxis("手机游戏", 手机游戏,color='#f1a9a2', category_gap='50%')
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2014年—2018年手机游戏​市场规模",pos_left='center',title_textstyle_opts=opts.TextStyleOpts(color='#624630')),
            legend_opts=opts.LegendOpts(pos_top="10%"),
            xaxis_opts=opts.AxisOpts(name="年份"),
            yaxis_opts=opts.AxisOpts(name="手机游戏​市场规模(亿元)",max_=900)
        )
    )
    tab = Tab()
    tab.add(t, "泛娱乐核心产业规模")
    tab.add(b1, "无线音乐")
    tab.add(b2, "在线视频")
    tab.add(b3, "电竞游戏")
    tab.add(b4, "移动阅读")
    tab.add(b5, "手机游戏")
    fig = tab.render()
    return fig


def get_picture2():
    df = pd.read_csv(UPLOAD_FOLDER + 'Internet penetration.csv', encoding='utf-8')
    tl = Timeline()
    for i in range(2012, 2017):
        map0 = (
            Map()
            .add(
                "互联网普及率(%)",list(zip(list(df.地区),list(df["{}年".format(i)]))) , "china"
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="各地区互联网普及率变化".format(i)),
                visualmap_opts=opts.VisualMapOpts(max_=80),
            )
        )
        tl.add(map0, "{}年".format(i))
    fig = tl.render()
    return fig


def get_picture3():
    c = (
        Pie(init_opts=opts.InitOpts(theme='white',bg_color='#cacfd0'))
        .add(
            "",
            [list(z) for z in zip(["第一产业", "第二产业","第三产业"], [4.6,47.9,47.5])],
            center=["20%", "30%"],
            radius=[40, 70],
           
            

        )
        .add(
            "",
            [list(z) for z in zip(["第一产业", "第二产业","第三产业"], [4.5,42.5,53.0])],
            center=["55%", "30%"],
            radius=[40, 70],
           
        )
        .add(
            "",
            [list(z) for z in zip(["第一产业", "第二产业","第三产业"], [4.1,38.2,57.7])],
            center=["20%", "70%"],
            radius=[40, 70],

        )
        .add(
            "",
            [list(z) for z in zip(["第一产业", "第二产业","第三产业"], [4.8,35.7,59.6])],
            center=["50%", "70%"],
            radius=[40, 70],

        )
        .add(
            "",
            [list(z) for z in zip(["第一产业", "第二产业","第三产业"], [4.2,36.1,59.7])],
            center=["80%", "70%"],
            radius=[40, 70],
        
            

        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2014年—2018年三大产业对gdp的贡献率变化",subtitle="\n第一行左-右：2014年-2015年\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n第二行左-右：2016年-2018年"),
            legend_opts=opts.LegendOpts(
                type_="scroll", pos_top="20%", pos_left="80%", orient="vertical"
        ),)
            
    )

    fig = c.render()

    return fig



def get_picture4():
    df = pd.read_csv(UPLOAD_FOLDER + 'Urban and rural consumption expenditure.csv' , encoding='utf-8')
    df=df.set_index("指标")
    df_reset = df.loc[:,::-1]

    城镇居民人均教文娱消费支出=go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x),format="%m/%d/%Y")for x in df_reset.columns.values],
        y=df_reset.loc["城镇居民人均教文娱消费支出",:].values,
        name="城镇居民人均教文娱消费支出")
    农村居民人均教文娱消费支出 = go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in df_reset.columns.values],
        y=df_reset.loc["农村居民人均教文娱消费支出",:].values,
        name = "农村居民人均教文娱消费支出"
    )
    
    layout=dict(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=2,
                        label="2年",
                        step="year",
                        stepmode="backward"),
                    dict(count=4,
                        label="4年",
                        step="year",
                        stepmode="backward"),
                    dict(count=6,
                        label="6年",
                        step="year",
                        stepmode="backward"),
        
                    dict(step="all")
                ])
            ),
            rangeslider=dict(bgcolor="#FFC1C1"),
            title='年份'
        ),
        yaxis=dict(title='城乡居民人均教文娱消费支出（元）'),
        title="城乡居民人均教文娱消费支出"
    )
    fig=dict(data=[城镇居民人均教文娱消费支出,农村居民人均教文娱消费支出],layout=layout)
    py.offline.plot(fig, filename = 'example.html',auto_open=False)
    return 'example.html'
