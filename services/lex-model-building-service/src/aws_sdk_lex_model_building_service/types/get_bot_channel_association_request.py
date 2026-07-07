"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetBotChannelAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.alias_name
    import aws_sdk_lex_model_building_service.types.bot_channel_name
    import aws_sdk_lex_model_building_service.types.bot_name


class GetBotChannelAssociationRequest(TypedDict, closed=True):
    name: "aws_sdk_lex_model_building_service.types.bot_channel_name.BotChannelName"
    """<p>The name of the association between the bot and the channel. The name is case sensitive. </p>"""
    bot_name: "aws_sdk_lex_model_building_service.types.bot_name.BotName"
    """<p>The name of the Amazon Lex bot.</p>"""
    bot_alias: "aws_sdk_lex_model_building_service.types.alias_name.AliasName"
    """<p>An alias pointing to the specific version of the Amazon Lex bot to which this association is being made.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBotChannelAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBotChannelAssociationRequest:
    out: GetBotChannelAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
