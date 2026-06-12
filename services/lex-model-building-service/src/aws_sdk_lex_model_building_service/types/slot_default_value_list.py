"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#SlotDefaultValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.slot_default_value

SlotDefaultValueList: TypeAlias = list[
    "aws_sdk_lex_model_building_service.types.slot_default_value.SlotDefaultValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: SlotDefaultValueList) -> list:
    import aws_sdk_lex_model_building_service.types.slot_default_value

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_model_building_service.types.slot_default_value.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SlotDefaultValueList:
    import aws_sdk_lex_model_building_service.types.slot_default_value

    out: SlotDefaultValueList = []
    for item in data:
        out.append(
            aws_sdk_lex_model_building_service.types.slot_default_value.deserialize_json(
                item
            )
        )
    return out
