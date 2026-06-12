"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#IntegerWithLengthBetween50And30000``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_apigatewayv2.errors import DeserializationError
from aws_sdk_apigatewayv2._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>An integer with a value between [50-30000].</p>"""
IntegerWithLengthBetween50And30000: TypeAlias = int
