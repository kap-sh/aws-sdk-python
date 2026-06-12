"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceAttributeResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.name


class AnalyticsUtteranceAttributeResult(TypedDict):
    last_used_intent: NotRequired["aws_sdk_lex_models_v2.types.name.Name"]
    """<p>The intent that the bot mapped the utterance to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsUtteranceAttributeResult) -> dict:
    out: dict = {}
    if "last_used_intent" in value:
        out["lastUsedIntent"] = value["last_used_intent"]
    return out


def deserialize_json(data: dict) -> AnalyticsUtteranceAttributeResult:
    out: AnalyticsUtteranceAttributeResult = {}  # type: ignore[typeddict-item]
    if "lastUsedIntent" in data:
        out["last_used_intent"] = data["lastUsedIntent"]
    return out
