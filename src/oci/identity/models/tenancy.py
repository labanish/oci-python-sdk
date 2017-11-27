# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Tenancy(object):

    def __init__(self, **kwargs):
        """
        Initializes a new Tenancy object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Tenancy.
        :type id: str

        :param name:
            The value to assign to the name property of this Tenancy.
        :type name: str

        :param description:
            The value to assign to the description property of this Tenancy.
        :type description: str

        :param home_region_key:
            The value to assign to the home_region_key property of this Tenancy.
        :type home_region_key: str

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'home_region_key': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'home_region_key': 'homeRegionKey'
        }

        self._id = None
        self._name = None
        self._description = None
        self._home_region_key = None

    @property
    def id(self):
        """
        Gets the id of this Tenancy.
        The OCID of the tenancy.


        :return: The id of this Tenancy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Tenancy.
        The OCID of the tenancy.


        :param id: The id of this Tenancy.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Tenancy.
        The name of the tenancy.


        :return: The name of this Tenancy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Tenancy.
        The name of the tenancy.


        :param name: The name of this Tenancy.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Tenancy.
        The description of the tenancy.


        :return: The description of this Tenancy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Tenancy.
        The description of the tenancy.


        :param description: The description of this Tenancy.
        :type: str
        """
        self._description = description

    @property
    def home_region_key(self):
        """
        Gets the home_region_key of this Tenancy.
        The region key for the tenancy's home region.

        Allowed values are:
        - `IAD`
        - `PHX`
        - `FRA`


        :return: The home_region_key of this Tenancy.
        :rtype: str
        """
        return self._home_region_key

    @home_region_key.setter
    def home_region_key(self, home_region_key):
        """
        Sets the home_region_key of this Tenancy.
        The region key for the tenancy's home region.

        Allowed values are:
        - `IAD`
        - `PHX`
        - `FRA`


        :param home_region_key: The home_region_key of this Tenancy.
        :type: str
        """
        self._home_region_key = home_region_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
