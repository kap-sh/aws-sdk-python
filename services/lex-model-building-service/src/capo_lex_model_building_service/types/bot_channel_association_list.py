"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#BotChannelAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.bot_channel_association

BotChannelAssociationList: TypeAlias = list[
    "capo_lex_model_building_service.types.bot_channel_association.BotChannelAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: BotChannelAssociationList) -> list:
    import capo_lex_model_building_service.types.bot_channel_association

    out: list = []
    for item in value:
        out.append(
            capo_lex_model_building_service.types.bot_channel_association.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BotChannelAssociationList:
    import capo_lex_model_building_service.types.bot_channel_association

    out: BotChannelAssociationList = []
    for item in data:
        out.append(
            capo_lex_model_building_service.types.bot_channel_association.deserialize_json(
                item
            )
        )
    return out
