"""Generated from Smithy shape ``com.amazonaws.lakeformation#PermissionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.permission

PermissionList: TypeAlias = list["capo_lakeformation.types.permission.Permission"]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionList) -> list:
    import capo_lakeformation.types.permission

    out: list = []
    for item in value:
        out.append(capo_lakeformation.types.permission.serialize_json(item))
    return out


def deserialize_json(data: list) -> PermissionList:
    import capo_lakeformation.types.permission

    out: PermissionList = []
    for item in data:
        out.append(capo_lakeformation.types.permission.deserialize_json(item))
    return out
