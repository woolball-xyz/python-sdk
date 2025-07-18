# coding: utf-8

"""
    Woolball AI Network API

    **Transform idle browsers into a powerful distributed AI inference network**  For detailed examples and model lists, visit our [GitHub repository](https://github.com/woolball-xyz/woolball-server).  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TranslationRequestContract(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'model': 'str',
        'dtype': 'str',
        'input': 'str',
        'src_lang': 'str',
        'tgt_lang': 'str'
    }

    attribute_map = {
        'model': 'model',
        'dtype': 'dtype',
        'input': 'input',
        'src_lang': 'srcLang',
        'tgt_lang': 'tgtLang'
    }

    def __init__(self, model=None, dtype=None, input=None, src_lang=None, tgt_lang=None):  # noqa: E501
        """TranslationRequestContract - a model defined in Swagger"""  # noqa: E501
        self._model = None
        self._dtype = None
        self._input = None
        self._src_lang = None
        self._tgt_lang = None
        self.discriminator = None
        self.model = model
        self.dtype = dtype
        self.input = input
        self.src_lang = src_lang
        self.tgt_lang = tgt_lang

    @property
    def model(self):
        """Gets the model of this TranslationRequestContract.  # noqa: E501


        :return: The model of this TranslationRequestContract.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this TranslationRequestContract.


        :param model: The model of this TranslationRequestContract.  # noqa: E501
        :type: str
        """
        if model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def dtype(self):
        """Gets the dtype of this TranslationRequestContract.  # noqa: E501


        :return: The dtype of this TranslationRequestContract.  # noqa: E501
        :rtype: str
        """
        return self._dtype

    @dtype.setter
    def dtype(self, dtype):
        """Sets the dtype of this TranslationRequestContract.


        :param dtype: The dtype of this TranslationRequestContract.  # noqa: E501
        :type: str
        """
        if dtype is None:
            raise ValueError("Invalid value for `dtype`, must not be `None`")  # noqa: E501

        self._dtype = dtype

    @property
    def input(self):
        """Gets the input of this TranslationRequestContract.  # noqa: E501


        :return: The input of this TranslationRequestContract.  # noqa: E501
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this TranslationRequestContract.


        :param input: The input of this TranslationRequestContract.  # noqa: E501
        :type: str
        """
        if input is None:
            raise ValueError("Invalid value for `input`, must not be `None`")  # noqa: E501

        self._input = input

    @property
    def src_lang(self):
        """Gets the src_lang of this TranslationRequestContract.  # noqa: E501


        :return: The src_lang of this TranslationRequestContract.  # noqa: E501
        :rtype: str
        """
        return self._src_lang

    @src_lang.setter
    def src_lang(self, src_lang):
        """Sets the src_lang of this TranslationRequestContract.


        :param src_lang: The src_lang of this TranslationRequestContract.  # noqa: E501
        :type: str
        """
        if src_lang is None:
            raise ValueError("Invalid value for `src_lang`, must not be `None`")  # noqa: E501

        self._src_lang = src_lang

    @property
    def tgt_lang(self):
        """Gets the tgt_lang of this TranslationRequestContract.  # noqa: E501


        :return: The tgt_lang of this TranslationRequestContract.  # noqa: E501
        :rtype: str
        """
        return self._tgt_lang

    @tgt_lang.setter
    def tgt_lang(self, tgt_lang):
        """Sets the tgt_lang of this TranslationRequestContract.


        :param tgt_lang: The tgt_lang of this TranslationRequestContract.  # noqa: E501
        :type: str
        """
        if tgt_lang is None:
            raise ValueError("Invalid value for `tgt_lang`, must not be `None`")  # noqa: E501

        self._tgt_lang = tgt_lang

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TranslationRequestContract, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TranslationRequestContract):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
