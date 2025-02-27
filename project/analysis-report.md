<div style="text-align: center;">
    <h2 style="font-size: 24px;"><strong>Did the U.S. and China trade war result in economic decoupling? A Data-Driven Analysis</strong></h2>
</div>

## **Introduction**
For decades, the economic interdependence between China and the U.S. has been profound. Recent tensions from 2018 to 2022 due raise in tariff for chinese imports by US president Donald Trump government raise the question: Are their economies drifting apart? The answer is mixed. U.S. imports of certain Chinese goods, like semiconductors and IT hardware, have dropped, while imports of laptops, phones, and toys have surged, especially during the COVID-19 pandemic. Trade policies and a push to diversify supply chains contribute to this partial disentanglement. However, these actions come with repercussions, including supply chain disruptions and increased costs. Let's interpret these actions further.

## **Used Data**:
### **Pipeline A**:
This pipeline imports tariffs applied on each quantity based on the Harmonized Tariff Schedule (HTS), a U.S. system for classifying imported goods. For example, HTS Code 8471.30.01 classifies laptops and portable computers. The pipeline classifies the imports in time series and categories based on HTS codes. This dataset is intended for public access and use. License: us-pd  

### Harmonized Tariff Schedule (HTS) with Tariffs  
Example
| **HTS Number** | **Description**           | **Unit** | **General Duty** | **Special Duty** | **Column 2 Duty** | **Quota** | **Additional Duties** |
|----------------|---------------------------|----------|------------------|------------------|-------------------|-----------|-----------------------|
| 8471.30.01     | Laptops and portable computers | Number   | Free             | Free             | 35%               | None      | N/A                   |

### **Pipeline B**:
This pipeline imports the quantities of data imports from different countries based on HTS in time series from USA Trade® Online using selenium automation. This provides the raw materials and direct finished goods consumption. Further, I can also analyze the consumption trends if commodities from other countries have been used more. The license will be strictly followed by me by providing citations, un-manipulated and without bias.  
        

### Volume of imports from China
Example
| **Nominal Value (million USD)** | **China, Lists 1,2,3 ROW** | **Lists 1,2,3 China** | **List 4A ROW** | **List 4A China** | **Not on Any List ROW** | **Not on Any China** |
|---------------------------------|----------------------------|-----------------------|------------------|-------------------|-------------------------|----------------------|
| 500                             | 150                        | 120                   | 80               | 60                | 70                      | 20                   |

## **Analysis**
By calculating the percentage of goods which was imported gives us the amount of consumption by the US. The slope of the graph is calculated, using linear regression to understand the rate of change in imports over time. Mapping this slope with percentage changes quantifies the impact of tariffs.


### **Plot 1**
The analysis done based on tariffs applied on group of Lists like List 1, 2, 3 with 25% raise in tariff, list 4A with 7.5% tariff where US government put tariff only on these Chinese list of products and rest of the world with no tariff.
<div style="text-align: center;">
    <img src="./pic1.png" alt="Alt Text" title="Optional Title" style="width: auto; height: auto;">
    <p><strong>Figure 1:</strong> US imports from Rest of World and China in 2018-2022</p>
</div>
As expected, the trade war has had the largest impact on imports from China of products hit with the highest US tariffs. US imports from China of goods currently facing a 25 percent duty (Lists 1, 2, and 3) remain 22 percent below pre-trade war levels. US imports of those same products from the rest of the world are now 34 percent higher. US imports from China of products currently subject to 7.5 percent tariffs (List 4A) remain 3 percent below levels in August 2019 (right before the imposition of tariffs on those products), whereas comparable imports from the rest of the world are now 45 percent higher.

### **Plot 2**
Beginning in 2020, COVID-19 lockdowns led many Americans to work, school, and play from home, which sharply increased demand for certain products, many of which were imported predominately from China. These are the lists that had no tariff imposed and show little evidence of decoupling as there are no decrease in imports compared to rest of the world.
<div style="text-align: center;">
    <img src="./pic2.png" alt="Alt Text" title="Optional Title" style="width: auto; height: auto;">
    <p><strong>Figure 2:</strong> Value of US imports from china not hit by trade war</p>
</div>

### **Plot 3**
US Imports from China Subject to Section 301 Tariffs, by Product List (Percent of Total Imports from China)

| **Product Grouping** | **Year Prior to Trade War** *(July 2017 - June 2018)* | **Most Recent Year** *(September 2021 - August 2022)* |
|----------------------|-------------------------------------------------------|-------------------------------------------------------|
| **Not Subject to Tariffs** | | |
| Total | 33 | 47 |
| Laptops and monitors | 8 | 11 |
| Phones, including smartphones | 9 | 9 |
| Video game consoles | 1 | 2 |
| Toys | 3 | 5 |
| Others not subject to tariffs | 12 | 20 |
| **Subject to 25 Percent Tariff (Lists 1, 2, or 3)** | | |
| Total | 47 | 34 |
| Selected IT hardware and consumer electronics* | 5 | 2 |
| Auto parts | 2 | 2 |
| Furniture | 6 | 4 |
| Semiconductors | 1 | 1 |
| Others on Lists 1, 2, or 3 | 33 | 26 |
| **Subject to 7.5 Percent Tariff (List 4A)** | | |
| Total | 20 | 19 |
| Clothing and footwear | 7 | 6 |
| Personal protective equipment (PPE) and COVID-19 products** | 1 | 2 |
| Exercise equipment | 1 | 1 |
| Lithium batteries, including for electric vehicles | 0 | 1 |
| Others on List 4A | 11 | 9 |

\* Includes products such as data servers, modems, routers, wireless headphones, and smartwatches.  
\** Includes masks, gloves, and other pandemic-related supplies.

## **Conclusion**
Yes,from above analysis decoupling has happened and affected Chinese supply chain from these plots. For some products, the evidence here shows the United States increasingly sourcing imports assembled in countries other than China. The United States now buys more expensive imports from third countries that it once bought but no longer buys from China because of the tariffs. The changes in imports shown here are consistent with other evidence that rest of the world, are now trading more, including with the United States, in response to the US-China trade war.
US tariffs are not the only “cause” of the United States importing less from China. Some labor-intensive production closely associated with much of the clothing and footwear industry was likely relocating anyway, following a trend that was visible even before the trade war.
Policymakers therefore need to interpret even this preliminary evidence of some US-China “decoupling” with extreme caution.

### **Note**
This document is part of an academic research study. All data presented herein has been sourced from open-source and publicly available information. The research adheres to ethical guidelines, ensuring transparency and accuracy in data usage and analysis. AI tools were utilized exclusively for grammar checks and formatting purposes to enhance readability. No AI intervention was involved in the core research, data interpretation, or conclusion derivation.
