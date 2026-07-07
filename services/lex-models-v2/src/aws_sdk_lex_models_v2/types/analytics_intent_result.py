"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_bin_keys
    import aws_sdk_lex_models_v2.types.analytics_intent_group_by_keys
    import aws_sdk_lex_models_v2.types.analytics_intent_metric_results


class AnalyticsIntentResult(TypedDict, closed=True):
    bin_keys: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_bin_keys.AnalyticsBinKeys"
    ]
    """<p>A list of objects containing the criteria you requested for binning results and the values of the bins.</p>"""
    group_by_keys: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_intent_group_by_keys.AnalyticsIntentGroupByKeys"
    ]
    """<p>A list of objects containing the criteria you requested for grouping results and the values of the groups.</p>"""
    metrics_results: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_intent_metric_results.AnalyticsIntentMetricResults"
    ]
    """<p>A list of objects, each of which contains a metric you want to list, the statistic for the metric you want to return, and the method by which to organize the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentResult) -> dict:
    out: dict = {}
    if "bin_keys" in value:
        import aws_sdk_lex_models_v2.types.analytics_bin_keys

        out["binKeys"] = aws_sdk_lex_models_v2.types.analytics_bin_keys.serialize_json(
            value["bin_keys"]
        )
    if "group_by_keys" in value:
        import aws_sdk_lex_models_v2.types.analytics_intent_group_by_keys

        out["groupByKeys"] = (
            aws_sdk_lex_models_v2.types.analytics_intent_group_by_keys.serialize_json(
                value["group_by_keys"]
            )
        )
    if "metrics_results" in value:
        import aws_sdk_lex_models_v2.types.analytics_intent_metric_results

        out["metricsResults"] = (
            aws_sdk_lex_models_v2.types.analytics_intent_metric_results.serialize_json(
                value["metrics_results"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnalyticsIntentResult:
    out: AnalyticsIntentResult = {}  # type: ignore[typeddict-item]
    if "binKeys" in data:
        import aws_sdk_lex_models_v2.types.analytics_bin_keys

        out["bin_keys"] = (
            aws_sdk_lex_models_v2.types.analytics_bin_keys.deserialize_json(
                data["binKeys"]
            )
        )
    if "groupByKeys" in data:
        import aws_sdk_lex_models_v2.types.analytics_intent_group_by_keys

        out["group_by_keys"] = (
            aws_sdk_lex_models_v2.types.analytics_intent_group_by_keys.deserialize_json(
                data["groupByKeys"]
            )
        )
    if "metricsResults" in data:
        import aws_sdk_lex_models_v2.types.analytics_intent_metric_results

        out["metrics_results"] = (
            aws_sdk_lex_models_v2.types.analytics_intent_metric_results.deserialize_json(
                data["metricsResults"]
            )
        )
    return out
