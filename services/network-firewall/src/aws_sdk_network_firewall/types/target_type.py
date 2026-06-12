"""Generated from Smithy shape ``com.amazonaws.networkfirewall#TargetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

TargetType: TypeAlias = Literal[
    "TLS_SNI",
    "HTTP_HOST",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TLS_SNI",
        "HTTP_HOST",
    )
)


def serialize_aws_json_1_0(value: TargetType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TargetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetType value: {data!r}")
    return cast(TargetType, data)
