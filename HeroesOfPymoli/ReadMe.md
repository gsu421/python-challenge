

```python
import pandas as pd
import numpy as np




```


```python
#Read in JSON file
file_path = "purchase_data.json"
pymoli_df = pd.read_json(file_path)
pymoli_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Write to csv
# pymoli_df.to_csv('fileOne.csv', index=False, header=True)
pymoli_df.columns
```


```python
# Player Count
    # Total Number of Players
player_count = pymoli_df['SN'].nunique()
print("Total Number of Player: ", player_count )






```

    Total Number of Player:  573



```python

# Purchasing Analysis (Total)
    # Number of Unique Items
item_count = pymoli_df['Item Name'].nunique()
    # Average Purchase Price
avg_price = pymoli_df['Price'].mean()
    # Total Number of Purchases
total_purchase = pymoli_df['Item ID'].count()
    # Total Revenue
rev = pymoli_df['Price'].sum()

print("Number of Unique Items: ", item_count)
print("Average Purchase Price: ", avg_price)
print("Total Number of Purchases", total_purchase)
print("Total Revenue", rev)

```

    Number of Unique Items:  179
    Average Purchase Price:  2.931192307692303
    Total Number of Purchases 780
    Total Revenue 2286.3299999999963



```python
# Gender Demographics

players_profile_df = pymoli_df[['Gender','SN']] #why is it a list of a list

#Remove Duplicates
players_profile_df = players_profile_df.drop_duplicates(subset='SN', keep='last', inplace=False)
gender_count_df = players_profile_df.groupby('Gender').count()




    # Percentage and Count of Male Players
    # Percentage and Count of Female Players
    # Percentage and Count of Other / Non-Disclosed


gender_df = pd.DataFrame({'Count_of': gender_count_df['SN']})
gender_df['Percentage']=gender_count_df['SN'].apply(lambda x: x/player_count) 

gender_df


```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Count_of</th>
      <th>Percentage</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>100</td>
      <td>0.174520</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>465</td>
      <td>0.811518</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>8</td>
      <td>0.013962</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Purchasing Analysis (Gender)
purchasing_df = pymoli_df.groupby('Gender')

    # The below each broken by gender
        # Purchase Count
purchase_count = purchasing_df['Price'].count()
        # Average Purchase Price
purchase_avg = purchasing_df['Price'].mean()
        # Total Purchase Value
purchase_total = purchasing_df['Price'].sum()
 
    # Normalized Totals (normalizing for the # of people in each gender group)
norm_total = purchase_total / gender_df.Count_of
    # See the first paragraph of this reference for more information on normalization.
pa_gender_df = pd.DataFrame({'Purchase Count': purchase_count, 
                   'Avg Purchase Price': purchase_avg, 
                   'Total Purchase Value': purchase_total,
                   'Normalized Totals': norm_total              
                    })
pa_gender_df

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Avg Purchase Price</th>
      <th>Normalized Totals</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>2.815515</td>
      <td>3.829100</td>
      <td>136</td>
      <td>382.91</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>2.950521</td>
      <td>4.016516</td>
      <td>633</td>
      <td>1867.68</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>3.249091</td>
      <td>4.467500</td>
      <td>11</td>
      <td>35.74</td>
    </tr>
  </tbody>
</table>
</div>




