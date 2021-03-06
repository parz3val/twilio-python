# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class FunctionVersionTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.serverless.v1.services("ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .functions("ZHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .function_versions.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://serverless.twilio.com/v1/Services/ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Functions/ZHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Versions',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "function_versions": [],
                "meta": {
                    "first_page_url": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Functions/ZH00000000000000000000000000000000/Versions?PageSize=50&Page=0",
                    "key": "function_versions",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Functions/ZH00000000000000000000000000000000/Versions?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.serverless.v1.services("ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .functions("ZHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .function_versions.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.serverless.v1.services("ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .functions("ZHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .function_versions("ZNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://serverless.twilio.com/v1/Services/ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Functions/ZHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Versions/ZNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "ZN00000000000000000000000000000000",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ZS00000000000000000000000000000000",
                "function_sid": "ZH00000000000000000000000000000000",
                "path": "/test-path",
                "visibility": "public",
                "date_created": "2018-11-10T20:00:00Z",
                "url": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Functions/ZH00000000000000000000000000000000/Versions/ZN00000000000000000000000000000000",
                "links": {
                    "function_version_content": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Functions/ZH00000000000000000000000000000000/Versions/ZN00000000000000000000000000000000/Content"
                }
            }
            '''
        ))

        actual = self.client.serverless.v1.services("ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .functions("ZHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .function_versions("ZNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)
