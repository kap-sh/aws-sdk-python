"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#DeleteBotChannelAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.alias_name
    import capo_lex_model_building_service.types.bot_channel_name
    import capo_lex_model_building_service.types.bot_name


class DeleteBotChannelAssociationRequest(TypedDict, closed=True):
    name: "capo_lex_model_building_service.types.bot_channel_name.BotChannelName"
    """<p>The name of the association. The name is case sensitive. </p>"""
    bot_name: "capo_lex_model_building_service.types.bot_name.BotName"
    """<p>The name of the Amazon Lex bot.</p>"""
    bot_alias: "capo_lex_model_building_service.types.alias_name.AliasName"
    """<p>An alias that points to the specific version of the Amazon Lex bot to which this association is being made.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBotChannelAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBotChannelAssociationRequest:
    out: DeleteBotChannelAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
