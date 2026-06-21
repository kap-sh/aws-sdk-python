"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BuiltInSlotTypeSortAttribute``."""

from typing import Literal, TypeAlias, cast

BuiltInSlotTypeSortAttribute: TypeAlias = Literal["SlotTypeSignature",]


# --- restJson1 ser/de ---
def serialize_json(value: BuiltInSlotTypeSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> BuiltInSlotTypeSortAttribute:
    return cast(BuiltInSlotTypeSortAttribute, data)
