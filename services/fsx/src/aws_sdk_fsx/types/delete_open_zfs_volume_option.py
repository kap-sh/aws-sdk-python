"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteOpenZFSVolumeOption``."""

from typing import Literal, TypeAlias, cast

DeleteOpenZFSVolumeOption: TypeAlias = Literal["DELETE_CHILD_VOLUMES_AND_SNAPSHOTS",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteOpenZFSVolumeOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeleteOpenZFSVolumeOption:
    return cast(DeleteOpenZFSVolumeOption, data)
