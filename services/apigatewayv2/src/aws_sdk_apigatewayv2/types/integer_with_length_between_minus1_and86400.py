"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#IntegerWithLengthBetweenMinus1And86400``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_apigatewayv2.errors import DeserializationError
from aws_sdk_apigatewayv2._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>An integer with a value between -1 and 86400. Supported only for HTTP APIs.</p>"""
IntegerWithLengthBetweenMinus1And86400: TypeAlias = int
