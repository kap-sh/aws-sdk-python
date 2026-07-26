"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#BotAliasMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.bot_alias_metadata

BotAliasMetadataList: TypeAlias = list[
    "capo_lex_model_building_service.types.bot_alias_metadata.BotAliasMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: BotAliasMetadataList) -> list:
    import capo_lex_model_building_service.types.bot_alias_metadata

    out: list = []
    for item in value:
        out.append(
            capo_lex_model_building_service.types.bot_alias_metadata.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BotAliasMetadataList:
    import capo_lex_model_building_service.types.bot_alias_metadata

    out: BotAliasMetadataList = []
    for item in data:
        out.append(
            capo_lex_model_building_service.types.bot_alias_metadata.deserialize_json(
                item
            )
        )
    return out
