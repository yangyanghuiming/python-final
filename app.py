from flask import Flask, render_template, request
from pyecharts.charts import Map, Geo, EffectScatter
from pyecharts import options as opts
from pyecharts.charts import Pie
import pandas as pd
import cufflinks as cf
import plotly as py
import getpicture
import json

app = Flask(__name__)

# 准备工作
cf.set_config_file(offline=True, theme="ggplot")

py.offline.init_notebook_mode()

@app.route('/getSelect', methods=['GET', 'POST'])
def get_select() -> 'html':
    select = {
        "picture1" : "泛娱乐核心产业规模",
        "picture2" :  "各地区互联网普及率",
        "picture3" :  "三大产业对GDP的贡献率变化",
        "picture4" :  "城乡居民人均教文娱消费支出"
    }
    return json.dumps(select)
        

@app.route('/', methods=['GET'])
def get_index():
    with open('tittle.html', encoding="utf8", mode="r") as f:
        tittle = "".join(f.readlines())

    return render_template('results.html', the_tittle=tittle,)


@app.route('/', methods=['POST'])
def show() -> 'html':
    the_select = request.values.get('the_region_selected')
    if(the_select=="picture1"):
        path = getpicture.get_picture1()
        analyse = './analyse/analyse1.html'
    if(the_select=="picture2"):
        path = getpicture.get_picture2()
        analyse = './analyse/analyse2.html'
    if(the_select=="picture3"):
        path = getpicture.get_picture3()
        analyse = './analyse/analyse3.html'
    if(the_select=="picture4"):
        path = getpicture.get_picture4()
        analyse = './analyse/analyse4.html'
 
    with open('tittle.html', encoding="utf8", mode="r") as f:
        tittle = "".join(f.readlines())

    with open(path, encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

    with open(analyse, encoding="utf8", mode="r") as f:
        describe = "".join(f.readlines())

    # plotly.offline.plot(data, filename='file.html')
    return render_template('results.html', the_plot_all=plot_all,the_tittle=tittle,
                           the_describe=describe)


if __name__ == '__main__':
    app.run(debug=True, port=8000)

