"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#CallAnalyticsLanguageWithScore``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.call_analytics_language_code
    import aws_sdk_transcribe_streaming.types.double


class CallAnalyticsLanguageWithScore(TypedDict):
    language_code: NotRequired[
        "aws_sdk_transcribe_streaming.types.call_analytics_language_code.CallAnalyticsLanguageCode"
    ]
    """<p>The language code of the identified language.</p>"""
    score: "aws_sdk_transcribe_streaming.types.double.Double"
    """<p>The confidence score associated with the identified language code. Confidence scores are values between zero and one; larger values indicate a higher confidence in the identified language.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CallAnalyticsLanguageWithScore) -> dict:
    out: dict = {}
    if "language_code" in value:
        import aws_sdk_transcribe_streaming.types.call_analytics_language_code

        out["LanguageCode"] = (
            aws_sdk_transcribe_streaming.types.call_analytics_language_code.serialize_json(
                value["language_code"]
            )
        )
    out["Score"] = value.get("score", 0)
    return out


def deserialize_json(data: dict) -> CallAnalyticsLanguageWithScore:
    out: CallAnalyticsLanguageWithScore = {}  # type: ignore[typeddict-item]
    if "LanguageCode" in data:
        import aws_sdk_transcribe_streaming.types.call_analytics_language_code

        out["language_code"] = (
            aws_sdk_transcribe_streaming.types.call_analytics_language_code.deserialize_json(
                data["LanguageCode"]
            )
        )
    if "Score" in data:
        out["score"] = data["Score"]
    else:
        out["score"] = 0
    return out
