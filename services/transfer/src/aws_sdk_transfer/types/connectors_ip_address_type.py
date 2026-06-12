"""Generated from Smithy shape ``com.amazonaws.transfer#ConnectorsIpAddressType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

ConnectorsIpAddressType: TypeAlias = Literal[
    "IPV4",
    "DUALSTACK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IPV4",
        "DUALSTACK",
    )
)


def serialize_aws_json_1_1(value: ConnectorsIpAddressType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectorsIpAddressType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectorsIpAddressType value: {data!r}")
    return cast(ConnectorsIpAddressType, data)
