"""Generated from Smithy shape ``com.amazonaws.datazone#AssetPermissions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_permission

AssetPermissions: TypeAlias = list[
    "aws_sdk_datazone.types.asset_permission.AssetPermission"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetPermissions) -> list:
    import aws_sdk_datazone.types.asset_permission

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.asset_permission.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssetPermissions:
    import aws_sdk_datazone.types.asset_permission

    out: AssetPermissions = []
    for item in data:
        out.append(aws_sdk_datazone.types.asset_permission.deserialize_json(item))
    return out
