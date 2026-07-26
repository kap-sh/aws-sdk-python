"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetBotAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.alias_name
    import capo_lex_model_building_service.types.bot_name


class GetBotAliasRequest(TypedDict, closed=True):
    name: "capo_lex_model_building_service.types.alias_name.AliasName"
    """<p>The name of the bot alias. The name is case sensitive.</p>"""
    bot_name: "capo_lex_model_building_service.types.bot_name.BotName"
    """<p>The name of the bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBotAliasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBotAliasRequest:
    out: GetBotAliasRequest = {}  # type: ignore[typeddict-item]
    return out
