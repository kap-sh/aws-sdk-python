"""Generated from Smithy shape ``com.amazonaws.qapps#PermissionsOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qapps.types.permission_output

PermissionsOutputList: TypeAlias = list[
    "capo_qapps.types.permission_output.PermissionOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionsOutputList) -> list:
    import capo_qapps.types.permission_output

    out: list = []
    for item in value:
        out.append(capo_qapps.types.permission_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> PermissionsOutputList:
    import capo_qapps.types.permission_output

    out: PermissionsOutputList = []
    for item in data:
        out.append(capo_qapps.types.permission_output.deserialize_json(item))
    return out
