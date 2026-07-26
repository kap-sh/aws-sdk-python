"""Generated from Smithy shape ``com.amazonaws.grafana#UpdateInstruction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import capo_grafana.types.role
    import capo_grafana.types.update_action
    import capo_grafana.types.user_list


class UpdateInstruction(TypedDict, closed=True):
    action: "capo_grafana.types.update_action.UpdateAction"
    """<p>Specifies whether this update is to add or revoke role permissions.</p>"""
    role: "capo_grafana.types.role.Role"
    """<p>The role to add or revoke for the user or the group specified in <code>users</code>.</p>"""
    users: "capo_grafana.types.user_list.UserList"
    """<p>A structure that specifies the user or group to add or revoke the role for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateInstruction) -> dict:
    out: dict = {}
    out["action"] = value["action"]
    out["role"] = value["role"]
    import capo_grafana.types.user_list

    out["users"] = capo_grafana.types.user_list.serialize_json(value["users"])
    return out


def deserialize_json(data: dict) -> UpdateInstruction:
    out: UpdateInstruction = {}  # type: ignore[typeddict-item]
    if "action" in data:
        out["action"] = data["action"]
    else:
        raise DeserializationError("UpdateInstruction.action required")
    if "role" in data:
        out["role"] = data["role"]
    else:
        raise DeserializationError("UpdateInstruction.role required")
    if "users" in data:
        import capo_grafana.types.user_list

        out["users"] = capo_grafana.types.user_list.deserialize_json(data["users"])
    else:
        raise DeserializationError("UpdateInstruction.users required")
    return out
