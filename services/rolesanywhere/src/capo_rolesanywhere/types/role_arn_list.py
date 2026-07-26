"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#RoleArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rolesanywhere.types.role_arn

RoleArnList: TypeAlias = list["capo_rolesanywhere.types.role_arn.RoleArn"]


# --- restJson1 ser/de ---
def serialize_json(value: RoleArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> RoleArnList:
    return list(data)