```python

# Age Demographics
    # The below each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)

age_bin = [0, 10, 14, 19, 24, 29, 34, 39, 44, 49 ]
age_label = ['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49']
pymoli_df['Age Group'] = pd.cut(pymoli_df['Age'], age_bin, labels=age_label)
# pd.cut(pymoli_df['Age'], age_bin, age_label)
age_df = pymoli_df.groupby('Age Group')



        # Purchase Count
purchase_count_age = age_df['Price'].count()

        # Average Purchase Price
purchase_avg_age = age_df['Price'].mean()

        # Total Purchase Value
purchase_total_age = age_df['Price'].sum()

        # Normalized Totals (normalizing for the # of people in each age group)
age_profile_df = pymoli_df.drop_duplicates(subset='SN', keep='last', inplace=False)
age_count_df = age_profile_df.groupby('Age Group').count()
norm_total_age = purchase_total_age / age_count_df.SN

pa_age_df = pd.DataFrame({
                          'Purchase Count': purchase_count_age,
                          'Avg Purchase Price': purchase_avg_age,
                          'Total Purchase Value': purchase_total_age,
                          'Normalized Totals': norm_total_age})


pa_age_df

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Avg Purchase Price</th>
      <th>Normalized Totals</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Age Group</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10-14</th>
      <td>2.702903</td>
      <td>4.189500</td>
      <td>31</td>
      <td>83.79</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>2.905414</td>
      <td>3.864200</td>
      <td>133</td>
      <td>386.42</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>2.913006</td>
      <td>3.779035</td>
      <td>336</td>
      <td>978.77</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>2.962640</td>
      <td>4.256667</td>
      <td>125</td>
      <td>370.33</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>3.082031</td>
      <td>4.196809</td>
      <td>64</td>
      <td>197.25</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>2.842857</td>
      <td>4.422222</td>
      <td>42</td>
      <td>119.40</td>
    </tr>
    <tr>
      <th>40-44</th>
      <td>3.189375</td>
      <td>5.103000</td>
      <td>16</td>
      <td>51.03</td>
    </tr>
    <tr>
      <th>45-49</th>
      <td>2.720000</td>
      <td>2.720000</td>
      <td>1</td>
      <td>2.72</td>
    </tr>
    <tr>
      <th>&lt;10</th>
      <td>3.019375</td>
      <td>4.391818</td>
      <td>32</td>
      <td>96.62</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Top Spenders
    # Identify the the top 5 spenders in the game by total purchase value, then list (in a table):
spenders_df = pymoli_df.groupby('SN')
purchase_total_spenders = spenders_df['Price'].sum()
purchase_count_spenders = spenders_df['Item ID'].count()
purchase_avg_spenders = purchase_total_spenders / purchase_count_spenders
        # SN
        # Purchase Count
        # Average Purchase Price
        # Total Purchase Value
top_spenders_df = pd.DataFrame({"Purchase Count": purchase_count_spenders,
                               "Average Purchase Price": purchase_avg_spenders, 
                               "Total Purchase Value": purchase_total_spenders
                               })

top_spenders_df.sort_values("Total Purchase Value", ascending=False).head(5)

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>3.412000</td>
      <td>5</td>
      <td>17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>3.390000</td>
      <td>4</td>
      <td>13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>3.185000</td>
      <td>4</td>
      <td>12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>4.243333</td>
      <td>3</td>
      <td>12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>3.860000</td>
      <td>3</td>
      <td>11.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
    # Most Popular Items
        # Identify the 5 most popular items by purchase count, then list (in a table):
        # Item ID
        # Item Name
        # Purchase Count
        # Item Price
        # Total Purchase Value
# popular_df = pymoli_df.groupby('Item ID')



popular_df = pymoli_df.groupby(['Item ID', 'Item Name', 'Price']) #Group by ID, Name, Price b/c they could all be indexed

purchase_count_popular = popular_df['Item ID'].count()
purchase_total_popular = popular_df['Price'].sum()

popular_items_df = pd.DataFrame({"Purchase Count": purchase_count_popular,
                                 "Total Purchase Value": purchase_total_popular
                                })

popular_items_df.sort_values("Purchase Count", ascending=False).head(5)



```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <th>2.35</th>
      <td>11</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <th>2.23</th>
      <td>11</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <th>2.07</th>
      <td>9</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>175</th>
      <th>Woeful Adamantite Claymore</th>
      <th>1.24</th>
      <td>9</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <th>1.49</th>
      <td>9</td>
      <td>13.41</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Most Profitable Items
    # Identify the 5 most profitable items by total purchase value, then list (in a table):
        # Item ID
        # Item Name
        # Purchase Count
        # Item Price
        # Total Purchase Value
popular_items_df.sort_values("Total Purchase Value", ascending=False).head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <th>4.14</th>
      <td>9</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <th>4.25</th>
      <td>7</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <th>4.95</th>
      <td>6</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <th>4.87</th>
      <td>6</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <th>3.61</th>
      <td>8</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>




```python
ipython nbconvert --to markdown notebook.ipynb --stdout
```


      File "<ipython-input-1-f75ad7d94293>", line 1
        ipython nbconvert --to markdown notebook.ipynb --stdout
                        ^
    SyntaxError: invalid syntax


