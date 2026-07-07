"""Generated from Smithy shape ``com.amazonaws.chime#RegenerateSecurityTokenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.bot


class RegenerateSecurityTokenResponse(TypedDict, closed=True):
    bot: NotRequired["aws_sdk_chime.types.bot.Bot"]
    """<p>A resource that allows Enterprise account administrators to configure an interface that receives events from Amazon Chime.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegenerateSecurityTokenResponse) -> dict:
    out: dict = {}
    if "bot" in value:
        import aws_sdk_chime.types.bot

        out["Bot"] = aws_sdk_chime.types.bot.serialize_json(value["bot"])
    return out


def deserialize_json(data: dict) -> RegenerateSecurityTokenResponse:
    out: RegenerateSecurityTokenResponse = {}  # type: ignore[typeddict-item]
    if "Bot" in data:
        import aws_sdk_chime.types.bot

        out["bot"] = aws_sdk_chime.types.bot.deserialize_json(data["Bot"])
    return out
