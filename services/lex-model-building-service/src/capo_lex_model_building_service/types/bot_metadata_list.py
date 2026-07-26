"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#BotMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.bot_metadata

BotMetadataList: TypeAlias = list[
    "capo_lex_model_building_service.types.bot_metadata.BotMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: BotMetadataList) -> list:
    import capo_lex_model_building_service.types.bot_metadata

    out: list = []
    for item in value:
        out.append(
            capo_lex_model_building_service.types.bot_metadata.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BotMetadataList:
    import capo_lex_model_building_service.types.bot_metadata

    out: BotMetadataList = []
    for item in data:
        out.append(
            capo_lex_model_building_service.types.bot_metadata.deserialize_json(item)
        )
    return out
