"""Generated from Smithy shape ``com.amazonaws.ecs#TransportProtocol``."""

from typing import Literal, TypeAlias, cast

TransportProtocol: TypeAlias = Literal[
    "tcp",
    "udp",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransportProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TransportProtocol:
    return cast(TransportProtocol, data)
