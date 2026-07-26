"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateFlowPermissionsInputRevokePermissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.permission

UpdateFlowPermissionsInputRevokePermissionsList: TypeAlias = list[
    "capo_quicksight.types.permission.Permission"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFlowPermissionsInputRevokePermissionsList) -> list:
    import capo_quicksight.types.permission

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.permission.serialize_json(item))
    return out


def deserialize_json(data: list) -> UpdateFlowPermissionsInputRevokePermissionsList:
    import capo_quicksight.types.permission

    out: UpdateFlowPermissionsInputRevokePermissionsList = []
    for item in data:
        out.append(capo_quicksight.types.permission.deserialize_json(item))
    return out
