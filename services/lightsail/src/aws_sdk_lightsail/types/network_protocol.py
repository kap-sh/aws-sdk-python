"""Generated from Smithy shape ``com.amazonaws.lightsail#NetworkProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

NetworkProtocol: TypeAlias = Literal[
    "tcp",
    "all",
    "udp",
    "icmp",
    "icmpv6",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "tcp",
        "all",
        "udp",
        "icmp",
        "icmpv6",
    )
)


def serialize_aws_json_1_1(value: NetworkProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NetworkProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetworkProtocol value: {data!r}")
    return cast(NetworkProtocol, data)
