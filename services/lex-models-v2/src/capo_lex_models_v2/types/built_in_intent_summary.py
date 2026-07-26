"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BuiltInIntentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.intent_signature


class BuiltInIntentSummary(TypedDict, closed=True):
    intent_signature: NotRequired[
        "capo_lex_models_v2.types.intent_signature.IntentSignature"
    ]
    """<p>The signature of the built-in intent. Use this to specify the parent intent of a derived intent.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>The description of the intent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BuiltInIntentSummary) -> dict:
    out: dict = {}
    if "intent_signature" in value:
        out["intentSignature"] = value["intent_signature"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> BuiltInIntentSummary:
    out: BuiltInIntentSummary = {}  # type: ignore[typeddict-item]
    if "intentSignature" in data:
        out["intent_signature"] = data["intentSignature"]
    if "description" in data:
        out["description"] = data["description"]
    return out
