"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#SlotTypeMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.slot_type_metadata

SlotTypeMetadataList: TypeAlias = list[
    "aws_sdk_lex_model_building_service.types.slot_type_metadata.SlotTypeMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: SlotTypeMetadataList) -> list:
    import aws_sdk_lex_model_building_service.types.slot_type_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_model_building_service.types.slot_type_metadata.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SlotTypeMetadataList:
    import aws_sdk_lex_model_building_service.types.slot_type_metadata

    out: SlotTypeMetadataList = []
    for item in data:
        out.append(
            aws_sdk_lex_model_building_service.types.slot_type_metadata.deserialize_json(
                item
            )
        )
    return out
