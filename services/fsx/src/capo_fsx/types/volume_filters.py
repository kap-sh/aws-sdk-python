"""Generated from Smithy shape ``com.amazonaws.fsx#VolumeFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.volume_filter

VolumeFilters: TypeAlias = list["capo_fsx.types.volume_filter.VolumeFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VolumeFilters) -> list:
    import capo_fsx.types.volume_filter

    out: list = []
    for item in value:
        out.append(capo_fsx.types.volume_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> VolumeFilters:
    import capo_fsx.types.volume_filter

    out: VolumeFilters = []
    for item in data:
        out.append(capo_fsx.types.volume_filter.deserialize_aws_json_1_1(item))
    return out
