"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ActionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.action

ActionsList: TypeAlias = list["capo_accessanalyzer.types.action.Action"]


# --- restJson1 ser/de ---
def serialize_json(value: ActionsList) -> list:
    return list(value)


def deserialize_json(data: list) -> ActionsList:
    return list(data)
