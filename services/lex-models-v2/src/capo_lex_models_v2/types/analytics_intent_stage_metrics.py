"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentStageMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_intent_stage_metric

AnalyticsIntentStageMetrics: TypeAlias = list[
    "capo_lex_models_v2.types.analytics_intent_stage_metric.AnalyticsIntentStageMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentStageMetrics) -> list:
    import capo_lex_models_v2.types.analytics_intent_stage_metric

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.analytics_intent_stage_metric.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalyticsIntentStageMetrics:
    import capo_lex_models_v2.types.analytics_intent_stage_metric

    out: AnalyticsIntentStageMetrics = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.analytics_intent_stage_metric.deserialize_json(
                item
            )
        )
    return out
