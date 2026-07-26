"""Generated from Smithy shape ``com.amazonaws.chime#UpdateBotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.bot


class UpdateBotResponse(TypedDict, closed=True):
    bot: NotRequired["capo_chime.types.bot.Bot"]
    """<p>The updated bot details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBotResponse) -> dict:
    out: dict = {}
    if "bot" in value:
        import capo_chime.types.bot

        out["Bot"] = capo_chime.types.bot.serialize_json(value["bot"])
    return out


def deserialize_json(data: dict) -> UpdateBotResponse:
    out: UpdateBotResponse = {}  # type: ignore[typeddict-item]
    if "Bot" in data:
        import capo_chime.types.bot

        out["bot"] = capo_chime.types.bot.deserialize_json(data["Bot"])
    return out
