# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
# %reload_ext autoreload
# %autoreload 2
# from file_utils import *       # 独自関数群
# from misc_utils import *    # 独自関数群
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
# %matplotlib inline
# #%matplotlib widget
# # %config InlineBackend.figure_format = 'retina'  # レポート作成用
import os
import re
#sns.set(font=['osaka_unicode'])
np.set_printoptions(precision=20, suppress=True)
import matplotlib as mpl
mpl.rc('figure', facecolor='#eeeeee',figsize=(6.4,4.8))  # そのままpptに貼れるくらいのサイズ
mpl.rc('axes', facecolor='#ffffff',edgecolor="#dddddd")  # 背景白,ラベル部gray
mpl.rc('grid',color='#dddddd',linewidth=1)               # ラベル部と同色のグリッド
mpl.rc('axes', titlesize=18,labelsize=16,grid=True)
mpl.rc('xtick',labelsize=14)
mpl.rc('ytick',labelsize=14)
mpl.rc('legend',fontsize=14)
plt.rcParams['axes.axisbelow'] = True   # gridを最背面に
cmap = plt.get_cmap("tab10")       # tableau colormap
import warnings
#warnings.filterwarnings('ignore')  # 最初から無視するのは良くないのでコメントアウトしておく
DATA_ROOT='/Users/hao/data'

# %% [markdown]
# # github連携のテスト

# %%
import plotly
import plotly.graph_objs as go

plotly.offline.init_notebook_mode(connected=False)

plotly.offline.iplot({
    "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
    "layout": go.Layout(title="hello world")
})

# %% [markdown]
# 毎回結果が変わる出力が必要

# %%
# !date

# %%
# !id
