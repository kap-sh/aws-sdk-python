"""Generated from Smithy shape ``com.amazonaws.connectparticipant#Receipts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectparticipant.types.receipt

Receipts: TypeAlias = list["capo_connectparticipant.types.receipt.Receipt"]


# --- restJson1 ser/de ---
def serialize_json(value: Receipts) -> list:
    import capo_connectparticipant.types.receipt

    out: list = []
    for item in value:
        out.append(capo_connectparticipant.types.receipt.serialize_json(item))
    return out


def deserialize_json(data: list) -> Receipts:
    import capo_connectparticipant.types.receipt

    out: Receipts = []
    for item in data:
        out.append(capo_connectparticipant.types.receipt.deserialize_json(item))
    return out
