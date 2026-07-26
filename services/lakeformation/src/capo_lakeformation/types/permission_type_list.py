"""Generated from Smithy shape ``com.amazonaws.lakeformation#PermissionTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.permission_type

PermissionTypeList: TypeAlias = list[
    "capo_lakeformation.types.permission_type.PermissionType"
]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionTypeList) -> list:
    import capo_lakeformation.types.permission_type

    out: list = []
    for item in value:
        out.append(capo_lakeformation.types.permission_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> PermissionTypeList:
    import capo_lakeformation.types.permission_type

    out: PermissionTypeList = []
    for item in data:
        out.append(capo_lakeformation.types.permission_type.deserialize_json(item))
    return out
