"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#IntegrationType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_apigatewayv2.errors import DeserializationError
from aws_sdk_apigatewayv2._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>Represents an API method integration type.</p>"""
IntegrationType: TypeAlias = Literal[
    "AWS",
    "HTTP",
    "MOCK",
    "HTTP_PROXY",
    "AWS_PROXY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS",
        "HTTP",
        "MOCK",
        "HTTP_PROXY",
        "AWS_PROXY",
    )
)


def serialize_json(value: IntegrationType) -> str:
    return value


def deserialize_json(data: str) -> IntegrationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IntegrationType value: {data!r}")
    return cast(IntegrationType, data)
