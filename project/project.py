import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file and return as DataFrame
def load_csv(filename):
    try:
        df = pd.read_csv(filename)
        print("\n✅ CSV file loaded successfully.\n")
        return df
    except Exception as e:
        print(f"❌ Error loading file: {e}")
        return None

# Show the first n rows of the DataFrame
def show_head(df, n=10):
    if df.empty:
        return "The dataset is empty."
    return df.head(n)

# Display basic summary statistics of the DataFrame
def show_basic_info(df):
    if df.empty or df.shape[1] == 0:
        return "DataFrame is empty or has no columns."
    return df.describe(include='all')

# Filter data based on a column and value
def filter_data(df, column, value):
    if column not in df.columns:
        raise ValueError("Column not found in DataFrame")
    return df[df[column].astype(str) == str(value)]

# Export DataFrame to a new CSV file
def export_data(df, output_filename):
    df.to_csv(output_filename, index=False)
    return True

# Generate a chart based on selected chart type and columns
def visualize_data(df, chart_type, x_column, y_column=None):
    if chart_type == 'bar':
        df[x_column].value_counts().plot(kind='bar')
    elif chart_type == 'line' and y_column:
        df.plot(x=x_column, y=y_column, kind='line')
    elif chart_type == 'scatter' and y_column:
        sns.scatterplot(x=df[x_column], y=df[y_column])
    elif chart_type == 'pie':
        df[x_column].value_counts().plot(kind='pie', autopct='%1.1f%%')
    else:
        raise ValueError("Invalid chart type or missing columns.")

    plt.title(f'{chart_type.title()} Chart')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()

# Main interactive loop
def main():
    original_df = None
    current_df = None

    while True:
        print("\n📊 Data Visualizer and Analyzer")
        print("1. Load CSV File")
        print("2. Show First 10 Rows")
        print("3. Show Basic Info")
        print("4. Filter Data")
        print("5. Export Data")
        print("6. Visualize Data")
        print("7. Reset to Original Data")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            filename = input("Enter CSV file name: ")
            filename = 'Data/' + filename
            original_df = load_csv(filename)
            current_df = original_df.copy() if original_df is not None else None

        elif choice == '2':
            if current_df is not None:
                print(show_head(current_df))
            else:
                print("⚠️ Please load a file first.")

        elif choice == '3':
            if current_df is not None:
                print(show_basic_info(current_df))
            else:
                print("⚠️ Please load a file first.")

        elif choice == '4':
            if current_df is not None:
                col = input("Enter column name to filter by: ")
                val = input("Enter value to match: ")
                try:
                    filtered = filter_data(current_df, col, val)
                    if filtered.empty:
                        print("⚠️ No rows match your filter. Data not updated.")
                    else:
                        current_df = filtered
                        print(current_df)
                except ValueError as e:
                    print(f"⚠️ {e}")
            else:
                print("⚠️ Please load a file first.")

        elif choice == '5':
            if current_df is not None:
                filename = input("Enter filename to export (e.g., output.csv): ")
                filename = 'Output/' + filename
                export_data(current_df, filename)
                print(f"✅ Data exported to {filename}")
            else:
                print("⚠️ Please load a file first.")

        elif choice == '6':
            if current_df is not None:
                chart_type = input("Enter chart type (bar, line, scatter, pie): ")
                x = input("Enter X-axis column: ")
                y = None
                if chart_type in ['line', 'scatter']:
                    y = input("Enter Y-axis column: ")
                try:
                    visualize_data(current_df, chart_type, x, y)
                except Exception as e:
                    print(f"⚠️ {e}")
            else:
                print("⚠️ Please load a file first.")

        elif choice == '7':
            if original_df is not None:
                current_df = original_df.copy()
                print("✅ Data has been reset to the original version.")
            else:
                print("⚠️ No original data to reset. Please load a file first.")

        elif choice == '8':
            print("👋 Exiting program. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    