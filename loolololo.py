# code for creating choropleth map of USA states
# import plotly library
import plotly
 
# import plotly.express module
# this module is used to create entire figures at once
import plotly.express as px
 
# create figure
fig = px.choropleth(locationmode="USA-states", color=[1], scope="usa")
 

#code for representing states of USA
#pass list of states in locations
#list will have two-letter abbreviations of states
fig = px.choropleth(locations=["AL", "AR", "CA", "CO", "FL", "GA", "IL", "KS", "KY", "MD", "MA", "MI", "MN", "MS", "NJ", "PA", "WA", "AR", "IN", "IA", "LA", "MO", "NE", "NY", "NC", "OH", "OK", "SC", "TN", "TX", "UT", "WV", "WI", "CT", "NV", "NM", "OR" , "VA"], locationmode="USA-states", color=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3], scope="usa")
 
fig.show()
