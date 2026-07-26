"""Generated from Smithy shape ``com.amazonaws.connect#AllowedUserActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.allowed_user_action

AllowedUserActions: TypeAlias = list[
    "capo_connect.types.allowed_user_action.AllowedUserAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedUserActions) -> list:
    import capo_connect.types.allowed_user_action

    out: list = []
    for item in value:
        out.append(capo_connect.types.allowed_user_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> AllowedUserActions:
    import capo_connect.types.allowed_user_action

    out: AllowedUserActions = []
    for item in data:
        out.append(capo_connect.types.allowed_user_action.deserialize_json(item))
    return out
