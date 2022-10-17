```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
```


```python
data = pd.read_csv('C:/Users/Rakesh/Datasets/apple_products.csv')
```


```python
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Product Name</th>
      <th>Product URL</th>
      <th>Brand</th>
      <th>Sale Price</th>
      <th>Mrp</th>
      <th>Discount Percentage</th>
      <th>Number Of Ratings</th>
      <th>Number Of Reviews</th>
      <th>Upc</th>
      <th>Star Rating</th>
      <th>Ram</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>APPLE iPhone 8 Plus (Gold, 64 GB)</td>
      <td>https://www.flipkart.com/apple-iphone-8-plus-g...</td>
      <td>Apple</td>
      <td>49900</td>
      <td>49900</td>
      <td>0</td>
      <td>3431</td>
      <td>356</td>
      <td>MOBEXRGV7EHHTGUH</td>
      <td>4.6</td>
      <td>2 GB</td>
    </tr>
    <tr>
      <th>1</th>
      <td>APPLE iPhone 8 Plus (Space Grey, 256 GB)</td>
      <td>https://www.flipkart.com/apple-iphone-8-plus-s...</td>
      <td>Apple</td>
      <td>84900</td>
      <td>84900</td>
      <td>0</td>
      <td>3431</td>
      <td>356</td>
      <td>MOBEXRGVAC6TJT4F</td>
      <td>4.6</td>
      <td>2 GB</td>
    </tr>
    <tr>
      <th>2</th>
      <td>APPLE iPhone 8 Plus (Silver, 256 GB)</td>
      <td>https://www.flipkart.com/apple-iphone-8-plus-s...</td>
      <td>Apple</td>
      <td>84900</td>
      <td>84900</td>
      <td>0</td>
      <td>3431</td>
      <td>356</td>
      <td>MOBEXRGVGETABXWZ</td>
      <td>4.6</td>
      <td>2 GB</td>
    </tr>
    <tr>
      <th>3</th>
      <td>APPLE iPhone 8 (Silver, 256 GB)</td>
      <td>https://www.flipkart.com/apple-iphone-8-silver...</td>
      <td>Apple</td>
      <td>77000</td>
      <td>77000</td>
      <td>0</td>
      <td>11202</td>
      <td>794</td>
      <td>MOBEXRGVMZWUHCBA</td>
      <td>4.5</td>
      <td>2 GB</td>
    </tr>
    <tr>
      <th>4</th>
      <td>APPLE iPhone 8 (Gold, 256 GB)</td>
      <td>https://www.flipkart.com/apple-iphone-8-gold-2...</td>
      <td>Apple</td>
      <td>77000</td>
      <td>77000</td>
      <td>0</td>
      <td>11202</td>
      <td>794</td>
      <td>MOBEXRGVPK7PFEJZ</td>
      <td>4.5</td>
      <td>2 GB</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.isnull().sum()
```




    Product Name           0
    Product URL            0
    Brand                  0
    Sale Price             0
    Mrp                    0
    Discount Percentage    0
    Number Of Ratings      0
    Number Of Reviews      0
    Upc                    0
    Star Rating            0
    Ram                    0
    dtype: int64




