"""Generated from Smithy shape ``com.amazonaws.quicksight#Slots``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.slot

Slots: TypeAlias = list["capo_quicksight.types.slot.Slot"]


# --- restJson1 ser/de ---
def serialize_json(value: Slots) -> list:
    import capo_quicksight.types.slot

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.slot.serialize_json(item))
    return out


def deserialize_json(data: list) -> Slots:
    import capo_quicksight.types.slot

    out: Slots = []
    for item in data:
        out.append(capo_quicksight.types.slot.deserialize_json(item))
    return out
