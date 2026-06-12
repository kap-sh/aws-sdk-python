"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentStageFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_intent_stage_filter

AnalyticsIntentStageFilters: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.analytics_intent_stage_filter.AnalyticsIntentStageFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentStageFilters) -> list:
    import aws_sdk_lex_models_v2.types.analytics_intent_stage_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_intent_stage_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AnalyticsIntentStageFilters:
    import aws_sdk_lex_models_v2.types.analytics_intent_stage_filter

    out: AnalyticsIntentStageFilters = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_intent_stage_filter.deserialize_json(
                item
            )
        )
    return out
