"""Generated from Smithy shape ``com.amazonaws.fsx#VolumeType``."""

from typing import Literal, TypeAlias, cast

VolumeType: TypeAlias = Literal[
    "ONTAP",
    "OPENZFS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VolumeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VolumeType:
    return cast(VolumeType, data)
