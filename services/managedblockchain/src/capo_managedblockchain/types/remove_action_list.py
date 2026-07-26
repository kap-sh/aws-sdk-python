"""Generated from Smithy shape ``com.amazonaws.managedblockchain#RemoveActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_managedblockchain.types.remove_action

RemoveActionList: TypeAlias = list[
    "capo_managedblockchain.types.remove_action.RemoveAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: RemoveActionList) -> list:
    import capo_managedblockchain.types.remove_action

    out: list = []
    for item in value:
        out.append(capo_managedblockchain.types.remove_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> RemoveActionList:
    import capo_managedblockchain.types.remove_action

    out: RemoveActionList = []
    for item in data:
        out.append(capo_managedblockchain.types.remove_action.deserialize_json(item))
    return out
