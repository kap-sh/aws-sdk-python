"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentMetricResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_intent_metric_result

AnalyticsIntentMetricResults: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.analytics_intent_metric_result.AnalyticsIntentMetricResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentMetricResults) -> list:
    import aws_sdk_lex_models_v2.types.analytics_intent_metric_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_intent_metric_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AnalyticsIntentMetricResults:
    import aws_sdk_lex_models_v2.types.analytics_intent_metric_result

    out: AnalyticsIntentMetricResults = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_intent_metric_result.deserialize_json(
                item
            )
        )
    return out
