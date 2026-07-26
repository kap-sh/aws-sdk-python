"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceAttributeResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_utterance_attribute_result

AnalyticsUtteranceAttributeResults: TypeAlias = list[
    "capo_lex_models_v2.types.analytics_utterance_attribute_result.AnalyticsUtteranceAttributeResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsUtteranceAttributeResults) -> list:
    import capo_lex_models_v2.types.analytics_utterance_attribute_result

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.analytics_utterance_attribute_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AnalyticsUtteranceAttributeResults:
    import capo_lex_models_v2.types.analytics_utterance_attribute_result

    out: AnalyticsUtteranceAttributeResults = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.analytics_utterance_attribute_result.deserialize_json(
                item
            )
        )
    return out
