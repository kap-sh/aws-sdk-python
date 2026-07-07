"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_bin_keys
    import aws_sdk_lex_models_v2.types.analytics_utterance_attribute_results
    import aws_sdk_lex_models_v2.types.analytics_utterance_group_by_keys
    import aws_sdk_lex_models_v2.types.analytics_utterance_metric_results


class AnalyticsUtteranceResult(TypedDict, closed=True):
    bin_keys: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_bin_keys.AnalyticsBinKeys"
    ]
    """<p>A list of objects containing the criteria you requested for binning results and the values of the bins.</p>"""
    group_by_keys: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_utterance_group_by_keys.AnalyticsUtteranceGroupByKeys"
    ]
    """<p>A list of objects containing the criteria you requested for grouping results and the values of the bins.</p>"""
    metrics_results: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_utterance_metric_results.AnalyticsUtteranceMetricResults"
    ]
    """<p>A list of objects, each of which contains a metric you want to list, the statistic for the metric you want to return, and the method by which to organize the results.</p>"""
    attribute_results: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_utterance_attribute_results.AnalyticsUtteranceAttributeResults"
    ]
    """<p>A list of objects containing information about the last used intent at the time of an utterance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsUtteranceResult) -> dict:
    out: dict = {}
    if "bin_keys" in value:
        import aws_sdk_lex_models_v2.types.analytics_bin_keys

        out["binKeys"] = aws_sdk_lex_models_v2.types.analytics_bin_keys.serialize_json(
            value["bin_keys"]
        )
    if "group_by_keys" in value:
        import aws_sdk_lex_models_v2.types.analytics_utterance_group_by_keys

        out["groupByKeys"] = (
            aws_sdk_lex_models_v2.types.analytics_utterance_group_by_keys.serialize_json(
                value["group_by_keys"]
            )
        )
    if "metrics_results" in value:
        import aws_sdk_lex_models_v2.types.analytics_utterance_metric_results

        out["metricsResults"] = (
            aws_sdk_lex_models_v2.types.analytics_utterance_metric_results.serialize_json(
                value["metrics_results"]
            )
        )
    if "attribute_results" in value:
        import aws_sdk_lex_models_v2.types.analytics_utterance_attribute_results

        out["attributeResults"] = (
            aws_sdk_lex_models_v2.types.analytics_utterance_attribute_results.serialize_json(
                value["attribute_results"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnalyticsUtteranceResult:
    out: AnalyticsUtteranceResult = {}  # type: ignore[typeddict-item]
    if "binKeys" in data:
        import aws_sdk_lex_models_v2.types.analytics_bin_keys

        out["bin_keys"] = (
            aws_sdk_lex_models_v2.types.analytics_bin_keys.deserialize_json(
                data["binKeys"]
            )
        )
    if "groupByKeys" in data:
        import aws_sdk_lex_models_v2.types.analytics_utterance_group_by_keys

        out["group_by_keys"] = (
            aws_sdk_lex_models_v2.types.analytics_utterance_group_by_keys.deserialize_json(
                data["groupByKeys"]
            )
        )
    if "metricsResults" in data:
        import aws_sdk_lex_models_v2.types.analytics_utterance_metric_results

        out["metrics_results"] = (
            aws_sdk_lex_models_v2.types.analytics_utterance_metric_results.deserialize_json(
                data["metricsResults"]
            )
        )
    if "attributeResults" in data:
        import aws_sdk_lex_models_v2.types.analytics_utterance_attribute_results

        out["attribute_results"] = (
            aws_sdk_lex_models_v2.types.analytics_utterance_attribute_results.deserialize_json(
                data["attributeResults"]
            )
        )
    return out
