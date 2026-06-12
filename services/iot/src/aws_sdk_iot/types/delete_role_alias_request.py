"""Generated from Smithy shape ``com.amazonaws.iot#DeleteRoleAliasRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.role_alias


class DeleteRoleAliasRequest(TypedDict):
    role_alias: "aws_sdk_iot.types.role_alias.RoleAlias"
    """<p>The role alias to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRoleAliasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRoleAliasRequest:
    out: DeleteRoleAliasRequest = {}  # type: ignore[typeddict-item]
    return out
