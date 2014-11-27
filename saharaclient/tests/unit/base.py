# Copyright (c) 2014 Mirantis Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import six
import testtools

from saharaclient.api import client


class BaseTestCase(testtools.TestCase):
    client = client.Client(sahara_url='http://localhost:8386',
                           input_auth_token='token')

    def assertFields(self, body, obj):
        for key, value in six.iteritems(body):
            self.assertEqual(value, getattr(obj, key))


class FakeResponse(object):
    def __init__(self, status_code, content=None, response_key=None):
        self.status_code = status_code
        self.content = content or {}
        self.response_key = response_key
        self.name = 'name'

    def json(self):
        if self.response_key:
            return {self.response_key: self.content}
        else:
            return self.content
