"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentGroupByList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_intent_group_by_specification

AnalyticsIntentGroupByList: TypeAlias = list[
    "capo_lex_models_v2.types.analytics_intent_group_by_specification.AnalyticsIntentGroupBySpecification"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentGroupByList) -> list:
    import capo_lex_models_v2.types.analytics_intent_group_by_specification

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.analytics_intent_group_by_specification.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AnalyticsIntentGroupByList:
    import capo_lex_models_v2.types.analytics_intent_group_by_specification

    out: AnalyticsIntentGroupByList = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.analytics_intent_group_by_specification.deserialize_json(
                item
            )
        )
    return out
