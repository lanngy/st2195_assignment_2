install.packages("tidyverse")

library(rvest)

html <- read_html("https://en.wikipedia.org/wiki/Comma-separated_values")

html %>% 
  html_element(".wikitable") %>% 
  html_table()

df<-html_table(html_nodes(cars, '.wikitable', fill=TRUE)
write.csv(df,file="cars.csv",row.names = FALSE)

