"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#RoleArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.role_arn

RoleArnList: TypeAlias = list["aws_sdk_rolesanywhere.types.role_arn.RoleArn"]


# --- restJson1 ser/de ---
def serialize_json(value: RoleArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> RoleArnList:
    return list(data)
