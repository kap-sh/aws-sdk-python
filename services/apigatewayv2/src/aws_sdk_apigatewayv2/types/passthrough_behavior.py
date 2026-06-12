"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#PassthroughBehavior``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_apigatewayv2.errors import DeserializationError
from aws_sdk_apigatewayv2._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>Represents passthrough behavior for an integration response. Supported only for WebSocket APIs.</p>"""
PassthroughBehavior: TypeAlias = Literal[
    "WHEN_NO_MATCH",
    "NEVER",
    "WHEN_NO_TEMPLATES",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WHEN_NO_MATCH",
        "NEVER",
        "WHEN_NO_TEMPLATES",
    )
)


def serialize_json(value: PassthroughBehavior) -> str:
    return value


def deserialize_json(data: str) -> PassthroughBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PassthroughBehavior value: {data!r}")
    return cast(PassthroughBehavior, data)
