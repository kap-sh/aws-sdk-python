"""Generated from Smithy shape ``com.amazonaws.dlm#CrossRegionCopyActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dlm.types.cross_region_copy_action

CrossRegionCopyActionList: TypeAlias = list[
    "capo_dlm.types.cross_region_copy_action.CrossRegionCopyAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: CrossRegionCopyActionList) -> list:
    import capo_dlm.types.cross_region_copy_action

    out: list = []
    for item in value:
        out.append(capo_dlm.types.cross_region_copy_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> CrossRegionCopyActionList:
    import capo_dlm.types.cross_region_copy_action

    out: CrossRegionCopyActionList = []
    for item in data:
        out.append(capo_dlm.types.cross_region_copy_action.deserialize_json(item))
    return out
