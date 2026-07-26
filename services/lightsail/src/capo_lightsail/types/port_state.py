"""Generated from Smithy shape ``com.amazonaws.lightsail#PortState``."""

from typing import Literal, TypeAlias, cast

PortState: TypeAlias = Literal[
    "open",
    "closed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PortState:
    return cast(PortState, data)
