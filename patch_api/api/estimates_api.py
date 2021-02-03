# coding: utf-8

"""
    Patch API V1

    The core API used to integrate with Patch's service  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: developers@usepatch.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from patch_api.exceptions import ApiTypeError, ApiValueError


class EstimatesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    ALLOWED_QUERY_PARAMS = ["mass_g", "price_cents_usd", "project_id", "page"]

    def __init__(self, api_client=None):
        self.api_client = api_client

    def create_mass_estimate(
        self, create_mass_estimate_request={}, **kwargs
    ):  # noqa: E501
        """Create an estimate based on mass of CO2  # noqa: E501

        Creates an estimate for the mass of CO2 to be compensated. An order in the `draft` state will also be created, linked to the estimate.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_mass_estimate(create_mass_estimate_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreateMassEstimateRequest create_mass_estimate_request: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: EstimateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.create_mass_estimate_with_http_info(
            create_mass_estimate_request, **kwargs
        )  # noqa: E501

    def create_mass_estimate_with_http_info(
        self, create_mass_estimate_request, **kwargs
    ):  # noqa: E501
        """Create an estimate based on mass of CO2  # noqa: E501

        Creates an estimate for the mass of CO2 to be compensated. An order in the `draft` state will also be created, linked to the estimate.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_mass_estimate_with_http_info(create_mass_estimate_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreateMassEstimateRequest create_mass_estimate_request: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(EstimateResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["create_mass_estimate_request"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")
        all_params.append("mass_g")
        all_params.append("price_cents_usd")
        all_params.append("project_id")
        all_params.append("metadata")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_mass_estimate" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'create_mass_estimate_request' is set
        if (
            "create_mass_estimate_request" not in local_var_params
            or local_var_params["create_mass_estimate_request"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `create_mass_estimate_request` when calling `create_mass_estimate`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        for key in kwargs:
            query_params.append([key, kwargs.get(key)])

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "create_mass_estimate_request" in local_var_params:
            body_params = local_var_params["create_mass_estimate_request"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearer_auth"]  # noqa: E501

        return self.api_client.call_api(
            "/v1/estimates/mass",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="EstimateResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def retrieve_estimate(self, id={}, **kwargs):  # noqa: E501
        """Retrieves an estimate  # noqa: E501

        Retrieves a given estimate and its associated order. You can only retrieve estimates associated with the organization you are querying for.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_estimate(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: EstimateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.retrieve_estimate_with_http_info(id, **kwargs)  # noqa: E501

    def retrieve_estimate_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieves an estimate  # noqa: E501

        Retrieves a given estimate and its associated order. You can only retrieve estimates associated with the organization you are querying for.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_estimate_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(EstimateResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")
        all_params.append("mass_g")
        all_params.append("price_cents_usd")
        all_params.append("project_id")
        all_params.append("metadata")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_estimate" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in local_var_params or local_var_params["id"] is None:
            raise ApiValueError(
                "Missing the required parameter `id` when calling `retrieve_estimate`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in local_var_params:
            path_params["id"] = local_var_params["id"]  # noqa: E501

        query_params = []
        for key in kwargs:
            query_params.append([key, kwargs.get(key)])

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearer_auth"]  # noqa: E501

        return self.api_client.call_api(
            "/v1/estimates/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="EstimateResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def retrieve_estimates(self, **kwargs):  # noqa: E501
        """Retrieves a list of estimates  # noqa: E501

        Retrieves a list of estimates and their associated orders. You can only retrieve estimates associated with the organization you are querying for.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_estimates(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int page:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: EstimateListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.retrieve_estimates_with_http_info(**kwargs)  # noqa: E501

    def retrieve_estimates_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves a list of estimates  # noqa: E501

        Retrieves a list of estimates and their associated orders. You can only retrieve estimates associated with the organization you are querying for.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_estimates_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int page:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(EstimateListResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["page"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")
        all_params.append("mass_g")
        all_params.append("price_cents_usd")
        all_params.append("project_id")
        all_params.append("metadata")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_estimates" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        for key in kwargs:
            query_params.append([key, kwargs.get(key)])
        if "page" in local_var_params:
            query_params.append(("page", local_var_params["page"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearer_auth"]  # noqa: E501

        return self.api_client.call_api(
            "/v1/estimates",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="EstimateListResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )