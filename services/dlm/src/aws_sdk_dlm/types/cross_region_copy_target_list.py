"""Generated from Smithy shape ``com.amazonaws.dlm#CrossRegionCopyTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dlm.types.cross_region_copy_target

CrossRegionCopyTargetList: TypeAlias = list[
    "aws_sdk_dlm.types.cross_region_copy_target.CrossRegionCopyTarget"
]


# --- restJson1 ser/de ---
def serialize_json(value: CrossRegionCopyTargetList) -> list:
    import aws_sdk_dlm.types.cross_region_copy_target

    out: list = []
    for item in value:
        out.append(aws_sdk_dlm.types.cross_region_copy_target.serialize_json(item))
    return out


def deserialize_json(data: list) -> CrossRegionCopyTargetList:
    import aws_sdk_dlm.types.cross_region_copy_target

    out: CrossRegionCopyTargetList = []
    for item in data:
        out.append(aws_sdk_dlm.types.cross_region_copy_target.deserialize_json(item))
    return out
