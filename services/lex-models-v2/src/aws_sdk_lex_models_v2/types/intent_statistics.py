"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentStatistics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.count


class IntentStatistics(TypedDict):
    discovered_intent_count: NotRequired["aws_sdk_lex_models_v2.types.count.Count"]
    """<p>The number of recommended intents associated with the bot recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntentStatistics) -> dict:
    out: dict = {}
    if "discovered_intent_count" in value:
        out["discoveredIntentCount"] = value["discovered_intent_count"]
    return out


def deserialize_json(data: dict) -> IntentStatistics:
    out: IntentStatistics = {}  # type: ignore[typeddict-item]
    if "discoveredIntentCount" in data:
        out["discovered_intent_count"] = data["discoveredIntentCount"]
    return out
