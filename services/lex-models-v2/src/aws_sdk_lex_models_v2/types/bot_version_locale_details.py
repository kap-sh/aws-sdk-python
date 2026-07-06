"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotVersionLocaleDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_version


class BotVersionLocaleDetails(TypedDict, closed=True):
    source_bot_version: "aws_sdk_lex_models_v2.types.bot_version.BotVersion"
    """<p>The version of a bot used for a bot locale.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotVersionLocaleDetails) -> dict:
    out: dict = {}
    out["sourceBotVersion"] = value["source_bot_version"]
    return out


def deserialize_json(data: dict) -> BotVersionLocaleDetails:
    out: BotVersionLocaleDetails = {}  # type: ignore[typeddict-item]
    if "sourceBotVersion" in data:
        out["source_bot_version"] = data["sourceBotVersion"]
    else:
        raise DeserializationError(
            "BotVersionLocaleDetails.source_bot_version required"
        )
    return out
