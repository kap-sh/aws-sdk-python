"""Generated from Smithy shape ``com.amazonaws.managedblockchain#InviteActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_managedblockchain.types.invite_action

InviteActionList: TypeAlias = list[
    "capo_managedblockchain.types.invite_action.InviteAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: InviteActionList) -> list:
    import capo_managedblockchain.types.invite_action

    out: list = []
    for item in value:
        out.append(capo_managedblockchain.types.invite_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> InviteActionList:
    import capo_managedblockchain.types.invite_action

    out: InviteActionList = []
    for item in data:
        out.append(capo_managedblockchain.types.invite_action.deserialize_json(item))
    return out
