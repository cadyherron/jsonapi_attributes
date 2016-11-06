from marshmallow_jsonapi import Schema, fields
from marshmallow import pre_dump, post_load


class PuppySchema(Schema):
    """
    This schema converts our nested database attributes into flat JSONAPI attributes, and vice versa.
    Database attributes: id, description, birthday
    JSONAPI attributes: name, breed, gender (these all get saved to 'description' in the db)
    """
    id = fields.Int()
    # the "load_only" flag means this value will be skipped during serialization:
    description = fields.Dict(load_only=True)
    name = fields.Str()
    breed = fields.Str()
    gender = fields.Str()
    birthday = fields.DateTime()

    @post_load
    def combine_fields_into_description(self, attributes):
        """
        This function is run after deserialization. It combines the incoming "attributes" into the
        nested description property.
        :param attributes: deserialized dictionary
        :return: dictionary where the key is "description", and the value is the dictionary of attributes
        """
        return {'config': attributes}

    @pre_dump
    def flatten_description(self, puppy):
        """
        This function is run before serialization. It flattens the "description" property into the
        attributes listed in PuppySchema.
        :param kiosk: the original object
        :return: the processed object to be serialized
        """
        if puppy.config:
            puppy.name = puppy.config.get('name')
            puppy.breed = puppy.config.get('breed')
            puppy.gender = puppy.config.get('gender')
        return kiosk

    class Meta:
        type_ = "puppies"
        strict = True

puppy_schema = PuppySchema()
puppies_schema = PuppySchema(many=True)