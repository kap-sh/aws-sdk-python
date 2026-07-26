"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#RecommendedIntentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.sample_utterances_count


class RecommendedIntentSummary(TypedDict, closed=True):
    intent_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of a recommended intent associated with the bot recommendation.</p>"""
    intent_name: NotRequired["capo_lex_models_v2.types.name.Name"]
    """<p>The name of a recommended intent associated with the bot recommendation.</p>"""
    sample_utterances_count: NotRequired[
        "capo_lex_models_v2.types.sample_utterances_count.SampleUtterancesCount"
    ]
    """<p>The count of sample utterances of a recommended intent that is associated with a bot recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendedIntentSummary) -> dict:
    out: dict = {}
    if "intent_id" in value:
        out["intentId"] = value["intent_id"]
    if "intent_name" in value:
        out["intentName"] = value["intent_name"]
    if "sample_utterances_count" in value:
        out["sampleUtterancesCount"] = value["sample_utterances_count"]
    return out


def deserialize_json(data: dict) -> RecommendedIntentSummary:
    out: RecommendedIntentSummary = {}  # type: ignore[typeddict-item]
    if "intentId" in data:
        out["intent_id"] = data["intentId"]
    if "intentName" in data:
        out["intent_name"] = data["intentName"]
    if "sampleUtterancesCount" in data:
        out["sample_utterances_count"] = data["sampleUtterancesCount"]
    return out
