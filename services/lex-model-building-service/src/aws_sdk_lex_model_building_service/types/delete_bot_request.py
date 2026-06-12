"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#DeleteBotRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.bot_name


class DeleteBotRequest(TypedDict):
    name: "aws_sdk_lex_model_building_service.types.bot_name.BotName"
    """<p>The name of the bot. The name is case sensitive. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBotRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBotRequest:
    out: DeleteBotRequest = {}  # type: ignore[typeddict-item]
    return out
