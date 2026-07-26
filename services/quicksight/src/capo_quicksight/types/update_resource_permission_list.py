"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateResourcePermissionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.resource_permission

UpdateResourcePermissionList: TypeAlias = list[
    "capo_quicksight.types.resource_permission.ResourcePermission"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResourcePermissionList) -> list:
    import capo_quicksight.types.resource_permission

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.resource_permission.serialize_json(item))
    return out


def deserialize_json(data: list) -> UpdateResourcePermissionList:
    import capo_quicksight.types.resource_permission

    out: UpdateResourcePermissionList = []
    for item in data:
        out.append(capo_quicksight.types.resource_permission.deserialize_json(item))
    return out