```python
data.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sale Price</th>
      <th>Mrp</th>
      <th>Discount Percentage</th>
      <th>Number Of Ratings</th>
      <th>Number Of Reviews</th>
      <th>Star Rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>62.000000</td>
      <td>62.000000</td>
      <td>62.000000</td>
      <td>62.000000</td>
      <td>62.000000</td>
      <td>62.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>80073.887097</td>
      <td>88058.064516</td>
      <td>9.951613</td>
      <td>22420.403226</td>
      <td>1861.677419</td>
      <td>4.575806</td>
    </tr>
    <tr>
      <th>std</th>
      <td>34310.446132</td>
      <td>34728.825597</td>
      <td>7.608079</td>
      <td>33768.589550</td>
      <td>2855.883830</td>
      <td>0.059190</td>
    </tr>
    <tr>
      <th>min</th>
      <td>29999.000000</td>
      <td>39900.000000</td>
      <td>0.000000</td>
      <td>542.000000</td>
      <td>42.000000</td>
      <td>4.500000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>49900.000000</td>
      <td>54900.000000</td>
      <td>6.000000</td>
      <td>740.000000</td>
      <td>64.000000</td>
      <td>4.500000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>75900.000000</td>
      <td>79900.000000</td>
      <td>10.000000</td>
      <td>2101.000000</td>
      <td>180.000000</td>
      <td>4.600000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>117100.000000</td>
      <td>120950.000000</td>
      <td>14.000000</td>
      <td>43470.000000</td>
      <td>3331.000000</td>
      <td>4.600000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>140900.000000</td>
      <td>149900.000000</td>
      <td>29.000000</td>
      <td>95909.000000</td>
      <td>8161.000000</td>
      <td>4.700000</td>
    </tr>
  </tbody>
</table>
</div>



# Highest rated iphones in India(Flipkart)


```python
highest_rated= data.sort_values(by=['Star Rating'], ascending=False)
```


```python
highest_rated.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Product Name</th>
      <th>Product URL</th>
      <th>Brand</th>
      <th>Sale Price</th>
      <th>Mrp</th>
      <th>Discount Percentage</th>
      <th>Number Of Ratings</th>
      <th>Number Of Reviews</th>
      <th>Upc</th>
      <th>Star Rating</th>
      <th>Ram</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>20</th>
      <td>APPLE iPhone 11 Pro Max (Midnight Green, 64 GB)</td>
      <td>https://www.flipkart.com/apple-iphone-11-pro-m...</td>
      <td>Apple</td>
      <td>117100</td>
      <td>117100</td>
      <td>0</td>
      <td>1078</td>
      <td>101</td>
      <td>MOBFKCTSRYPAQNYT</td>
      <td>4.7</td>
      <td>4 GB</td>
    </tr>
    <tr>
      <th>17</th>
      <td>APPLE iPhone 11 Pro Max (Space Grey, 64 GB)</td>
      <td>https://www.flipkart.com/apple-iphone-11-pro-m...</td>
      <td>Apple</td>
      <td>117100</td>
      <td>117100</td>
      <td>0</td>
      <td>1078</td>
      <td>101</td>
      <td>MOBFKCTSKDMKCGQS</td>
      <td>4.7</td>
      <td>4 GB</td>
    </tr>
    <tr>
      <th>16</th>
      <td>APPLE iPhone 11 Pro Max (Midnight Green, 256 GB)</td>
      <td>https://www.flipkart.com/apple-iphone-11-pro-m...</td>
      <td>Apple</td>
      <td>131900</td>
      <td>131900</td>
      <td>0</td>
      <td>1078</td>
      <td>101</td>
      <td>MOBFKCTSCAAKGQV7</td>
      <td>4.7</td>
      <td>4 GB</td>
    </tr>
    <tr>
      <th>15</th>
      <td>APPLE iPhone 11 Pro Max (Gold, 64 GB)</td>
      <td>https://www.flipkart.com/apple-iphone-11-pro-m...</td>
      <td>Apple</td>
      <td>117100</td>
      <td>117100</td>
      <td>0</td>
      <td>1078</td>
      <td>101</td>
      <td>MOBFKCTSAPAYNSGG</td>
      <td>4.7</td>
      <td>4 GB</td>
    </tr>
    <tr>
      <th>14</th>
      <td>APPLE iPhone 11 Pro Max (Gold, 256 GB)</td>
      <td>https://www.flipkart.com/apple-iphone-11-pro-m...</td>
      <td>Apple</td>
      <td>131900</td>
      <td>131900</td>
      <td>0</td>
      <td>1078</td>
      <td>101</td>
      <td>MOBFKCTS7HCHSPFH</td>
      <td>4.7</td>
      <td>4 GB</td>
    </tr>
    <tr>
      <th>0</th>
      <td>APPLE iPhone 8 Plus (Gold, 64 GB)</td>
      <td>https://www.flipkart.com/apple-iphone-8-plus-g...</td>
      <td>Apple</td>
      <td>49900</td>
      <td>49900</td>
      <td>0</td>
      <td>3431</td>
      <td>356</td>
      <td>MOBEXRGV7EHHTGUH</td>
      <td>4.6</td>
      <td>2 GB</td>
    </tr>
    <tr>
      <th>29</th>
      <td>APPLE iPhone 12 (White, 128 GB)</td>
      <td>https://www.flipkart.com/apple-iphone-12-white...</td>
      <td>Apple</td>
      <td>75900</td>
      <td>84900</td>
      <td>10</td>
      <td>2101</td>
      <td>180</td>
      <td>MOBFWBYZBTZFGJF9</td>
      <td>4.6</td>
      <td>6 GB</td>
    </tr>
    <tr>
      <th>32</th>
      <td>APPLE iPhone 12 Pro Max (Graphite, 128 GB)</td>
      <td>https://www.flipkart.com/apple-iphone-12-pro-m...</td>
      <td>Apple</td>
      <td>120900</td>
      <td>129900</td>
      <td>6</td>
      <td>580</td>
      <td>45</td>
      <td>MOBFWBYZFDGQSDWS</td>
      <td>4.6</td>
      <td>6 GB</td>
    </tr>
    <tr>
      <th>35</th>
      <td>APPLE iPhone 12 (Black, 128 GB)</td>
      <td>https://www.flipkart.com/apple-iphone-12-black...</td>
      <td>Apple</td>
      <td>75900</td>
      <td>84900</td>
      <td>10</td>
      <td>2101</td>
      <td>180</td>
      <td>MOBFWBYZK3HACR72</td>
      <td>4.6</td>
      <td>6 GB</td>
    </tr>
    <tr>
      <th>36</th>
      <td>APPLE iPhone 12 (Blue, 128 GB)</td>
      <td>https://www.flipkart.com/apple-iphone-12-blue-...</td>
      <td>Apple</td>
      <td>75900</td>
      <td>84900</td>
      <td>10</td>
      <td>2101</td>
      <td>180</td>
      <td>MOBFWBYZKPTZF9VG</td>
      <td>4.6</td>
      <td>6 GB</td>
    </tr>
  </tbody>
