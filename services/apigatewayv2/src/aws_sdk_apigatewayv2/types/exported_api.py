"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ExportedApi``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_apigatewayv2.errors import DeserializationError
from aws_sdk_apigatewayv2._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>Represents an exported definition of an API in a particular output format, for example, YAML. The API is serialized to the requested specification, for example, OpenAPI 3.0.</p>"""
ExportedApi: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: ExportedApi) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> ExportedApi:
    return base64.b64decode(data)
