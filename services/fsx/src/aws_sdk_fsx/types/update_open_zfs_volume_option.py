"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateOpenZFSVolumeOption``."""

from typing import Literal, TypeAlias, cast

UpdateOpenZFSVolumeOption: TypeAlias = Literal[
    "DELETE_INTERMEDIATE_SNAPSHOTS",
    "DELETE_CLONED_VOLUMES",
    "DELETE_INTERMEDIATE_DATA",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateOpenZFSVolumeOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UpdateOpenZFSVolumeOption:
    return cast(UpdateOpenZFSVolumeOption, data)
