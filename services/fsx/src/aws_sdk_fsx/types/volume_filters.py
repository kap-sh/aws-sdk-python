"""Generated from Smithy shape ``com.amazonaws.fsx#VolumeFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.volume_filter

VolumeFilters: TypeAlias = list["aws_sdk_fsx.types.volume_filter.VolumeFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VolumeFilters) -> list:
    import aws_sdk_fsx.types.volume_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_fsx.types.volume_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> VolumeFilters:
    import aws_sdk_fsx.types.volume_filter

    out: VolumeFilters = []
    for item in data:
        out.append(aws_sdk_fsx.types.volume_filter.deserialize_aws_json_1_1(item))
    return out
