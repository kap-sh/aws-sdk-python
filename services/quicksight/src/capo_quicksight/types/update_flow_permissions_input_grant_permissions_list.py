"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateFlowPermissionsInputGrantPermissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.permission

UpdateFlowPermissionsInputGrantPermissionsList: TypeAlias = list[
    "capo_quicksight.types.permission.Permission"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFlowPermissionsInputGrantPermissionsList) -> list:
    import capo_quicksight.types.permission

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.permission.serialize_json(item))
    return out


def deserialize_json(data: list) -> UpdateFlowPermissionsInputGrantPermissionsList:
    import capo_quicksight.types.permission

    out: UpdateFlowPermissionsInputGrantPermissionsList = []
    for item in data:
        out.append(capo_quicksight.types.permission.deserialize_json(item))
    return out
