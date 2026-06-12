"""Generated from Smithy shape ``com.amazonaws.iot#RoleAliases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.role_alias

RoleAliases: TypeAlias = list["aws_sdk_iot.types.role_alias.RoleAlias"]


# --- restJson1 ser/de ---
def serialize_json(value: RoleAliases) -> list:
    return list(value)


def deserialize_json(data: list) -> RoleAliases:
    return list(data)
