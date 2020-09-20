from flask import Flask,render_template
from pyecharts import options as opts
from pyecharts.charts import Geo,Map,Timeline,Page,Bar,Tab, Grid, Line,Scatter
from pyecharts.globals import ChartType, SymbolType,ThemeType
import pandas as pd
app = Flask(__name__)
农业女性就业 = pd.read_csv('API_SL.AGR.csv',index_col="Country Name")
工业女性就业 = pd.read_csv('API_SL.IND.csv',index_col="Country Name")
服务业女性就业 = pd.read_csv('API_SL.SRV.csv',index_col="Country Name")

@app.route('/')
def nong_base() -> Line:
    df = pd.read_csv('API_SL.AGR.csv')
    df = pd.read_csv('API_SL.IND.csv')
    df = pd.read_csv('API_SL.SRV.csv')
    c = (
            Line()
                .add_xaxis([str(x) for x in 农业女性就业.columns.values[19:31]])
                .add_yaxis("美国", list(农业女性就业.loc['United States'].values)[19:31])
                .add_yaxis("中国", list(农业女性就业.loc['China'].values)[19:31])
                .add_yaxis("日本", list(农业女性就业.loc['Japan'].values)[19:31])
                .add_yaxis("德国", list(农业女性就业.loc['Germany'].values)[19:31])
                .add_yaxis("英国", list(农业女性就业.loc['United Kingdom'].values)[19:31])
                .set_global_opts(title_opts=opts.TitleOpts(title="农业女性就业（占女性就业的百分比）", subtitle="世界发达国家十年数据"))
        )
    c.render("./templates/nongye.html")
    with open("./templates/nongye.html", encoding="utf8", mode="r") as f:
            sym = "".join(f.readlines())
            return render_template('1.html',
                                   the_sym=sym,
                                               )

@app.route('/1')
def timeline_map1() -> Timeline:
    a = Timeline()
    for i in range(2010, 2020):
        m = (
            Map()
                .add("农业女性就业率",zip(list(农业女性就业.index),list(农业女性就业["{}".format(i)])), "world",
                is_map_symbol_show=False)
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年农业女性就业情况".format(i), subtitle=""),
                visualmap_opts=opts.VisualMapOpts(max_=100, is_piecewise=True),

            )
        )
        a.add(m, "{}".format(i))
    a.render("./templates/ditu.html")
    with open("./templates/ditu.html", encoding="utf8", mode="r") as f:
        sym = "".join(f.readlines())
        return render_template('2.html',
                               the_sym=sym,
                               )

@app.route('/2')
def fuwu_base() -> Line:
    c = (
        Line()
        .add_xaxis([str(x)for x in 服务业女性就业.columns.values[19:31]])
        .add_yaxis("美国",list(服务业女性就业.loc['United States'].values)[19:31])
        .add_yaxis("中国",list(服务业女性就业.loc['China'].values)[19:31])
        .add_yaxis("日本",list(服务业女性就业.loc['Japan'].values)[19:31])
        .add_yaxis("德国",list(服务业女性就业.loc['Germany'].values)[19:31])
        .add_yaxis("英国",list(服务业女性就业.loc['United Kingdom'].values)[19:31])
        .set_global_opts(title_opts=opts.TitleOpts(title="服务业女性就业（占女性就业的百分比）", subtitle="世界发达国家十年数据"))
    )
    c.render("./templates/fuwuye.html")
    with open("./templates/fuwuye.html", encoding="utf8", mode="r") as f:
            sym = "".join(f.readlines())
            return render_template('3.html',
                                   the_sym=sym,
                                               )
@app.route('/3')
def timeline_map3() -> Timeline:
        a = Timeline()
        for i in range(2010, 2020):
            m = (
                Map()
                    .add("服务业女性就业率", zip(list(服务业女性就业.index), list(服务业女性就业["{}".format(i)])), "world",
                         is_map_symbol_show=False)
                    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                    .set_global_opts(
                    title_opts=opts.TitleOpts(title="{}年服务业女性就业情况".format(i), subtitle=""),
                    visualmap_opts=opts.VisualMapOpts(max_=100, is_piecewise=True),

                )
            )
            a.add(m, "{}".format(i))
            a.add(m, "{}".format(i))
        a.render("./templates/ditu.html")
        with open("./templates/ditu.html", encoding="utf8", mode="r") as f:
            sym = "".join(f.readlines())
            return render_template('4.html',
                                   the_sym=sym,
                                   )

@app.route('/4')
def gong_base() -> Bar:
    c = (
        Bar()
        .add_xaxis([str(x)for x in 工业女性就业.columns.values[19:31]])
        .add_yaxis("美国",list(工业女性就业.loc['United States'].values)[19:31])
        .add_yaxis("中国",list(工业女性就业.loc['China'].values)[19:31])
        .add_yaxis("日本",list(工业女性就业.loc['Japan'].values)[19:31])
        .add_yaxis("德国",list(工业女性就业.loc['Germany'].values)[19:31])
        .add_yaxis("英国",list(工业女性就业.loc['United Kingdom'].values)[19:31])
        .set_global_opts(title_opts=opts.TitleOpts(title="工业女性就业（占女性就业的百分比）", subtitle="世界发达国家十年数据"))
    )
    c.render("./templates/gongye.html")
    with open("./templates/gongye.html", encoding="utf8", mode="r") as f:
        sym = "".join(f.readlines())
        return render_template('5.html',
                               the_sym=sym,
                               )


@app.route('/5')
def timeline_map2() -> Timeline:
    a = Timeline()
    for i in range(2010, 2020):
        m = (
            Map()
                .add("工业女性就业率",zip(list(工业女性就业.index),list(工业女性就业["{}".format(i)])), "world",
                is_map_symbol_show=False)
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年工业女性就业情况".format(i), subtitle=""),
                visualmap_opts=opts.VisualMapOpts(max_=100, is_piecewise=True),

            )
        )
        a.add(m, "{}".format(i))
    a.render("./templates/ditu.html")
    with open("./templates/ditu.html", encoding="utf8", mode="r") as f:
        sym = "".join(f.readlines())
        return render_template('6.html',
                               the_sym=sym,
                               )





if __name__ == '__main__':
    app.run()
