"""Generated from Smithy shape ``com.amazonaws.fsx#RestoreOpenZFSVolumeOption``."""

from typing import Literal, TypeAlias, cast

RestoreOpenZFSVolumeOption: TypeAlias = Literal[
    "DELETE_INTERMEDIATE_SNAPSHOTS",
    "DELETE_CLONED_VOLUMES",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestoreOpenZFSVolumeOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RestoreOpenZFSVolumeOption:
    return cast(RestoreOpenZFSVolumeOption, data)
