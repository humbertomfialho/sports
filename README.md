# Activity Data Visualization Project

This project provides insightful visualizations based on fitness activity data. These visualizations help in understanding the distribution, averages, and comparisons of different metrics such as total calories, activated calories, and heart rate by activity type. The data for this analysis is collected by Apple Watch and written manually on Google Docs to be collected, and it requires specific configuration for access.

## Visualizations Included

1. Correlation Matrix
2. Pairplot Distribution
3. Monthly Activity Bar and Line Plot
4. Average Heart Rate by Activity Box Plot
5. Comparison of Total and Activated Calories
6. Box Plot for Total/Active Calories by Activity
7. Scatter Plot of Calories vs. Time by Activity Type

## Configuration

### Google Docs Connectivity
To fetch data for these visualizations, you need to configure access to Google Docs by placing your `key.json` file, which contains your Google API credentials, in the project's root directory. Ensure that this file has the appropriate permissions set to allow data retrieval without issues.

## Usage

1. Clone the repository to your local machine.
2. Place your `key.json` file in the root directory.
4. Run the script to generate the visualizations.

For detailed instructions on how to set up your Google API credentials and format your `key.json`, please refer to [Google Cloud Documentation](https://cloud.google.com/docs/authentication/getting-started).

## License

This project is released under the [GNU License](LICENSE).