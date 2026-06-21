"""Generated from Smithy shape ``com.amazonaws.lightsail#PortAccessType``."""

from typing import Literal, TypeAlias, cast

PortAccessType: TypeAlias = Literal[
    "Public",
    "Private",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortAccessType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PortAccessType:
    return cast(PortAccessType, data)
