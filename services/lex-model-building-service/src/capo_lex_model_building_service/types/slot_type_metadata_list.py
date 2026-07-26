"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#SlotTypeMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.slot_type_metadata

SlotTypeMetadataList: TypeAlias = list[
    "capo_lex_model_building_service.types.slot_type_metadata.SlotTypeMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: SlotTypeMetadataList) -> list:
    import capo_lex_model_building_service.types.slot_type_metadata

    out: list = []
    for item in value:
        out.append(
            capo_lex_model_building_service.types.slot_type_metadata.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SlotTypeMetadataList:
    import capo_lex_model_building_service.types.slot_type_metadata

    out: SlotTypeMetadataList = []
    for item in data:
        out.append(
            capo_lex_model_building_service.types.slot_type_metadata.deserialize_json(
                item
            )
        )
    return out
