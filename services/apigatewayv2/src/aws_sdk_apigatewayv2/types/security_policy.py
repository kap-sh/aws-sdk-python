"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#SecurityPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apigatewayv2.errors import DeserializationError

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
