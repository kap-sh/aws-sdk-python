"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentStageMetric``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_intent_stage_metric_name
    import aws_sdk_lex_models_v2.types.analytics_metric_statistic
    import aws_sdk_lex_models_v2.types.analytics_sort_order


class AnalyticsIntentStageMetric(TypedDict):
    name: "aws_sdk_lex_models_v2.types.analytics_intent_stage_metric_name.AnalyticsIntentStageMetricName"
    r"""<p>The metric for which you want to get intent stage summary statistics. See <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/analytics-key-definitions.html\">Key definitions</a> for more details about these metrics.</p> <ul> <li> <p> <code>Count</code> – The number of times the intent stage occurred.</p> </li> <li> <p> <code>Success</code> – The number of times the intent stage succeeded.</p> </li> <li> <p> <code>Failure</code> – The number of times the intent stage failed.</p> </li> <li> <p> <code>Dropped</code> – The number of times the user dropped the intent stage.</p> </li> <li> <p> <code>Retry</code> – The number of times the bot tried to elicit a response from the user at this stage.</p> </li> </ul>"""
    statistic: "aws_sdk_lex_models_v2.types.analytics_metric_statistic.AnalyticsMetricStatistic"
    """<p>The summary statistic to calculate.</p> <ul> <li> <p> <code>Sum</code> – The total count for the category you provide in <code>name</code>.</p> </li> <li> <p> <code>Average</code> – The total count divided by the number of intent stages in the category you provide in <code>name</code>.</p> </li> <li> <p> <code>Max</code> – The highest count in the category you provide in <code>name</code>.</p> </li> </ul>"""
    order: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_sort_order.AnalyticsSortOrder"
    ]
    """<p>Specifies whether to sort the results in ascending or descending order of the summary statistic (<code>value</code> in the response).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentStageMetric) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.analytics_intent_stage_metric_name

    out["name"] = (
        aws_sdk_lex_models_v2.types.analytics_intent_stage_metric_name.serialize_json(
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


def deserialize_json(data: dict) -> AnalyticsIntentStageMetric:
    out: AnalyticsIntentStageMetric = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_lex_models_v2.types.analytics_intent_stage_metric_name

        out["name"] = (
            aws_sdk_lex_models_v2.types.analytics_intent_stage_metric_name.deserialize_json(
                data["name"]
            )
        )
    else:
        raise DeserializationError("AnalyticsIntentStageMetric.name required")
    if "statistic" in data:
        import aws_sdk_lex_models_v2.types.analytics_metric_statistic

        out["statistic"] = (
            aws_sdk_lex_models_v2.types.analytics_metric_statistic.deserialize_json(
                data["statistic"]
            )
        )
    else:
        raise DeserializationError("AnalyticsIntentStageMetric.statistic required")
    if "order" in data:
        import aws_sdk_lex_models_v2.types.analytics_sort_order

        out["order"] = (
            aws_sdk_lex_models_v2.types.analytics_sort_order.deserialize_json(
                data["order"]
            )
        )
    return out
