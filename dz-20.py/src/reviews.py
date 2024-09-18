
def show_reviews(reviews: list) ->list:
     
         review = input("ведить видгук:")
         reviews.append(review)
         input("")
         return reviews



def palindromes(reviews: list) ->None:
         for review in reviews:
              print(review)       



def show_reviews(reviews: list) ->None:
         reviews =" ".join(reviews) 


         repeated_chart = set() 
         for  i in range(len(reviews)):
              for f in range(i+1, len(reviews)):
                   if reviews.count(reviews[i:f]) >= 2:
                        repeated_chart.add(reviews[i:f])  
         print(f"{repeated_chart}")   

