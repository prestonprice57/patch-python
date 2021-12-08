# coding: utf-8

"""
    Patch API V1

    The core API used to integrate with Patch's service  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: engineering@usepatch.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from patch_api.configuration import Configuration


class CreateVehicleEstimateRequest(object):
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
        "distance_m": "int",
        "make": "str",
        "model": "str",
        "year": "int",
        "project_id": "str",
        "create_order": "bool",
    }

    attribute_map = {
        "distance_m": "distance_m",
        "make": "make",
        "model": "model",
        "year": "year",
        "project_id": "project_id",
        "create_order": "create_order",
    }

    def __init__(
        self,
        distance_m=None,
        make=None,
        model=None,
        year=None,
        project_id=None,
        create_order=False,
        local_vars_configuration=None,
    ):  # noqa: E501
        """CreateVehicleEstimateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._distance_m = None
        self._make = None
        self._model = None
        self._year = None
        self._project_id = None
        self._create_order = None
        self.discriminator = None

        self.distance_m = distance_m
        self.make = make
        self.model = model
        self.year = year
        self.project_id = project_id
        self.create_order = create_order

    @property
    def distance_m(self):
        """Gets the distance_m of this CreateVehicleEstimateRequest.  # noqa: E501


        :return: The distance_m of this CreateVehicleEstimateRequest.  # noqa: E501
        :rtype: int
        """
        return self._distance_m

    @distance_m.setter
    def distance_m(self, distance_m):
        """Sets the distance_m of this CreateVehicleEstimateRequest.


        :param distance_m: The distance_m of this CreateVehicleEstimateRequest.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and distance_m is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `distance_m`, must not be `None`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and distance_m is not None
            and distance_m > 400000000
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `distance_m`, must be a value less than or equal to `400000000`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and distance_m is not None
            and distance_m < 0
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `distance_m`, must be a value greater than or equal to `0`"
            )  # noqa: E501

        self._distance_m = distance_m

    @property
    def make(self):
        """Gets the make of this CreateVehicleEstimateRequest.  # noqa: E501


        :return: The make of this CreateVehicleEstimateRequest.  # noqa: E501
        :rtype: str
        """
        return self._make

    @make.setter
    def make(self, make):
        """Sets the make of this CreateVehicleEstimateRequest.


        :param make: The make of this CreateVehicleEstimateRequest.  # noqa: E501
        :type: str
        """

        self._make = make

    @property
    def model(self):
        """Gets the model of this CreateVehicleEstimateRequest.  # noqa: E501


        :return: The model of this CreateVehicleEstimateRequest.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this CreateVehicleEstimateRequest.


        :param model: The model of this CreateVehicleEstimateRequest.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def year(self):
        """Gets the year of this CreateVehicleEstimateRequest.  # noqa: E501


        :return: The year of this CreateVehicleEstimateRequest.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this CreateVehicleEstimateRequest.


        :param year: The year of this CreateVehicleEstimateRequest.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and year is not None
            and year < 1900
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `year`, must be a value greater than or equal to `1900`"
            )  # noqa: E501

        self._year = year

    @property
    def project_id(self):
        """Gets the project_id of this CreateVehicleEstimateRequest.  # noqa: E501


        :return: The project_id of this CreateVehicleEstimateRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateVehicleEstimateRequest.


        :param project_id: The project_id of this CreateVehicleEstimateRequest.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def create_order(self):
        """Gets the create_order of this CreateVehicleEstimateRequest.  # noqa: E501


        :return: The create_order of this CreateVehicleEstimateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._create_order

    @create_order.setter
    def create_order(self, create_order):
        """Sets the create_order of this CreateVehicleEstimateRequest.


        :param create_order: The create_order of this CreateVehicleEstimateRequest.  # noqa: E501
        :type: bool
        """

        self._create_order = create_order

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
        if not isinstance(other, CreateVehicleEstimateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateVehicleEstimateRequest):
            return True

        return self.to_dict() != other.to_dict()
