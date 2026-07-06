"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceMetricResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_metric_statistic
    import aws_sdk_lex_models_v2.types.analytics_metric_value
    import aws_sdk_lex_models_v2.types.analytics_utterance_metric_name


class AnalyticsUtteranceMetricResult(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_utterance_metric_name.AnalyticsUtteranceMetricName"
    ]
    """<p>The metric that you requested.</p> <ul> <li> <p> <code>Count</code> – The number of utterances.</p> </li> <li> <p> <code>Missed</code> – The number of utterances that Amazon Lex failed to recognize.</p> </li> <li> <p> <code>Detected</code> – The number of utterances that Amazon Lex managed to detect.</p> </li> <li> <p> <code>UtteranceTimestamp</code> – The date and time of the utterance.</p> </li> </ul>"""
    statistic: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_metric_statistic.AnalyticsMetricStatistic"
    ]
    """<p>The summary statistic that you requested to calculate.</p> <ul> <li> <p> <code>Sum</code> – The total count for the category you provide in <code>name</code>.</p> </li> <li> <p> <code>Average</code> – The total count divided by the number of utterances in the category you provide in <code>name</code>.</p> </li> <li> <p> <code>Max</code> – The highest count in the category you provide in <code>name</code>.</p> </li> </ul>"""
    value: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_metric_value.AnalyticsMetricValue"
    ]
    """<p>The value of the summary statistic for the metric that you requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsUtteranceMetricResult) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_lex_models_v2.types.analytics_utterance_metric_name

        out["name"] = (
            aws_sdk_lex_models_v2.types.analytics_utterance_metric_name.serialize_json(
                value["name"]
            )
        )
    if "statistic" in value:
        import aws_sdk_lex_models_v2.types.analytics_metric_statistic

        out["statistic"] = (
            aws_sdk_lex_models_v2.types.analytics_metric_statistic.serialize_json(
                value["statistic"]
            )
        )
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> AnalyticsUtteranceMetricResult:
    out: AnalyticsUtteranceMetricResult = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_lex_models_v2.types.analytics_utterance_metric_name

        out["name"] = (
            aws_sdk_lex_models_v2.types.analytics_utterance_metric_name.deserialize_json(
                data["name"]
            )
        )
    if "statistic" in data:
        import aws_sdk_lex_models_v2.types.analytics_metric_statistic

        out["statistic"] = (
            aws_sdk_lex_models_v2.types.analytics_metric_statistic.deserialize_json(
                data["statistic"]
            )
        )
    if "value" in data:
        out["value"] = data["value"]
    return out
