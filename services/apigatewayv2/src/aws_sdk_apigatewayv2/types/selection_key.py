"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#SelectionKey``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_apigatewayv2.errors import DeserializationError
from aws_sdk_apigatewayv2._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>After evaluating a selection expression, the result is compared against one or more selection keys to find a matching key. See <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions\">Selection Expressions</a> for a list of expressions and each expression's associated selection key type.</p>"""
SelectionKey: TypeAlias = str
