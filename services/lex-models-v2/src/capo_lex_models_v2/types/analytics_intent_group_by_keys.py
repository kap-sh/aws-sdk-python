"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentGroupByKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_intent_group_by_key

AnalyticsIntentGroupByKeys: TypeAlias = list[
    "capo_lex_models_v2.types.analytics_intent_group_by_key.AnalyticsIntentGroupByKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentGroupByKeys) -> list:
    import capo_lex_models_v2.types.analytics_intent_group_by_key

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.analytics_intent_group_by_key.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalyticsIntentGroupByKeys:
    import capo_lex_models_v2.types.analytics_intent_group_by_key

    out: AnalyticsIntentGroupByKeys = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.analytics_intent_group_by_key.deserialize_json(
                item
            )
        )
    return out
