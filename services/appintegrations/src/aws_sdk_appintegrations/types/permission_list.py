"""Generated from Smithy shape ``com.amazonaws.appintegrations#PermissionList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.permission

PermissionList: TypeAlias = list["aws_sdk_appintegrations.types.permission.Permission"]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionList) -> list:
    return list(value)


def deserialize_json(data: list) -> PermissionList:
    return list(data)