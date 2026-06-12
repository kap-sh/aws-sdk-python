"""Generated from Smithy shape ``com.amazonaws.lightsail#IpAddressType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

IpAddressType: TypeAlias = Literal[
    "dualstack",
    "ipv4",
    "ipv6",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "dualstack",
        "ipv4",
        "ipv6",
    )
)


def serialize_aws_json_1_1(value: IpAddressType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IpAddressType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IpAddressType value: {data!r}")
    return cast(IpAddressType, data)
