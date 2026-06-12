"""Generated from Smithy shape ``com.amazonaws.lightsail#HttpProtocolIpv6``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

HttpProtocolIpv6: TypeAlias = Literal[
    "disabled",
    "enabled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "disabled",
        "enabled",
    )
)


def serialize_aws_json_1_1(value: HttpProtocolIpv6) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HttpProtocolIpv6:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HttpProtocolIpv6 value: {data!r}")
    return cast(HttpProtocolIpv6, data)
