"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_intent_metric

AnalyticsIntentMetrics: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.analytics_intent_metric.AnalyticsIntentMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentMetrics) -> list:
    import aws_sdk_lex_models_v2.types.analytics_intent_metric

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_intent_metric.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalyticsIntentMetrics:
    import aws_sdk_lex_models_v2.types.analytics_intent_metric

    out: AnalyticsIntentMetrics = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_intent_metric.deserialize_json(item)
        )
    return out
