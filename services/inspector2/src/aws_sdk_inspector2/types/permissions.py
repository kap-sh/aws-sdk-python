"""Generated from Smithy shape ``com.amazonaws.inspector2#Permissions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.permission

Permissions: TypeAlias = list["aws_sdk_inspector2.types.permission.Permission"]


# --- restJson1 ser/de ---
def serialize_json(value: Permissions) -> list:
    import aws_sdk_inspector2.types.permission

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.permission.serialize_json(item))
    return out


def deserialize_json(data: list) -> Permissions:
    import aws_sdk_inspector2.types.permission

    out: Permissions = []
    for item in data:
        out.append(aws_sdk_inspector2.types.permission.deserialize_json(item))
    return out
