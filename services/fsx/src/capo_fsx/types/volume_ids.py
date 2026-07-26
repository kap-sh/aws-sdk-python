"""Generated from Smithy shape ``com.amazonaws.fsx#VolumeIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.volume_id

VolumeIds: TypeAlias = list["capo_fsx.types.volume_id.VolumeId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VolumeIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> VolumeIds:
    return list(data)
