"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#BuiltinSlotTypeMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.builtin_slot_type_metadata

BuiltinSlotTypeMetadataList: TypeAlias = list[
    "aws_sdk_lex_model_building_service.types.builtin_slot_type_metadata.BuiltinSlotTypeMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: BuiltinSlotTypeMetadataList) -> list:
    import aws_sdk_lex_model_building_service.types.builtin_slot_type_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_model_building_service.types.builtin_slot_type_metadata.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BuiltinSlotTypeMetadataList:
    import aws_sdk_lex_model_building_service.types.builtin_slot_type_metadata

    out: BuiltinSlotTypeMetadataList = []
    for item in data:
        out.append(
            aws_sdk_lex_model_building_service.types.builtin_slot_type_metadata.deserialize_json(
                item
            )
        )
    return out
