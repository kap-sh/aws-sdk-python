"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#IpAddressType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apigatewayv2.errors import DeserializationError

"""<p>The IP address types that can invoke your API or domain name.</p>"""
IpAddressType: TypeAlias = Literal[
    "ipv4",
    "dualstack",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ipv4",
        "dualstack",
    )
)


def serialize_json(value: IpAddressType) -> str:
    return value


def deserialize_json(data: str) -> IpAddressType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IpAddressType value: {data!r}")
    return cast(IpAddressType, data)
