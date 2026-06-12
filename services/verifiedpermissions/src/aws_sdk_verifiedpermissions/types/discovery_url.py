"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#DiscoveryUrl``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_verifiedpermissions.errors import DeserializationError
from aws_sdk_verifiedpermissions._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

DiscoveryUrl: TypeAlias = str