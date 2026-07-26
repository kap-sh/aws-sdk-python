"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_utterance_attribute

AnalyticsUtteranceAttributes: TypeAlias = list[
    "capo_lex_models_v2.types.analytics_utterance_attribute.AnalyticsUtteranceAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsUtteranceAttributes) -> list:
    import capo_lex_models_v2.types.analytics_utterance_attribute

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.analytics_utterance_attribute.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalyticsUtteranceAttributes:
    import capo_lex_models_v2.types.analytics_utterance_attribute

    out: AnalyticsUtteranceAttributes = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.analytics_utterance_attribute.deserialize_json(
                item
            )
        )
    return out
