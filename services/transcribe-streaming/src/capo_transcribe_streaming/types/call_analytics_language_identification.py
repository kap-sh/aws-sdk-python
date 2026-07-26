"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#CallAnalyticsLanguageIdentification``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.call_analytics_language_with_score

CallAnalyticsLanguageIdentification: TypeAlias = list[
    "capo_transcribe_streaming.types.call_analytics_language_with_score.CallAnalyticsLanguageWithScore"
]


# --- restJson1 ser/de ---
def serialize_json(value: CallAnalyticsLanguageIdentification) -> list:
    import capo_transcribe_streaming.types.call_analytics_language_with_score

    out: list = []
    for item in value:
        out.append(
            capo_transcribe_streaming.types.call_analytics_language_with_score.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CallAnalyticsLanguageIdentification:
    import capo_transcribe_streaming.types.call_analytics_language_with_score

    out: CallAnalyticsLanguageIdentification = []
    for item in data:
        out.append(
            capo_transcribe_streaming.types.call_analytics_language_with_score.deserialize_json(
                item
            )
        )
    return out
