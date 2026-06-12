"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#TryItState``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_apigatewayv2.errors import DeserializationError
from aws_sdk_apigatewayv2._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>Represents the try it state for a product REST endpoint page.</p>"""
TryItState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: TryItState) -> str:
    return value


def deserialize_json(data: str) -> TryItState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TryItState value: {data!r}")
    return cast(TryItState, data)
