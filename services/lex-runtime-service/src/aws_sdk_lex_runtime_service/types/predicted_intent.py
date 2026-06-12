"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#PredictedIntent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_service.types.intent_confidence
    import aws_sdk_lex_runtime_service.types.intent_name
    import aws_sdk_lex_runtime_service.types.string_map


class PredictedIntent(TypedDict):
    intent_name: NotRequired["aws_sdk_lex_runtime_service.types.intent_name.IntentName"]
    """<p>The name of the intent that Amazon Lex suggests satisfies the user's intent.</p>"""
    nlu_intent_confidence: NotRequired[
        "aws_sdk_lex_runtime_service.types.intent_confidence.IntentConfidence"
    ]
    """<p>Indicates how confident Amazon Lex is that an intent satisfies the user's intent.</p>"""
    slots: NotRequired["aws_sdk_lex_runtime_service.types.string_map.StringMap"]
    """<p>The slot and slot values associated with the predicted intent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PredictedIntent) -> dict:
    out: dict = {}
    if "intent_name" in value:
        out["intentName"] = value["intent_name"]
    if "nlu_intent_confidence" in value:
        import aws_sdk_lex_runtime_service.types.intent_confidence

        out["nluIntentConfidence"] = (
            aws_sdk_lex_runtime_service.types.intent_confidence.serialize_json(
                value["nlu_intent_confidence"]
            )
        )
    if "slots" in value:
        import aws_sdk_lex_runtime_service.types.string_map

        out["slots"] = aws_sdk_lex_runtime_service.types.string_map.serialize_json(
            value["slots"]
        )
    return out


def deserialize_json(data: dict) -> PredictedIntent:
    out: PredictedIntent = {}  # type: ignore[typeddict-item]
    if "intentName" in data:
        out["intent_name"] = data["intentName"]
    if "nluIntentConfidence" in data:
        import aws_sdk_lex_runtime_service.types.intent_confidence

        out["nlu_intent_confidence"] = (
            aws_sdk_lex_runtime_service.types.intent_confidence.deserialize_json(
                data["nluIntentConfidence"]
            )
        )
    if "slots" in data:
        import aws_sdk_lex_runtime_service.types.string_map

        out["slots"] = aws_sdk_lex_runtime_service.types.string_map.deserialize_json(
            data["slots"]
        )
    return out
