"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsSessionMetricResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_session_metric_result

AnalyticsSessionMetricResults: TypeAlias = list[
    "capo_lex_models_v2.types.analytics_session_metric_result.AnalyticsSessionMetricResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsSessionMetricResults) -> list:
    import capo_lex_models_v2.types.analytics_session_metric_result

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.analytics_session_metric_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AnalyticsSessionMetricResults:
    import capo_lex_models_v2.types.analytics_session_metric_result

    out: AnalyticsSessionMetricResults = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.analytics_session_metric_result.deserialize_json(
                item
            )
        )
    return out
