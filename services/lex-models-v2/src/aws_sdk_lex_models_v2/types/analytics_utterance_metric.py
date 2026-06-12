"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceMetric``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_metric_statistic
    import aws_sdk_lex_models_v2.types.analytics_sort_order
    import aws_sdk_lex_models_v2.types.analytics_utterance_metric_name


class AnalyticsUtteranceMetric(TypedDict):
    name: "aws_sdk_lex_models_v2.types.analytics_utterance_metric_name.AnalyticsUtteranceMetricName"
    """<p>The metric for which you want to get utterance summary statistics.</p> <ul> <li> <p> <code>Count</code> – The number of utterances.</p> </li> <li> <p> <code>Missed</code> – The number of utterances that Amazon Lex failed to recognize.</p> </li> <li> <p> <code>Detected</code> – The number of utterances that Amazon Lex managed to detect.</p> </li> <li> <p> <code>UtteranceTimestamp</code> – The date and time of the utterance.</p> </li> </ul>"""
    statistic: "aws_sdk_lex_models_v2.types.analytics_metric_statistic.AnalyticsMetricStatistic"
    """<p>The summary statistic to calculate.</p> <ul> <li> <p> <code>Sum</code> – The total count for the category you provide in <code>name</code>.</p> </li> <li> <p> <code>Average</code> – The total count divided by the number of utterances in the category you provide in <code>name</code>.</p> </li> <li> <p> <code>Max</code> – The highest count in the category you provide in <code>name</code>.</p> </li> </ul>"""
    order: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_sort_order.AnalyticsSortOrder"
    ]
    """<p>Specifies whether to sort the results in ascending or descending order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsUtteranceMetric) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.analytics_utterance_metric_name

    out["name"] = (
        aws_sdk_lex_models_v2.types.analytics_utterance_metric_name.serialize_json(
            value["name"]
        )
    )
    import aws_sdk_lex_models_v2.types.analytics_metric_statistic

    out["statistic"] = (
        aws_sdk_lex_models_v2.types.analytics_metric_statistic.serialize_json(
            value["statistic"]
        )
    )
    if "order" in value:
        import aws_sdk_lex_models_v2.types.analytics_sort_order

        out["order"] = aws_sdk_lex_models_v2.types.analytics_sort_order.serialize_json(
            value["order"]
        )
    return out


def deserialize_json(data: dict) -> AnalyticsUtteranceMetric:
    out: AnalyticsUtteranceMetric = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_lex_models_v2.types.analytics_utterance_metric_name

        out["name"] = (
            aws_sdk_lex_models_v2.types.analytics_utterance_metric_name.deserialize_json(
                data["name"]
            )
        )
    else:
        raise DeserializationError("AnalyticsUtteranceMetric.name required")
    if "statistic" in data:
        import aws_sdk_lex_models_v2.types.analytics_metric_statistic

        out["statistic"] = (
            aws_sdk_lex_models_v2.types.analytics_metric_statistic.deserialize_json(
                data["statistic"]
            )
        )
    else:
        raise DeserializationError("AnalyticsUtteranceMetric.statistic required")
    if "order" in data:
        import aws_sdk_lex_models_v2.types.analytics_sort_order

        out["order"] = (
            aws_sdk_lex_models_v2.types.analytics_sort_order.deserialize_json(
                data["order"]
            )
        )
    return out
