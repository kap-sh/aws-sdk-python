"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#EndpointType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_apigatewayv2.errors import DeserializationError
from aws_sdk_apigatewayv2._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>Represents an endpoint type.</p>"""
EndpointType: TypeAlias = Literal[
    "REGIONAL",
    "EDGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REGIONAL",
        "EDGE",
    )
)


def serialize_json(value: EndpointType) -> str:
    return value


def deserialize_json(data: str) -> EndpointType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndpointType value: {data!r}")
    return cast(EndpointType, data)
