"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentStageGroupByList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_intent_stage_group_by_specification

AnalyticsIntentStageGroupByList: TypeAlias = list[
    "capo_lex_models_v2.types.analytics_intent_stage_group_by_specification.AnalyticsIntentStageGroupBySpecification"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentStageGroupByList) -> list:
    import capo_lex_models_v2.types.analytics_intent_stage_group_by_specification

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.analytics_intent_stage_group_by_specification.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AnalyticsIntentStageGroupByList:
    import capo_lex_models_v2.types.analytics_intent_stage_group_by_specification

    out: AnalyticsIntentStageGroupByList = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.analytics_intent_stage_group_by_specification.deserialize_json(
                item
            )
        )
    return out
