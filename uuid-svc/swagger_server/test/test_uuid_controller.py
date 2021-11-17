# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.uuid import Uuid  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUuidController(BaseTestCase):
    """UuidController integration test stubs"""

    def test_generate_uuid(self):
        """Test case for generate_uuid

        Request the generation and allocation of a UUID
        """
        response = self.client.open(
            '//uuid',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_uuid(self):
        """Test case for get_uuid

        Determine if a provided UUID has been allocated and is valid
        """
        response = self.client.open(
            '//uuid/{uuidstr}'.format(uuidstr='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
