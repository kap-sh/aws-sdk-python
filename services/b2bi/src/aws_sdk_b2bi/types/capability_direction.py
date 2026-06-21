"""Generated from Smithy shape ``com.amazonaws.b2bi#CapabilityDirection``."""

from typing import Literal, TypeAlias, cast

CapabilityDirection: TypeAlias = Literal[
    "INBOUND",
    "OUTBOUND",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CapabilityDirection) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CapabilityDirection:
    return cast(CapabilityDirection, data)
