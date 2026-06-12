"""Generated from Smithy shape ``com.amazonaws.ram#AssociatedPermissionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ram.types.associated_permission

AssociatedPermissionList: TypeAlias = list[
    "aws_sdk_ram.types.associated_permission.AssociatedPermission"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedPermissionList) -> list:
    import aws_sdk_ram.types.associated_permission

    out: list = []
    for item in value:
        out.append(aws_sdk_ram.types.associated_permission.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssociatedPermissionList:
    import aws_sdk_ram.types.associated_permission

    out: AssociatedPermissionList = []
    for item in data:
        out.append(aws_sdk_ram.types.associated_permission.deserialize_json(item))
    return out
