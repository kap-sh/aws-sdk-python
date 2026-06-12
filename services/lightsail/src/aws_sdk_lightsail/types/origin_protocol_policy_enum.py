"""Generated from Smithy shape ``com.amazonaws.lightsail#OriginProtocolPolicyEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

OriginProtocolPolicyEnum: TypeAlias = Literal[
    "http-only",
    "https-only",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "http-only",
        "https-only",
    )
)


def serialize_aws_json_1_1(value: OriginProtocolPolicyEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OriginProtocolPolicyEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OriginProtocolPolicyEnum value: {data!r}")
    return cast(OriginProtocolPolicyEnum, data)
