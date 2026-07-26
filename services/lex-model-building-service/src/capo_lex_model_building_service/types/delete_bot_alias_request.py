"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#DeleteBotAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.alias_name
    import capo_lex_model_building_service.types.bot_name


class DeleteBotAliasRequest(TypedDict, closed=True):
    name: "capo_lex_model_building_service.types.alias_name.AliasName"
    """<p>The name of the alias to delete. The name is case sensitive. </p>"""
    bot_name: "capo_lex_model_building_service.types.bot_name.BotName"
    """<p>The name of the bot that the alias points to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBotAliasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBotAliasRequest:
    out: DeleteBotAliasRequest = {}  # type: ignore[typeddict-item]
    return out
