
from src.data_loader import DataLoader
from src.data_loader import DataLoader
from src.preprocessing import Preprocessor
from src.analysis import Analyzer
from src.visualization import Visualizer

print("Program started")
file_path = 'data/sales_data.xlsx'

loader = DataLoader(file_path)
df = loader.load_data()

if df is not None:
    print(df.head())
    
    preprocessor = Preprocessor(df)
    preprocessor.check_nulls()
    preprocessor.check_dtypes()
    preprocessor.save_data('data/processed_sales_data.pkl')

    # Analysis
    analyzer = Analyzer(df)
    analyzer.summary_statistics()
    analyzer.count_categories() 
    analyzer.profit_by_category()
    analyzer.profit_margin()
    analyzer.sub_category_analysis()


    # Visualization
    visualizer = Visualizer(df)
    visualizer.age_distribution()
    visualizer.gender_distribution()
    visualizer.age_vs_revenue()
    visualizer.profit_by_category_chart()
    visualizer.profit_margin_scatter()
    visualizer.sub_category_chart()

   
category = input("Enter Product Category to analyze (or ALL): ").strip()
if category.upper() != "ALL":
      filtered_df = df[df['Product_Category'] == category]
else:
        filtered_df = df.copy()

analyzer_filtered = Analyzer(filtered_df)
visualizer_filtered = Visualizer(filtered_df)

analyzer_filtered.profit_by_category()
visualizer_filtered.profit_by_category_chart()


