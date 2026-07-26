"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceGroupByList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_utterance_group_by_specification

AnalyticsUtteranceGroupByList: TypeAlias = list[
    "capo_lex_models_v2.types.analytics_utterance_group_by_specification.AnalyticsUtteranceGroupBySpecification"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsUtteranceGroupByList) -> list:
    import capo_lex_models_v2.types.analytics_utterance_group_by_specification

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.analytics_utterance_group_by_specification.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AnalyticsUtteranceGroupByList:
    import capo_lex_models_v2.types.analytics_utterance_group_by_specification

    out: AnalyticsUtteranceGroupByList = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.analytics_utterance_group_by_specification.deserialize_json(
                item
            )
        )
    return out
