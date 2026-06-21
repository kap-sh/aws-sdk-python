"""Generated from Smithy shape ``com.amazonaws.lightsail#PortInfoSourceType``."""

from typing import Literal, TypeAlias, cast

PortInfoSourceType: TypeAlias = Literal[
    "DEFAULT",
    "INSTANCE",
    "NONE",
    "CLOSED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortInfoSourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PortInfoSourceType:
    return cast(PortInfoSourceType, data)
