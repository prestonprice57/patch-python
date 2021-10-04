# coding: utf-8

"""
    Patch API V1

    The core API used to integrate with Patch's service  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: developers@usepatch.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from patch_api.configuration import Configuration


class Project(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "id": "str",
        "production": "bool",
        "name": "str",
        "description": "str",
        "type": "str",
        "mechanism": "str",
        "country": "str",
        "state": "str",
        "latitude": "float",
        "longitude": "float",
        "developer": "str",
        "photos": "list[Photo]",
        "average_price_per_tonne_cents_usd": "int",
        "remaining_mass_g": "int",
        "standard": "Standard",
        "sdgs": "list[Sdg]",
        "tagline": "str",
        "technology_type": "TechnologyType",
    }

    attribute_map = {
        "id": "id",
        "production": "production",
        "name": "name",
        "description": "description",
        "type": "type",
        "mechanism": "mechanism",
        "country": "country",
        "state": "state",
        "latitude": "latitude",
        "longitude": "longitude",
        "developer": "developer",
        "photos": "photos",
        "average_price_per_tonne_cents_usd": "average_price_per_tonne_cents_usd",
        "remaining_mass_g": "remaining_mass_g",
        "standard": "standard",
        "sdgs": "sdgs",
        "tagline": "tagline",
        "technology_type": "technology_type",
    }

    def __init__(
        self,
        id=None,
        production=None,
        name=None,
        description=None,
        type=None,
        mechanism=None,
        country=None,
        state=None,
        latitude=None,
        longitude=None,
        developer=None,
        photos=None,
        average_price_per_tonne_cents_usd=None,
        remaining_mass_g=None,
        standard=None,
        sdgs=None,
        tagline=None,
        technology_type=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """Project - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._production = None
        self._name = None
        self._description = None
        self._type = None
        self._mechanism = None
        self._country = None
        self._state = None
        self._latitude = None
        self._longitude = None
        self._developer = None
        self._photos = None
        self._average_price_per_tonne_cents_usd = None
        self._remaining_mass_g = None
        self._standard = None
        self._sdgs = None
        self._tagline = None
        self._technology_type = None
        self.discriminator = None

        self.id = id
        self.production = production
        self.name = name
        self.description = description
        if type is not None:
            self.type = type
        if mechanism is not None:
            self.mechanism = mechanism
        self.country = country
        self.state = state
        self.latitude = latitude
        self.longitude = longitude
        self.developer = developer
        self.photos = photos
        self.average_price_per_tonne_cents_usd = average_price_per_tonne_cents_usd
        self.remaining_mass_g = remaining_mass_g
        self.standard = standard
        self.sdgs = sdgs
        if tagline is not None:
            self.tagline = tagline
        self.technology_type = technology_type

    @property
    def id(self):
        """Gets the id of this Project.  # noqa: E501

        A unique uid for the record. UIDs will be prepended by pro_prod or pro_test depending on the mode it was created in.  # noqa: E501

        :return: The id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Project.

        A unique uid for the record. UIDs will be prepended by pro_prod or pro_test depending on the mode it was created in.  # noqa: E501

        :param id: The id of this Project.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and id is None
        ):  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def production(self):
        """Gets the production of this Project.  # noqa: E501

        A boolean indicating if this project is a production or test mode project.  # noqa: E501

        :return: The production of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._production

    @production.setter
    def production(self, production):
        """Sets the production of this Project.

        A boolean indicating if this project is a production or test mode project.  # noqa: E501

        :param production: The production of this Project.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation and production is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `production`, must not be `None`"
            )  # noqa: E501

        self._production = production

    @property
    def name(self):
        """Gets the name of this Project.  # noqa: E501

        The name of the project.  # noqa: E501

        :return: The name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project.

        The name of the project.  # noqa: E501

        :param name: The name of this Project.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and name is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Project.  # noqa: E501

        The description of the project.  # noqa: E501

        :return: The description of this Project.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Project.

        The description of the project.  # noqa: E501

        :param description: The description of this Project.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and description is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `description`, must not be `None`"
            )  # noqa: E501

        self._description = description

    @property
    def type(self):
        """Gets the type of this Project.  # noqa: E501

        Deprecated. Favor the technology_type field instead.  # noqa: E501

        :return: The type of this Project.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Project.

        Deprecated. Favor the technology_type field instead.  # noqa: E501

        :param type: The type of this Project.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def mechanism(self):
        """Gets the mechanism of this Project.  # noqa: E501

        The mechanism of the project. Either removal or avoidance.  # noqa: E501

        :return: The mechanism of this Project.  # noqa: E501
        :rtype: str
        """
        return self._mechanism

    @mechanism.setter
    def mechanism(self, mechanism):
        """Sets the mechanism of this Project.

        The mechanism of the project. Either removal or avoidance.  # noqa: E501

        :param mechanism: The mechanism of this Project.  # noqa: E501
        :type: str
        """
        allowed_values = ["removal", "avoidance"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and mechanism not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `mechanism` ({0}), must be one of {1}".format(  # noqa: E501
                    mechanism, allowed_values
                )
            )

        self._mechanism = mechanism

    @property
    def country(self):
        """Gets the country of this Project.  # noqa: E501

        The country of origin of the project.  # noqa: E501

        :return: The country of this Project.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Project.

        The country of origin of the project.  # noqa: E501

        :param country: The country of this Project.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and country is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `country`, must not be `None`"
            )  # noqa: E501

        self._country = country

    @property
    def state(self):
        """Gets the state of this Project.  # noqa: E501

        The state where this project is located.  # noqa: E501

        :return: The state of this Project.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Project.

        The state where this project is located.  # noqa: E501

        :param state: The state of this Project.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def latitude(self):
        """Gets the latitude of this Project.  # noqa: E501

        The latitude at which this project is located.  # noqa: E501

        :return: The latitude of this Project.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this Project.

        The latitude at which this project is located.  # noqa: E501

        :param latitude: The latitude of this Project.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this Project.  # noqa: E501

        The longitude at which this project is located.  # noqa: E501

        :return: The longitude of this Project.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this Project.

        The longitude at which this project is located.  # noqa: E501

        :param longitude: The longitude of this Project.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def developer(self):
        """Gets the developer of this Project.  # noqa: E501

        The name of the project developer.  # noqa: E501

        :return: The developer of this Project.  # noqa: E501
        :rtype: str
        """
        return self._developer

    @developer.setter
    def developer(self, developer):
        """Sets the developer of this Project.

        The name of the project developer.  # noqa: E501

        :param developer: The developer of this Project.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and developer is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `developer`, must not be `None`"
            )  # noqa: E501

        self._developer = developer

    @property
    def photos(self):
        """Gets the photos of this Project.  # noqa: E501

        An array of URLs for photos of the project.  # noqa: E501

        :return: The photos of this Project.  # noqa: E501
        :rtype: list[Photo]
        """
        return self._photos

    @photos.setter
    def photos(self, photos):
        """Sets the photos of this Project.

        An array of URLs for photos of the project.  # noqa: E501

        :param photos: The photos of this Project.  # noqa: E501
        :type: list[Photo]
        """

        self._photos = photos

    @property
    def average_price_per_tonne_cents_usd(self):
        """Gets the average_price_per_tonne_cents_usd of this Project.  # noqa: E501

        The average price per tonne in USD cents for carbon offsets supplied by this project.  # noqa: E501

        :return: The average_price_per_tonne_cents_usd of this Project.  # noqa: E501
        :rtype: int
        """
        return self._average_price_per_tonne_cents_usd

    @average_price_per_tonne_cents_usd.setter
    def average_price_per_tonne_cents_usd(self, average_price_per_tonne_cents_usd):
        """Sets the average_price_per_tonne_cents_usd of this Project.

        The average price per tonne in USD cents for carbon offsets supplied by this project.  # noqa: E501

        :param average_price_per_tonne_cents_usd: The average_price_per_tonne_cents_usd of this Project.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and average_price_per_tonne_cents_usd is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `average_price_per_tonne_cents_usd`, must not be `None`"
            )  # noqa: E501

        self._average_price_per_tonne_cents_usd = average_price_per_tonne_cents_usd

    @property
    def remaining_mass_g(self):
        """Gets the remaining_mass_g of this Project.  # noqa: E501

        The remaining mass in grams available for purchase for this project.  # noqa: E501

        :return: The remaining_mass_g of this Project.  # noqa: E501
        :rtype: int
        """
        return self._remaining_mass_g

    @remaining_mass_g.setter
    def remaining_mass_g(self, remaining_mass_g):
        """Sets the remaining_mass_g of this Project.

        The remaining mass in grams available for purchase for this project.  # noqa: E501

        :param remaining_mass_g: The remaining_mass_g of this Project.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and remaining_mass_g is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `remaining_mass_g`, must not be `None`"
            )  # noqa: E501

        self._remaining_mass_g = remaining_mass_g

    @property
    def standard(self):
        """Gets the standard of this Project.  # noqa: E501

        An object returning the Standard associated with this project.  # noqa: E501

        :return: The standard of this Project.  # noqa: E501
        :rtype: Standard
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        """Sets the standard of this Project.

        An object returning the Standard associated with this project.  # noqa: E501

        :param standard: The standard of this Project.  # noqa: E501
        :type: Standard
        """

        self._standard = standard

    @property
    def sdgs(self):
        """Gets the sdgs of this Project.  # noqa: E501

        An array returning the UN Sustainable Development Goals associated with this project.  # noqa: E501

        :return: The sdgs of this Project.  # noqa: E501
        :rtype: list[Sdg]
        """
        return self._sdgs

    @sdgs.setter
    def sdgs(self, sdgs):
        """Sets the sdgs of this Project.

        An array returning the UN Sustainable Development Goals associated with this project.  # noqa: E501

        :param sdgs: The sdgs of this Project.  # noqa: E501
        :type: list[Sdg]
        """

        self._sdgs = sdgs

    @property
    def tagline(self):
        """Gets the tagline of this Project.  # noqa: E501

        A short description of the project.  # noqa: E501

        :return: The tagline of this Project.  # noqa: E501
        :rtype: str
        """
        return self._tagline

    @tagline.setter
    def tagline(self, tagline):
        """Sets the tagline of this Project.

        A short description of the project.  # noqa: E501

        :param tagline: The tagline of this Project.  # noqa: E501
        :type: str
        """

        self._tagline = tagline

    @property
    def technology_type(self):
        """Gets the technology_type of this Project.  # noqa: E501


        :return: The technology_type of this Project.  # noqa: E501
        :rtype: TechnologyType
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """Sets the technology_type of this Project.


        :param technology_type: The technology_type of this Project.  # noqa: E501
        :type: TechnologyType
        """
        if (
            self.local_vars_configuration.client_side_validation
            and technology_type is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `technology_type`, must not be `None`"
            )  # noqa: E501

        self._technology_type = technology_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Project):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Project):
            return True

        return self.to_dict() != other.to_dict()
