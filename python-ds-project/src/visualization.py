import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import seaborn as sns
import os

class Visualizer:

    def __init__(self, df):
        self.df = df

    def age_distribution(self):
        print("Running age_distribution")
        os.makedirs("outputs", exist_ok=True)
        plt.figure()
        sns.histplot(self.df['Customer_Age'], bins=10)
        plt.title("Age Distribution")
        plt.savefig("outputs/age_distribution.png")
        plt.close()

    def gender_distribution(self):
        print("Running gender_distribution")
        os.makedirs("outputs", exist_ok=True)

        plt.figure()
        self.df['Gender'].value_counts().plot.pie(
            autopct='%1.1f%%', colors=['skyblue','pink']
        )
        plt.title("Gender Distribution")
        plt.savefig("outputs/gender_distribution.png")
        plt.close()

    def age_vs_revenue(self):
        print("Running age_vs_revenue")
        os.makedirs("outputs", exist_ok=True)

        plt.figure()
        data = self.df.groupby('Customer_Age')['Revenue'].sum()
        data.plot(kind='bar')
        plt.title("Age vs Revenue")
        plt.savefig("outputs/age_vs_revenue.png")
        plt.close()

    def profit_by_category_chart(self):
        print("Running profit_by_category_chart")
        os.makedirs("outputs", exist_ok=True)

        plt.figure()
        data = self.df.groupby('Product_Category')['Profit'].sum()
        data.plot(kind='barh')
        plt.title("Profit by Category")
        plt.savefig("outputs/profit_by_category.png")
        plt.close()


    def profit_margin_scatter(self):
        print("Running profit_margin_scatter")
        os.makedirs("outputs", exist_ok=True)

        plt.figure()
        plt.scatter(self.df['Revenue'], self.df['Profit'])
        plt.xlabel("Revenue")
        plt.ylabel("Profit")
        plt.title("Profit vs Revenue")
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.savefig("outputs/profit_scatter.png")
        plt.close()

    def sub_category_chart(self):
        print("Running sub_category_chart")
        os.makedirs("outputs", exist_ok=True)

        data = self.df.groupby(['Product_Category', 'Gender'])['Profit'].sum().unstack()
        data.plot(kind='bar', stacked=True)
        plt.title("Profit by Category and Gender")
        plt.xlabel("Product Category")
        plt.ylabel("Profit")
        plt.xticks(rotation=0)
        plt.legend(title="Gender")
        plt.tight_layout()
        plt.savefig("outputs/sub_category_profit.png")
        plt.close()