"""Generated from Smithy shape ``com.amazonaws.workdocs#PermissionInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.permission_info

PermissionInfoList: TypeAlias = list[
    "capo_workdocs.types.permission_info.PermissionInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionInfoList) -> list:
    import capo_workdocs.types.permission_info

    out: list = []
    for item in value:
        out.append(capo_workdocs.types.permission_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> PermissionInfoList:
    import capo_workdocs.types.permission_info

    out: PermissionInfoList = []
    for item in data:
        out.append(capo_workdocs.types.permission_info.deserialize_json(item))
    return out
