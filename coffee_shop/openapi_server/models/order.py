# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.item import Item
from openapi_server import util

from openapi_server.models.item import Item  # noqa: E501

class Order(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, order_items=None, created_timestamp=None, status=None, customer_name=None, discount=None):  # noqa: E501
        """Order - a model defined in OpenAPI

        :param id: The id of this Order.  # noqa: E501
        :type id: int
        :param order_items: The order_items of this Order.  # noqa: E501
        :type order_items: List[Item]
        :param created_timestamp: The created_timestamp of this Order.  # noqa: E501
        :type created_timestamp: datetime
        :param status: The status of this Order.  # noqa: E501
        :type status: str
        :param customer_name: The customer_name of this Order.  # noqa: E501
        :type customer_name: str
        :param discount: The discount of this Order.  # noqa: E501
        :type discount: float
        """
        self.openapi_types = {
            'id': int,
            'order_items': List[Item],
            'created_timestamp': datetime,
            'status': str,
            'customer_name': str,
            'discount': float
        }

        self.attribute_map = {
            'id': 'id',
            'order_items': 'orderItems',
            'created_timestamp': 'createdTimestamp',
            'status': 'status',
            'customer_name': 'customerName',
            'discount': 'discount'
        }

        self._id = id
        self._order_items = order_items
        self._created_timestamp = created_timestamp
        self._status = status
        self._customer_name = customer_name
        self._discount = discount

    @classmethod
    def from_dict(cls, dikt) -> 'Order':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Order of this Order.  # noqa: E501
        :rtype: Order
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Order.


        :return: The id of this Order.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Order.


        :param id: The id of this Order.
        :type id: int
        """

        self._id = id

    @property
    def order_items(self):
        """Gets the order_items of this Order.


        :return: The order_items of this Order.
        :rtype: List[Item]
        """
        return self._order_items

    @order_items.setter
    def order_items(self, order_items):
        """Sets the order_items of this Order.


        :param order_items: The order_items of this Order.
        :type order_items: List[Item]
        """

        self._order_items = order_items

    @property
    def created_timestamp(self):
        """Gets the created_timestamp of this Order.


        :return: The created_timestamp of this Order.
        :rtype: datetime
        """
        return self._created_timestamp

    @created_timestamp.setter
    def created_timestamp(self, created_timestamp):
        """Sets the created_timestamp of this Order.


        :param created_timestamp: The created_timestamp of this Order.
        :type created_timestamp: datetime
        """

        self._created_timestamp = created_timestamp

    @property
    def status(self):
        """Gets the status of this Order.

        Order Status  # noqa: E501

        :return: The status of this Order.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Order.

        Order Status  # noqa: E501

        :param status: The status of this Order.
        :type status: str
        """
        allowed_values = ["placed", "delivered"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def customer_name(self):
        """Gets the customer_name of this Order.

        The name of the customer ordering  # noqa: E501

        :return: The customer_name of this Order.
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        """Sets the customer_name of this Order.

        The name of the customer ordering  # noqa: E501

        :param customer_name: The customer_name of this Order.
        :type customer_name: str
        """

        self._customer_name = customer_name

    @property
    def discount(self):
        """Gets the discount of this Order.


        :return: The discount of this Order.
        :rtype: float
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this Order.


        :param discount: The discount of this Order.
        :type discount: float
        """

        self._discount = discount
