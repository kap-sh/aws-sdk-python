"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceMetricResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_utterance_metric_result

AnalyticsUtteranceMetricResults: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.analytics_utterance_metric_result.AnalyticsUtteranceMetricResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsUtteranceMetricResults) -> list:
    import aws_sdk_lex_models_v2.types.analytics_utterance_metric_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_utterance_metric_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AnalyticsUtteranceMetricResults:
    import aws_sdk_lex_models_v2.types.analytics_utterance_metric_result

    out: AnalyticsUtteranceMetricResults = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_utterance_metric_result.deserialize_json(
                item
            )
        )
    return out
