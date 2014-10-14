# Copyright 2014 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from ebcli.core.abstractcontroller import AbstractBaseController
from ebcli.resources.strings import strings
from ebcli.core import operations, io


class UseController(AbstractBaseController):
    class Meta:
        label = 'use'
        description = strings['use.info']
        arguments = [
            (['environment_name'], dict(action='store', nargs=1,
                                        help='Environment name'))
        ]
        usage = 'eb use [environment_name]'

    def do_command(self):
        env_name = self.app.pargs.environment_name[0]

        operations.write_setting_to_current_branch('environment', env_name)