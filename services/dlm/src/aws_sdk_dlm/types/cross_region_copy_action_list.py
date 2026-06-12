"""Generated from Smithy shape ``com.amazonaws.dlm#CrossRegionCopyActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dlm.types.cross_region_copy_action

CrossRegionCopyActionList: TypeAlias = list[
    "aws_sdk_dlm.types.cross_region_copy_action.CrossRegionCopyAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: CrossRegionCopyActionList) -> list:
    import aws_sdk_dlm.types.cross_region_copy_action

    out: list = []
    for item in value:
        out.append(aws_sdk_dlm.types.cross_region_copy_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> CrossRegionCopyActionList:
    import aws_sdk_dlm.types.cross_region_copy_action

    out: CrossRegionCopyActionList = []
    for item in data:
        out.append(aws_sdk_dlm.types.cross_region_copy_action.deserialize_json(item))
    return out
