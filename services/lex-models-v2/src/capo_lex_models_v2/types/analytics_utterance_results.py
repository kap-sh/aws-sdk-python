"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_utterance_result

AnalyticsUtteranceResults: TypeAlias = list[
    "capo_lex_models_v2.types.analytics_utterance_result.AnalyticsUtteranceResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsUtteranceResults) -> list:
    import capo_lex_models_v2.types.analytics_utterance_result

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.analytics_utterance_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalyticsUtteranceResults:
    import capo_lex_models_v2.types.analytics_utterance_result

    out: AnalyticsUtteranceResults = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.analytics_utterance_result.deserialize_json(item)
        )
    return out
