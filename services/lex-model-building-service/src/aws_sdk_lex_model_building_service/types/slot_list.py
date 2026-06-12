"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#SlotList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.slot

SlotList: TypeAlias = list["aws_sdk_lex_model_building_service.types.slot.Slot"]


# --- restJson1 ser/de ---
def serialize_json(value: SlotList) -> list:
    import aws_sdk_lex_model_building_service.types.slot

    out: list = []
    for item in value:
        out.append(aws_sdk_lex_model_building_service.types.slot.serialize_json(item))
    return out


def deserialize_json(data: list) -> SlotList:
    import aws_sdk_lex_model_building_service.types.slot

    out: SlotList = []
    for item in data:
        out.append(aws_sdk_lex_model_building_service.types.slot.deserialize_json(item))
    return out
