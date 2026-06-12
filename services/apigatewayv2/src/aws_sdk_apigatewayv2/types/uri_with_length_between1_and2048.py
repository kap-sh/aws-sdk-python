"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#UriWithLengthBetween1And2048``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_apigatewayv2.errors import DeserializationError
from aws_sdk_apigatewayv2._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>A string representation of a URI with a length between [1-2048].</p>"""
UriWithLengthBetween1And2048: TypeAlias = str
