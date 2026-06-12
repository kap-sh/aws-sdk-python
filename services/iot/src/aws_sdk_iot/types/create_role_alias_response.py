"""Generated from Smithy shape ``com.amazonaws.iot#CreateRoleAliasResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.role_alias
    import aws_sdk_iot.types.role_alias_arn


class CreateRoleAliasResponse(TypedDict):
    role_alias: NotRequired["aws_sdk_iot.types.role_alias.RoleAlias"]
    """<p>The role alias.</p>"""
    role_alias_arn: NotRequired["aws_sdk_iot.types.role_alias_arn.RoleAliasArn"]
    """<p>The role alias ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRoleAliasResponse) -> dict:
    out: dict = {}
    if "role_alias" in value:
        out["roleAlias"] = value["role_alias"]
    if "role_alias_arn" in value:
        out["roleAliasArn"] = value["role_alias_arn"]
    return out


def deserialize_json(data: dict) -> CreateRoleAliasResponse:
    out: CreateRoleAliasResponse = {}  # type: ignore[typeddict-item]
    if "roleAlias" in data:
        out["role_alias"] = data["roleAlias"]
    if "roleAliasArn" in data:
        out["role_alias_arn"] = data["roleAliasArn"]
    return out
