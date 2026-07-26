"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_utterance_filter

AnalyticsUtteranceFilters: TypeAlias = list[
    "capo_lex_models_v2.types.analytics_utterance_filter.AnalyticsUtteranceFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsUtteranceFilters) -> list:
    import capo_lex_models_v2.types.analytics_utterance_filter

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.analytics_utterance_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalyticsUtteranceFilters:
    import capo_lex_models_v2.types.analytics_utterance_filter

    out: AnalyticsUtteranceFilters = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.analytics_utterance_filter.deserialize_json(item)
        )
    return out
