"""Generated from Smithy shape ``com.amazonaws.networkfirewall#IPAddressType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

IPAddressType: TypeAlias = Literal[
    "DUALSTACK",
    "IPV4",
    "IPV6",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DUALSTACK",
        "IPV4",
        "IPV6",
    )
)


def serialize_aws_json_1_0(value: IPAddressType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IPAddressType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IPAddressType value: {data!r}")
    return cast(IPAddressType, data)
