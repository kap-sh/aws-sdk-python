"""Generated from Smithy shape ``com.amazonaws.mpa#UpdateActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mpa.types.update_action

UpdateActions: TypeAlias = list["capo_mpa.types.update_action.UpdateAction"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateActions) -> list:
    import capo_mpa.types.update_action

    out: list = []
    for item in value:
        out.append(capo_mpa.types.update_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> UpdateActions:
    import capo_mpa.types.update_action

    out: UpdateActions = []
    for item in data:
        out.append(capo_mpa.types.update_action.deserialize_json(item))
    return out
