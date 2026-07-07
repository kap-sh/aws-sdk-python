"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetBotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.bot_name
    import aws_sdk_lex_model_building_service.types.string


class GetBotRequest(TypedDict, closed=True):
    name: "aws_sdk_lex_model_building_service.types.bot_name.BotName"
    """<p>The name of the bot. The name is case sensitive. </p>"""
    version_or_alias: "aws_sdk_lex_model_building_service.types.string.String"
    """<p>The version or alias of the bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBotRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBotRequest:
    out: GetBotRequest = {}  # type: ignore[typeddict-item]
    return out
