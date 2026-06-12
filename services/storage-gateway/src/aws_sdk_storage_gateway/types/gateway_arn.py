"""Generated from Smithy shape ``com.amazonaws.storagegateway#GatewayARN``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_storage_gateway.errors import DeserializationError
from aws_sdk_storage_gateway._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The Amazon Resource Name (ARN) of the gateway. Use the <a>ListGateways</a> operation to return a list of gateways for your account and Amazon Web Services Region.</p>"""
GatewayARN: TypeAlias = str
