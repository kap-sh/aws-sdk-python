"""Generated from Smithy shape ``com.amazonaws.wickr#DeleteBotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.bot_id
    import capo_wickr.types.network_id


class DeleteBotRequest(TypedDict, closed=True):
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network from which the bot will be deleted.</p>"""
    bot_id: "capo_wickr.types.bot_id.BotId"
    """<p>The unique identifier of the bot to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBotRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBotRequest:
    out: DeleteBotRequest = {}  # type: ignore[typeddict-item]
    return out
