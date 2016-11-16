# puppy_attributes

#### What is this?

This is an example repo for Flask and Marshmallow-JSONAPI. It shows how you can combine an object's
flat attributes into a nested property before persisting that object to the database. You can then flatten the
nested attributes before returning the response.


Python object:

puppy = {
    "description": {
        "name": "Spot",
        "breed": "dalmation",
        "gender": "male"
    },
    "birthday": "2016-02-16T00:05:34"
}


Database columns:
    id
    description
    birthday


JSONAPI response:

{"data": {
    "attributes": {
        "name": "Spot",
        "breed": "dalmation",
        "gender": "male",
        "birthday": "2016-02-16T00:05:34"
    },
    "id": "12",
    "type": "puppies"
 }
}


#### How to run locally:

1. Clone this repo
2. `cd` into it
3. `virtualenv venv`
4. `source venv/bin/activate`
5. `pip install -r requirements.txt`
6. `python application.py`