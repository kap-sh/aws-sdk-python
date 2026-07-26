"""Generated from Smithy shape ``com.amazonaws.fsx#VolumeStyle``."""

from typing import Literal, TypeAlias, cast

VolumeStyle: TypeAlias = Literal[
    "FLEXVOL",
    "FLEXGROUP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VolumeStyle) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VolumeStyle:
    return cast(VolumeStyle, data)
