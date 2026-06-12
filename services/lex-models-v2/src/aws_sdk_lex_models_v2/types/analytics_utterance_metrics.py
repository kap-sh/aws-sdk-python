"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_utterance_metric

AnalyticsUtteranceMetrics: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.analytics_utterance_metric.AnalyticsUtteranceMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsUtteranceMetrics) -> list:
    import aws_sdk_lex_models_v2.types.analytics_utterance_metric

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_utterance_metric.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalyticsUtteranceMetrics:
    import aws_sdk_lex_models_v2.types.analytics_utterance_metric

    out: AnalyticsUtteranceMetrics = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_utterance_metric.deserialize_json(
                item
            )
        )
    return out
