"""Generated from Smithy shape ``com.amazonaws.fsx#VolumeFilterName``."""

from typing import Literal, TypeAlias, cast

VolumeFilterName: TypeAlias = Literal[
    "file-system-id",
    "storage-virtual-machine-id",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VolumeFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VolumeFilterName:
    return cast(VolumeFilterName, data)
