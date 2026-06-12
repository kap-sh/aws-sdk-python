"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsSessionMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_session_metric

AnalyticsSessionMetrics: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.analytics_session_metric.AnalyticsSessionMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsSessionMetrics) -> list:
    import aws_sdk_lex_models_v2.types.analytics_session_metric

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_session_metric.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalyticsSessionMetrics:
    import aws_sdk_lex_models_v2.types.analytics_session_metric

    out: AnalyticsSessionMetrics = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_session_metric.deserialize_json(item)
        )
    return out
