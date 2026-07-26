"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentStageMetricResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_intent_stage_metric_result

AnalyticsIntentStageMetricResults: TypeAlias = list[
    "capo_lex_models_v2.types.analytics_intent_stage_metric_result.AnalyticsIntentStageMetricResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentStageMetricResults) -> list:
    import capo_lex_models_v2.types.analytics_intent_stage_metric_result

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.analytics_intent_stage_metric_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AnalyticsIntentStageMetricResults:
    import capo_lex_models_v2.types.analytics_intent_stage_metric_result

    out: AnalyticsIntentStageMetricResults = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.analytics_intent_stage_metric_result.deserialize_json(
                item
            )
        )
    return out
