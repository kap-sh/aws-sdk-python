"""Generated from Smithy shape ``com.amazonaws.iot#DeleteRoleAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.role_alias


class DeleteRoleAliasRequest(TypedDict, closed=True):
    role_alias: "capo_iot.types.role_alias.RoleAlias"
    """<p>The role alias to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRoleAliasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRoleAliasRequest:
    out: DeleteRoleAliasRequest = {}  # type: ignore[typeddict-item]
    return out
