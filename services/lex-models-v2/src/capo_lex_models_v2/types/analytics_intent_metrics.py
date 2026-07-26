"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_intent_metric

AnalyticsIntentMetrics: TypeAlias = list[
    "capo_lex_models_v2.types.analytics_intent_metric.AnalyticsIntentMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentMetrics) -> list:
    import capo_lex_models_v2.types.analytics_intent_metric

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.analytics_intent_metric.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalyticsIntentMetrics:
    import capo_lex_models_v2.types.analytics_intent_metric

    out: AnalyticsIntentMetrics = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.analytics_intent_metric.deserialize_json(item)
        )
    return out
