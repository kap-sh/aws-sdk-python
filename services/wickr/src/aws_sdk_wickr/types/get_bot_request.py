"""Generated from Smithy shape ``com.amazonaws.wickr#GetBotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_wickr.types.bot_id
    import aws_sdk_wickr.types.network_id


class GetBotRequest(TypedDict, closed=True):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network containing the bot.</p>"""
    bot_id: "aws_sdk_wickr.types.bot_id.BotId"
    """<p>The unique identifier of the bot to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBotRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBotRequest:
    out: GetBotRequest = {}  # type: ignore[typeddict-item]
    return out
