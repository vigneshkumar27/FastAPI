todo_collection = [
    {
        "id":"1",
        "title":"Go to Gym",
        "action":"Everyevening 7 - 8 go to GYM"
    },
        {
        "id":"2",
        "title":"Go to Gym",
        "action":"Everyevening 7 - 8 go to GYM"
    },
            {
        "id":"5",
        "title":"Go to Gym",
        "action":"Everyevening 7 - 8 go to GYM"
    }
        
]

search_item =     {
        "id":"5",
        "title":"Go to Gym",
        "action":"Everyevening 7 - 8 go to GYM"
    }

        
        
print([item for item in filter(lambda item : item['id'] != search_item['id'],todo_collection)])