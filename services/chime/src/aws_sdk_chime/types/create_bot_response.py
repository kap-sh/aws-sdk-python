"""Generated from Smithy shape ``com.amazonaws.chime#CreateBotResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime.types.bot


class CreateBotResponse(TypedDict):
    bot: NotRequired["aws_sdk_chime.types.bot.Bot"]
    """<p>The bot details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBotResponse) -> dict:
    out: dict = {}
    if "bot" in value:
        import aws_sdk_chime.types.bot

        out["Bot"] = aws_sdk_chime.types.bot.serialize_json(value["bot"])
    return out


def deserialize_json(data: dict) -> CreateBotResponse:
    out: CreateBotResponse = {}  # type: ignore[typeddict-item]
    if "Bot" in data:
        import aws_sdk_chime.types.bot

        out["bot"] = aws_sdk_chime.types.bot.deserialize_json(data["Bot"])
    return out
