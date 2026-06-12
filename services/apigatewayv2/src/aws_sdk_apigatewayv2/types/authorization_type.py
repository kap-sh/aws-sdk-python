"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#AuthorizationType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_apigatewayv2.errors import DeserializationError
from aws_sdk_apigatewayv2._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The authorization type. For WebSocket APIs, valid values are NONE for open access, AWS_IAM for using AWS IAM permissions, and CUSTOM for using a Lambda authorizer. For HTTP APIs, valid values are NONE for open access, JWT for using JSON Web Tokens, AWS_IAM for using AWS IAM permissions, and CUSTOM for using a Lambda authorizer.</p>"""
AuthorizationType: TypeAlias = Literal[
    "NONE",
    "AWS_IAM",
    "CUSTOM",
    "JWT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "AWS_IAM",
        "CUSTOM",
        "JWT",
    )
)


def serialize_json(value: AuthorizationType) -> str:
    return value


def deserialize_json(data: str) -> AuthorizationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthorizationType value: {data!r}")
    return cast(AuthorizationType, data)
