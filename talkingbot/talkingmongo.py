#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Module for MongoDB """

from pymongo import collection


class TalkingMongo(object):

    """Class for manage state in mongodb collections"""

    def __init__(self, db_collection, _id_name="_id",
                 last_command_array_name="last_commands",
                 params_name="params"):
        super(TalkingMongo, self).__init__()

        # if(isinstance(db_collection, collection.Collection)):
        #     self.collecion = db_collection
        # else:
        #     raise Exception("La coleccion no es coleccion flaco, que te pasa?")

        self._id_name = _id_name
        self.last_command_array_name = last_command_array_name
        self.params_name = params_name

    def get_current_action(self, id_user):
        return {"name": "/cuando", "params": {"bus": 141}}

    def save_update_action(self, id_user, action_name, params):
        pass

    def clear_action(self, id_user):
        pass

    def empty_params_action(self, id_user, array_to_search, only_first=True):
        command = self.get_current_action(id_user)
        if command:
            empty_params = []
            valid = True
            for key in array_to_search:
                if key not in command[self.params_name]:
                    empty_params.append(key)
                    if only_first:
                        return empty_params
                    else:
                        valid = False
            if valid:
                return None
            return empty_params
        else:
            return None


# re = TalkingMongo("db_collection")
# valid = re.empty_params_action(1, ["bus", "first", "second"])
# print valid
