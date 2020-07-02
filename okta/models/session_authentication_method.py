"""
Copyright 2020 - Present Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# AUTO-GENERATED! DO NOT EDIT FILE DIRECTLY
# SEE CONTRIBUTOR DOCUMENTATION

from enum import Enum


class SessionAuthenticationMethod(
    str,
    Enum
):
    pwd = "pwd"
    swk = "swk"
    hwk = "hwk"
    otp = "otp"
    sms = "sms"
    tel = "tel"
    geo = "geo"
    fpt = "fpt"
    kba = "kba"
    mfa = "mfa"

# End of File Generation
