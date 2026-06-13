"""Generated from Smithy shape ``com.amazonaws.quicksight#Slots``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.slot

Slots: TypeAlias = list["aws_sdk_quicksight.types.slot.Slot"]


# --- restJson1 ser/de ---
def serialize_json(value: Slots) -> list:
    import aws_sdk_quicksight.types.slot

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.slot.serialize_json(item))
    return out


def deserialize_json(data: list) -> Slots:
    import aws_sdk_quicksight.types.slot

    out: Slots = []
    for item in data:
        out.append(aws_sdk_quicksight.types.slot.deserialize_json(item))
    return out
