"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#DeleteBotVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.bot_name
    import capo_lex_model_building_service.types.numerical_version


class DeleteBotVersionRequest(TypedDict, closed=True):
    name: "capo_lex_model_building_service.types.bot_name.BotName"
    """<p>The name of the bot.</p>"""
    version: "capo_lex_model_building_service.types.numerical_version.NumericalVersion"
    """<p>The version of the bot to delete. You cannot delete the <code>$LATEST</code> version of the bot. To delete the <code>$LATEST</code> version, use the <a>DeleteBot</a> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBotVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBotVersionRequest:
    out: DeleteBotVersionRequest = {}  # type: ignore[typeddict-item]
    return out
