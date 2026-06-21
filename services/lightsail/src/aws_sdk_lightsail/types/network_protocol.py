"""Generated from Smithy shape ``com.amazonaws.lightsail#NetworkProtocol``."""

from typing import Literal, TypeAlias, cast

NetworkProtocol: TypeAlias = Literal[
    "tcp",
    "all",
    "udp",
    "icmp",
    "icmpv6",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NetworkProtocol:
    return cast(NetworkProtocol, data)
