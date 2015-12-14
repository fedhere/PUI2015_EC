# NYC_Small_Biz_Analytics
My first attempt at creating a simple recommender system.

This project demonstrates the capability of recommending small businesses for different NYC neighborhoods using the Yelp data.
Neighborhood names and locations are obtained from the ArcGIS book—NYC.gdb—Neighborhoods file. Only neighborhoods in Manhattan
and some neighborhoods in Brooklyn are selected for the convenience of analysis. The extracted file is called `nbhds.txt`.

## Steps to run

Run the code to convert the neighborhoods text file to csv:
`python file_converter.py`

To install the dependencies, run:
`pip install yelpapi`

Run the code to parse Yelp reviews:
`python y_parser.py`

Run `simple_analysis.ipynb` to see the similarity analysis based on cosine distance and the recommendation analysis based on 
the most similar neighborhood.

Run `analysis_w_matrix_factorization.ipynb` to see the analysis taking matrix factorization into account.

The recommended business results are illustrated in `results.jpg`, plotted using ArcGIS.
