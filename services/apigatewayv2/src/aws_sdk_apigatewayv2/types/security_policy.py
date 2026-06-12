"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#SecurityPolicy``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_apigatewayv2.errors import DeserializationError
from aws_sdk_apigatewayv2._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The Transport Layer Security (TLS) version of the security policy for this domain name. The valid values are TLS_1_0 and TLS_1_2.</p>"""
SecurityPolicy: TypeAlias = Literal[
    "TLS_1_0",
    "TLS_1_2",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TLS_1_0",
        "TLS_1_2",
    )
)


def serialize_json(value: SecurityPolicy) -> str:
    return value


def deserialize_json(data: str) -> SecurityPolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SecurityPolicy value: {data!r}")
    return cast(SecurityPolicy, data)
