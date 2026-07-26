"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentStageGroupByKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_intent_stage_group_by_key

AnalyticsIntentStageGroupByKeys: TypeAlias = list[
    "capo_lex_models_v2.types.analytics_intent_stage_group_by_key.AnalyticsIntentStageGroupByKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentStageGroupByKeys) -> list:
    import capo_lex_models_v2.types.analytics_intent_stage_group_by_key

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.analytics_intent_stage_group_by_key.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AnalyticsIntentStageGroupByKeys:
    import capo_lex_models_v2.types.analytics_intent_stage_group_by_key

    out: AnalyticsIntentStageGroupByKeys = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.analytics_intent_stage_group_by_key.deserialize_json(
                item
            )
        )
    return out
