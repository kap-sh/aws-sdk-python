"""Generated from Smithy shape ``com.amazonaws.fsx#VolumeFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.volume_filter_value

VolumeFilterValues: TypeAlias = list[
    "capo_fsx.types.volume_filter_value.VolumeFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VolumeFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> VolumeFilterValues:
    return list(data)
