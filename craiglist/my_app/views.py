import  requests
from django.shortcuts import render
from requests.compat import quote_plus
from bs4 import BeautifulSoup

BASE_URL = 'https://mumbai.craigslist.org/search/?query={}'
BASE_IMAGE_URL= 'https://images.craigslist.org/{}_300x300.jpg'


# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    final_url = BASE_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data=response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_listing = soup.find_all('li', {'class' : 'result-row'})

    final_postings = []

    for post in post_listing:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'N/A'

        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image_url = BASE_IMAGE_URL.format(post_image_id)
            # print(post_image_id)
        else:
            post_image_url ='https://bodhihealthedu.org/wp-content/uploads/2019/05/66579998-cute-funny-man-on-the-crossroad-with-question-symbol-on-the-blue-background-choice-or-decision-carto-300x300.jpg'

        final_postings.append((post_title, post_url, post_price, post_image_url)) 
  
    print(final_url)
    context = { 
        'search': search,
        'final_postings' : final_postings,
        }
    return render(request, 'my_app/new_search.html', context)