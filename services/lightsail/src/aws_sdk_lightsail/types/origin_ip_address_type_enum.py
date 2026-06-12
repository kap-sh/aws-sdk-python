"""Generated from Smithy shape ``com.amazonaws.lightsail#OriginIpAddressTypeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

OriginIpAddressTypeEnum: TypeAlias = Literal[
    "ipv4",
    "ipv6",
    "dualstack",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ipv4",
        "ipv6",
        "dualstack",
    )
)


def serialize_aws_json_1_1(value: OriginIpAddressTypeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OriginIpAddressTypeEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OriginIpAddressTypeEnum value: {data!r}")
    return cast(OriginIpAddressTypeEnum, data)
