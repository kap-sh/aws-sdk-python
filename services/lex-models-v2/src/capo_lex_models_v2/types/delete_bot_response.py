"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteBotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_status
    import capo_lex_models_v2.types.id


class DeleteBotResponse(TypedDict, closed=True):
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the bot that Amazon Lex is deleting.</p>"""
    bot_status: NotRequired["capo_lex_models_v2.types.bot_status.BotStatus"]
    """<p>The current status of the bot. The status is <code>Deleting</code> while the bot and its associated resources are being deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBotResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_status" in value:
        import capo_lex_models_v2.types.bot_status

        out["botStatus"] = capo_lex_models_v2.types.bot_status.serialize_json(
            value["bot_status"]
        )
    return out


def deserialize_json(data: dict) -> DeleteBotResponse:
    out: DeleteBotResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botStatus" in data:
        import capo_lex_models_v2.types.bot_status

        out["bot_status"] = capo_lex_models_v2.types.bot_status.deserialize_json(
            data["botStatus"]
        )
    return out