</table>
</div>



# Number of ratings for iphones for the top 10


```python
highest_rated= highest_rated.head(10)
```


```python
iphones=highest_rated['Product Name'].value_counts()
```


```python
label=iphones.index
```


```python
counts=highest_rated['Number Of Ratings']
```


```python
figure=px.bar(highest_rated,x=label,y=counts, title= 'Number of ratings of highest rated iphones')
figure.show()
```


<div>                            <div id="1e13441e-5817-4a25-85ec-9f7019f2a888" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("1e13441e-5817-4a25-85ec-9f7019f2a888")) {                    Plotly.newPlot(                        "1e13441e-5817-4a25-85ec-9f7019f2a888",                        [{"alignmentgroup":"True","hovertemplate":"x=%{x}<br>Number Of Ratings=%{y}<extra></extra>","legendgroup":"","marker":{"color":"#636efa","pattern":{"shape":""}},"name":"","offsetgroup":"","orientation":"v","showlegend":false,"textposition":"auto","x":["APPLE iPhone 11 Pro Max (Midnight Green, 64 GB)","APPLE iPhone 11 Pro Max (Space Grey, 64 GB)","APPLE iPhone 11 Pro Max (Midnight Green, 256 GB)","APPLE iPhone 11 Pro Max (Gold, 64 GB)","APPLE iPhone 11 Pro Max (Gold, 256 GB)","APPLE iPhone 8 Plus (Gold, 64 GB)","APPLE iPhone 12 (White, 128 GB)","APPLE iPhone 12 Pro Max (Graphite, 128 GB)","APPLE iPhone 12 (Black, 128 GB)","APPLE iPhone 12 (Blue, 128 GB)"],"xaxis":"x","y":[1078,1078,1078,1078,1078,3431,2101,580,2101,2101],"yaxis":"y","type":"bar"}],                        {"template":{"data":{"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"choropleth":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"choropleth"}],"contour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"contour"}],"contourcarpet":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"contourcarpet"}],"heatmap":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"heatmap"}],"heatmapgl":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"heatmapgl"}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"histogram2d":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"histogram2d"}],"histogram2dcontour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"histogram2dcontour"}],"mesh3d":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"mesh3d"}],"parcoords":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"parcoords"}],"pie":[{"automargin":true,"type":"pie"}],"scatter":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter"}],"scatter3d":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter3d"}],"scattercarpet":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattercarpet"}],"scattergeo":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergeo"}],"scattergl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergl"}],"scattermapbox":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattermapbox"}],"scatterpolar":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolar"}],"scatterpolargl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolargl"}],"scatterternary":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterternary"}],"surface":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"surface"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}]},"layout":{"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"autotypenumbers":"strict","coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]],"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]},"colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"geo":{"bgcolor":"white","lakecolor":"white","landcolor":"#E5ECF6","showlakes":true,"showland":true,"subunitcolor":"white"},"hoverlabel":{"align":"left"},"hovermode":"closest","mapbox":{"style":"light"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"bgcolor":"#E5ECF6","radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","gridwidth":2,"linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white"},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","gridwidth":2,"linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white"},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","gridwidth":2,"linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white"}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"ternary":{"aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"bgcolor":"#E5ECF6","caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"title":{"x":0.05},"xaxis":{"automargin":true,"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","zerolinewidth":2},"yaxis":{"automargin":true,"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","zerolinewidth":2}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{"text":"x"}},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"Number Of Ratings"}},"legend":{"tracegroupgap":0},"title":{"text":"Number of ratings of highest rated iphones"},"barmode":"relative"},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('1e13441e-5817-4a25-85ec-9f7019f2a888');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>


APPLE iPhone 8 Plus (Gold, 64 GB) has the most ratings on Flipkart

# Number of reviews of the highest-rated iPhones on Flipkart


```python
iphones= highest_rated['Product Name'].value_counts()
```


```python
label=iphones.index
```


```python
counts=highest_rated['Number Of Reviews']
```


```python
figure=px.bar(highest_rated,x=label,y=counts)
```


```python
figure.show()
```


<div>                            <div id="8a1b2f1a-d06f-418a-bc52-eadff7fdb196" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("8a1b2f1a-d06f-418a-bc52-eadff7fdb196")) {                    Plotly.newPlot(                        "8a1b2f1a-d06f-418a-bc52-eadff7fdb196",                        [{"alignmentgroup":"True","hovertemplate":"x=%{x}<br>Number Of Reviews=%{y}<extra></extra>","legendgroup":"","marker":{"color":"#636efa","pattern":{"shape":""}},"name":"","offsetgroup":"","orientation":"v","showlegend":false,"textposition":"auto","x":["APPLE iPhone 11 Pro Max (Midnight Green, 64 GB)","APPLE iPhone 11 Pro Max (Space Grey, 64 GB)","APPLE iPhone 11 Pro Max (Midnight Green, 256 GB)","APPLE iPhone 11 Pro Max (Gold, 64 GB)","APPLE iPhone 11 Pro Max (Gold, 256 GB)","APPLE iPhone 8 Plus (Gold, 64 GB)","APPLE iPhone 12 (White, 128 GB)","APPLE iPhone 12 Pro Max (Graphite, 128 GB)","APPLE iPhone 12 (Black, 128 GB)","APPLE iPhone 12 (Blue, 128 GB)"],"xaxis":"x","y":[101,101,101,101,101,356,180,45,180,180],"yaxis":"y","type":"bar"}],                        {"template":{"data":{"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"choropleth":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"choropleth"}],"contour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"contour"}],"contourcarpet":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"contourcarpet"}],"heatmap":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"heatmap"}],"heatmapgl":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"heatmapgl"}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"histogram2d":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"histogram2d"}],"histogram2dcontour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"histogram2dcontour"}],"mesh3d":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"mesh3d"}],"parcoords":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"parcoords"}],"pie":[{"automargin":true,"type":"pie"}],"scatter":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter"}],"scatter3d":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter3d"}],"scattercarpet":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattercarpet"}],"scattergeo":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergeo"}],"scattergl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergl"}],"scattermapbox":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattermapbox"}],"scatterpolar":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolar"}],"scatterpolargl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolargl"}],"scatterternary":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterternary"}],"surface":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"surface"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}]},"layout":{"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"autotypenumbers":"strict","coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]],"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]},"colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"geo":{"bgcolor":"white","lakecolor":"white","landcolor":"#E5ECF6","showlakes":true,"showland":true,"subunitcolor":"white"},"hoverlabel":{"align":"left"},"hovermode":"closest","mapbox":{"style":"light"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"bgcolor":"#E5ECF6","radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","gridwidth":2,"linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white"},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","gridwidth":2,"linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white"},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","gridwidth":2,"linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white"}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"ternary":{"aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"bgcolor":"#E5ECF6","caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"title":{"x":0.05},"xaxis":{"automargin":true,"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","zerolinewidth":2},"yaxis":{"automargin":true,"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","zerolinewidth":2}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{"text":"x"}},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"Number Of Reviews"}},"legend":{"tracegroupgap":0},"margin":{"t":60},"barmode":"relative"},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('8a1b2f1a-d06f-418a-bc52-eadff7fdb196');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>


# Finding a relationship between sale price of iphones and their ratings in flipkart


```python
figure=px.scatter(data,x='Number Of Ratings',y='Sale Price',size='Discount Percentage', trendline='ols', title='Relationship between saleprice and number of ratings in flipkart')
```


```python
figure.show()
```


<div>                            <div id="13cef57a-6f1a-457f-9b43-15b219580360" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("13cef57a-6f1a-457f-9b43-15b219580360")) {                    Plotly.newPlot(                        "13cef57a-6f1a-457f-9b43-15b219580360",                        [{"hovertemplate":"Number Of Ratings=%{x}<br>Sale Price=%{y}<br>Discount Percentage=%{marker.size}<extra></extra>","legendgroup":"","marker":{"color":"#636efa","size":[0,0,0,0,0,0,0,0,0,20,16,20,20,20,0,0,0,0,29,15,0,15,17,18,6,6,13,6,14,10,7,6,6,13,13,10,10,6,14,6,10,6,11,11,10,14,7,6,6,6,8,8,24,22,22,22,8,24,14,14,14,14],"sizemode":"area","sizeref":0.0725,"symbol":"circle"},"mode":"markers","name":"","orientation":"v","showlegend":false,"x":[3431,3431,3431,11202,11202,3431,3431,11202,1454,79512,79512,79582,79512,79512,1078,1078,1078,1078,7088,7088,1078,7088,7081,95909,542,580,740,545,740,2101,545,580,580,730,730,2101,2101,580,740,580,2092,545,2101,2092,2101,740,545,580,580,580,43707,43707,95807,95909,95807,95909,43470,95909,43470,43470,43470,43470],"xaxis":"x","y":[49900,84900,84900,77000,77000,49900,49900,77000,89900,41999,39999,41999,41999,41999,131900,117100,131900,117100,74999,117900,117100,117900,99900,44999,140900,130900,64900,120900,59900,75900,110900,130900,120900,64900,64900,75900,75900,120900,59900,120900,75900,140900,70900,70900,75900,59900,110900,120900,130900,130900,54999,54999,29999,34999,34999,34999,54999,29999,46999,46999,46999,46999],"yaxis":"y","type":"scatter"},{"hovertemplate":"<b>OLS trendline</b><br>Sale Price = -0.712783 * Number Of Ratings + 96054.8<br>R<sup>2</sup>=0.492139<br><br>Number Of Ratings=%{x}<br>Sale Price=%{y} <b>(trend)</b><extra></extra>","legendgroup":"","marker":{"color":"#636efa","symbol":"circle"},"mode":"lines","name":"","showlegend":false,"x":[542,545,545,545,545,580,580,580,580,580,580,580,580,730,730,740,740,740,740,1078,1078,1078,1078,1078,1454,2092,2092,2101,2101,2101,2101,2101,3431,3431,3431,3431,3431,7081,7088,7088,7088,11202,11202,11202,43470,43470,43470,43470,43470,43707,43707,79512,79512,79512,79512,79582,95807,95807,95909,95909,95909,95909],"xaxis":"x","y":[95668.43493113318,95666.29658296306,95666.29658296306,95666.29658296306,95666.29658296306,95641.34918764498,95641.34918764498,95641.34918764498,95641.34918764498,95641.34918764498,95641.34918764498,95641.34918764498,95641.34918764498,95534.43177913892,95534.43177913892,95527.30395190518,95527.30395190518,95527.30395190518,95527.30395190518,95286.38339140486,95286.38339140486,95286.38339140486,95286.38339140486,95286.38339140486,95018.37708741635,94563.62170990389,94563.62170990389,94557.20666539353,94557.20666539353,94557.20666539353,94557.20666539353,94557.20666539353,93609.20564330647,93609.20564330647,93609.20564330647,93609.20564330647,93609.20564330647,91007.54870299235,91002.55922392874,91002.55922392874,91002.55922392874,88070.1710999692,88070.1710999692,88070.1710999692,65070.09818214562,65070.09818214562,65070.09818214562,65070.09818214562,65070.09818214562,64901.168676706046,64901.168676706046,39379.98326630958,39379.98326630958,39379.98326630958,39379.98326630958,39330.088475673416,27765.188788934625,27765.188788934625,27692.4849511505,27692.4849511505,27692.4849511505,27692.4849511505],"yaxis":"y","type":"scatter"}],                        {"template":{"data":{"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"choropleth":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"choropleth"}],"contour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"contour"}],"contourcarpet":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"contourcarpet"}],"heatmap":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"heatmap"}],"heatmapgl":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"heatmapgl"}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"histogram2d":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"histogram2d"}],"histogram2dcontour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"histogram2dcontour"}],"mesh3d":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"mesh3d"}],"parcoords":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"parcoords"}],"pie":[{"automargin":true,"type":"pie"}],"scatter":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter"}],"scatter3d":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter3d"}],"scattercarpet":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattercarpet"}],"scattergeo":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergeo"}],"scattergl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergl"}],"scattermapbox":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattermapbox"}],"scatterpolar":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolar"}],"scatterpolargl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolargl"}],"scatterternary":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterternary"}],"surface":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"surface"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}]},"layout":{"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"autotypenumbers":"strict","coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]],"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]},"colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"geo":{"bgcolor":"white","lakecolor":"white","landcolor":"#E5ECF6","showlakes":true,"showland":true,"subunitcolor":"white"},"hoverlabel":{"align":"left"},"hovermode":"closest","mapbox":{"style":"light"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"bgcolor":"#E5ECF6","radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","gridwidth":2,"linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white"},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","gridwidth":2,"linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white"},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","gridwidth":2,"linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white"}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"ternary":{"aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"bgcolor":"#E5ECF6","caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"title":{"x":0.05},"xaxis":{"automargin":true,"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","zerolinewidth":2},"yaxis":{"automargin":true,"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","zerolinewidth":2}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{"text":"Number Of Ratings"}},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"Sale Price"}},"legend":{"tracegroupgap":0,"itemsizing":"constant"},"title":{"text":"Relationship between saleprice and number of ratings in flipkart"}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('13cef57a-6f1a-457f-9b43-15b219580360');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>


 Here there is a negative linear relationship which means iphones with lower price are sold in India

# Relationship between discount percentage and number of ratings for iphones


```python
figure= px.scatter(data,x='Number Of Ratings', y='Discount Percentage',size='Sale Price',  trendline='ols', title='Relationship between discount percentage and number of ratings for iphones')
```


```python
figure.show()
```


<div>                            <div id="30d2cda1-f49f-4ed5-817e-ec65358bd892" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("30d2cda1-f49f-4ed5-817e-ec65358bd892")) {                    Plotly.newPlot(                        "30d2cda1-f49f-4ed5-817e-ec65358bd892",                        [{"hovertemplate":"Number Of Ratings=%{x}<br>Discount Percentage=%{y}<br>Sale Price=%{marker.size}<extra></extra>","legendgroup":"","marker":{"color":"#636efa","size":[49900,84900,84900,77000,77000,49900,49900,77000,89900,41999,39999,41999,41999,41999,131900,117100,131900,117100,74999,117900,117100,117900,99900,44999,140900,130900,64900,120900,59900,75900,110900,130900,120900,64900,64900,75900,75900,120900,59900,120900,75900,140900,70900,70900,75900,59900,110900,120900,130900,130900,54999,54999,29999,34999,34999,34999,54999,29999,46999,46999,46999,46999],"sizemode":"area","sizeref":352.25,"symbol":"circle"},"mode":"markers","name":"","orientation":"v","showlegend":false,"x":[3431,3431,3431,11202,11202,3431,3431,11202,1454,79512,79512,79582,79512,79512,1078,1078,1078,1078,7088,7088,1078,7088,7081,95909,542,580,740,545,740,2101,545,580,580,730,730,2101,2101,580,740,580,2092,545,2101,2092,2101,740,545,580,580,580,43707,43707,95807,95909,95807,95909,43470,95909,43470,43470,43470,43470],"xaxis":"x","y":[0,0,0,0,0,0,0,0,0,20,16,20,20,20,0,0,0,0,29,15,0,15,17,18,6,6,13,6,14,10,7,6,6,13,13,10,10,6,14,6,10,6,11,11,10,14,7,6,6,6,8,8,24,22,22,22,8,24,14,14,14,14],"yaxis":"y","type":"scatter"},{"hovertemplate":"<b>OLS trendline</b><br>Discount Percentage = 0.000154292 * Number Of Ratings + 6.49233<br>R<sup>2</sup>=0.468988<br><br>Number Of Ratings=%{x}<br>Discount Percentage=%{y} <b>(trend)</b><extra></extra>","legendgroup":"","marker":{"color":"#636efa","symbol":"circle"},"mode":"lines","name":"","showlegend":false,"x":[542,545,545,545,545,580,580,580,580,580,580,580,580,730,730,740,740,740,740,1078,1078,1078,1078,1078,1454,2092,2092,2101,2101,2101,2101,2101,3431,3431,3431,3431,3431,7081,7088,7088,7088,11202,11202,11202,43470,43470,43470,43470,43470,43707,43707,79512,79512,79512,79512,79582,95807,95807,95909,95909,95909,95909],"xaxis":"x","y":[6.5759534706633325,6.576416346230309,6.576416346230309,6.576416346230309,6.576416346230309,6.581816561178369,6.581816561178369,6.581816561178369,6.581816561178369,6.581816561178369,6.581816561178369,6.581816561178369,6.581816561178369,6.6049603395271985,6.6049603395271985,6.606503258083787,6.606503258083787,6.606503258083787,6.606503258083787,6.658653905296482,6.658653905296482,6.658653905296482,6.658653905296482,6.658653905296482,6.716667643024214,6.815105846934566,6.815105846934566,6.816494473635496,6.816494473635496,6.816494473635496,6.816494473635496,6.816494473635496,7.021702641661781,7.021702641661781,7.021702641661781,7.021702641661781,7.021702641661781,7.584867914816621,7.5859479578062325,7.5859479578062325,7.5859479578062325,8.220704651986784,8.220704651986784,8.220704651986784,13.199394250386892,13.199394250386892,13.199394250386892,13.199394250386892,13.199394250386892,13.23596142017804,13.23596142017804,18.760381312043535,18.760381312043535,18.760381312043535,18.760381312043535,18.771181741939657,21.274567100004667,21.274567100004667,21.29030486928187,21.29030486928187,21.29030486928187,21.29030486928187],"yaxis":"y","type":"scatter"}],                        {"template":{"data":{"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"choropleth":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"choropleth"}],"contour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"contour"}],"contourcarpet":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"contourcarpet"}],"heatmap":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"heatmap"}],"heatmapgl":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"heatmapgl"}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"histogram2d":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"histogram2d"}],"histogram2dcontour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"histogram2dcontour"}],"mesh3d":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"mesh3d"}],"parcoords":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"parcoords"}],"pie":[{"automargin":true,"type":"pie"}],"scatter":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter"}],"scatter3d":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter3d"}],"scattercarpet":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattercarpet"}],"scattergeo":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergeo"}],"scattergl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergl"}],"scattermapbox":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattermapbox"}],"scatterpolar":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolar"}],"scatterpolargl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolargl"}],"scatterternary":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterternary"}],"surface":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"surface"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}]},"layout":{"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"autotypenumbers":"strict","coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]],"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]},"colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"geo":{"bgcolor":"white","lakecolor":"white","landcolor":"#E5ECF6","showlakes":true,"showland":true,"subunitcolor":"white"},"hoverlabel":{"align":"left"},"hovermode":"closest","mapbox":{"style":"light"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"bgcolor":"#E5ECF6","radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","gridwidth":2,"linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white"},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","gridwidth":2,"linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white"},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","gridwidth":2,"linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white"}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"ternary":{"aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"bgcolor":"#E5ECF6","caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"title":{"x":0.05},"xaxis":{"automargin":true,"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","zerolinewidth":2},"yaxis":{"automargin":true,"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","zerolinewidth":2}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{"text":"Number Of Ratings"}},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"Discount Percentage"}},"legend":{"tracegroupgap":0,"itemsizing":"constant"},"title":{"text":"Relationship between discount percentage and number of ratings for iphones"}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('30d2cda1-f49f-4ed5-817e-ec65358bd892');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>



```python
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Product Name</th>
      <th>Product URL</th>
      <th>Brand</th>
      <th>Sale Price</th>
      <th>Mrp</th>
      <th>Discount Percentage</th>
      <th>Number Of Ratings</th>
      <th>Number Of Reviews</th>
      <th>Upc</th>
      <th>Star Rating</th>
      <th>Ram</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>APPLE iPhone 8 Plus (Gold, 64 GB)</td>
      <td>https://www.flipkart.com/apple-iphone-8-plus-g...</td>
      <td>Apple</td>
      <td>49900</td>
      <td>49900</td>
      <td>0</td>
      <td>3431</td>
      <td>356</td>
      <td>MOBEXRGV7EHHTGUH</td>
      <td>4.6</td>
      <td>2 GB</td>
    </tr>
    <tr>
      <th>1</th>
      <td>APPLE iPhone 8 Plus (Space Grey, 256 GB)</td>
      <td>https://www.flipkart.com/apple-iphone-8-plus-s...</td>
      <td>Apple</td>
      <td>84900</td>
      <td>84900</td>
      <td>0</td>
      <td>3431</td>
      <td>356</td>
      <td>MOBEXRGVAC6TJT4F</td>
      <td>4.6</td>
      <td>2 GB</td>
    </tr>
    <tr>
      <th>2</th>
      <td>APPLE iPhone 8 Plus (Silver, 256 GB)</td>
      <td>https://www.flipkart.com/apple-iphone-8-plus-s...</td>
      <td>Apple</td>
      <td>84900</td>
      <td>84900</td>
      <td>0</td>
      <td>3431</td>
      <td>356</td>
      <td>MOBEXRGVGETABXWZ</td>
      <td>4.6</td>
      <td>2 GB</td>
    </tr>
    <tr>
      <th>3</th>
      <td>APPLE iPhone 8 (Silver, 256 GB)</td>
      <td>https://www.flipkart.com/apple-iphone-8-silver...</td>
      <td>Apple</td>
      <td>77000</td>
      <td>77000</td>
      <td>0</td>
      <td>11202</td>
      <td>794</td>
      <td>MOBEXRGVMZWUHCBA</td>
      <td>4.5</td>
      <td>2 GB</td>
    </tr>
    <tr>
      <th>4</th>
      <td>APPLE iPhone 8 (Gold, 256 GB)</td>
      <td>https://www.flipkart.com/apple-iphone-8-gold-2...</td>
      <td>Apple</td>
      <td>77000</td>
      <td>77000</td>
      <td>0</td>
      <td>11202</td>
      <td>794</td>
      <td>MOBEXRGVPK7PFEJZ</td>
      <td>4.5</td>
      <td>2 GB</td>
    </tr>
  </tbody>
</table>
</div>


