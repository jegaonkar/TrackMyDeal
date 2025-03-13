def popularDeals(request):
    sample_deals = [
        {"name": "iPhone 14", "price": "$799", "image_url": "https://via.placeholder.com/150", "link": "#"},
        {"name": "Samsung Galaxy S23", "price": "$699", "image_url": "https://via.placeholder.com/150", "link": "#"},
        {"name": "Sony Headphones", "price": "$199", "image_url": "https://via.placeholder.com/150", "link": "#"},
    ]
    return {'popular_deals': sample_deals}

def carousel_items(request):
    carousel_items = [
        {
            "id": 1,
            "image_url": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=1600&q=80",
            "title": "Trending Tech Deals",
            "subtitle": "Save up to 40% on latest gadgets"
        },
        {
            "id": 2,
            "image_url": "https://images.unsplash.com/photo-1555774698-0b77e0d5fac6?auto=format&fit=crop&w=1600&q=80",
            "title": "Summer Sale",
            "subtitle": "Hot deals for the season"
        },
        {
            "id": 3,
            "image_url": "https://images.unsplash.com/photo-1550009158-9ebf69173e03?auto=format&fit=crop&w=1600&q=80",
            "title": "Home Essentials",
            "subtitle": "Everything for your smart home"
        }
    ]
    return {"carousel_items": carousel_items}