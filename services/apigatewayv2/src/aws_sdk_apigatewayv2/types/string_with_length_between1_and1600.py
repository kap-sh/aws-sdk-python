"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#StringWithLengthBetween1And1600``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_apigatewayv2.errors import DeserializationError
from aws_sdk_apigatewayv2._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>A string with a length between [0-1600].</p>"""
StringWithLengthBetween1And1600: TypeAlias = str
