"""Generated from Smithy shape ``com.amazonaws.qapps#PermissionsInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qapps.types.permission_input

PermissionsInputList: TypeAlias = list[
    "capo_qapps.types.permission_input.PermissionInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionsInputList) -> list:
    import capo_qapps.types.permission_input

    out: list = []
    for item in value:
        out.append(capo_qapps.types.permission_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> PermissionsInputList:
    import capo_qapps.types.permission_input

    out: PermissionsInputList = []
    for item in data:
        out.append(capo_qapps.types.permission_input.deserialize_json(item))
    return out
