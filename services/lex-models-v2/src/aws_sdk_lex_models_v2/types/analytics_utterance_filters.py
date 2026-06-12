"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_utterance_filter

AnalyticsUtteranceFilters: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.analytics_utterance_filter.AnalyticsUtteranceFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsUtteranceFilters) -> list:
    import aws_sdk_lex_models_v2.types.analytics_utterance_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_utterance_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalyticsUtteranceFilters:
    import aws_sdk_lex_models_v2.types.analytics_utterance_filter

    out: AnalyticsUtteranceFilters = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_utterance_filter.deserialize_json(
                item
            )
        )
    return out
