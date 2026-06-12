"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#AuthorizerType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_apigatewayv2.errors import DeserializationError
from aws_sdk_apigatewayv2._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The authorizer type. Specify REQUEST for a Lambda function using incoming request parameters. Specify JWT to use JSON Web Tokens (supported only for HTTP APIs).</p>"""
AuthorizerType: TypeAlias = Literal[
    "REQUEST",
    "JWT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUEST",
        "JWT",
    )
)


def serialize_json(value: AuthorizerType) -> str:
    return value


def deserialize_json(data: str) -> AuthorizerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthorizerType value: {data!r}")
    return cast(AuthorizerType, data)
