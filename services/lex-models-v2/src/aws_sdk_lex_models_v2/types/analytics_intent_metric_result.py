"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentMetricResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_intent_metric_name
    import aws_sdk_lex_models_v2.types.analytics_metric_statistic
    import aws_sdk_lex_models_v2.types.analytics_metric_value


class AnalyticsIntentMetricResult(TypedDict):
    name: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_intent_metric_name.AnalyticsIntentMetricName"
    ]
    r"""<p>The metric that you requested. See <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/analytics-key-definitions.html\">Key definitions</a> for more details about these metrics.</p> <ul> <li> <p> <code>Count</code> – The number of times the intent was invoked.</p> </li> <li> <p> <code>Success</code> – The number of times the intent succeeded.</p> </li> <li> <p> <code>Failure</code> – The number of times the intent failed.</p> </li> <li> <p> <code>Switched</code> – The number of times there was a switch to a different intent.</p> </li> <li> <p> <code>Dropped</code> – The number of times the user dropped the intent.</p> </li> </ul>"""
    statistic: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_metric_statistic.AnalyticsMetricStatistic"
    ]
    """<p>The statistic that you requested to calculate.</p> <ul> <li> <p> <code>Sum</code> – The total count for the category you provide in <code>name</code>.</p> </li> <li> <p> <code>Average</code> – The total count divided by the number of intents in the category you provide in <code>name</code>.</p> </li> <li> <p> <code>Max</code> – The highest count in the category you provide in <code>name</code>.</p> </li> </ul>"""
    value: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_metric_value.AnalyticsMetricValue"
    ]
    """<p>The value of the summary statistic for the metric that you requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentMetricResult) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_lex_models_v2.types.analytics_intent_metric_name

        out["name"] = (
            aws_sdk_lex_models_v2.types.analytics_intent_metric_name.serialize_json(
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


def deserialize_json(data: dict) -> AnalyticsIntentMetricResult:
    out: AnalyticsIntentMetricResult = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_lex_models_v2.types.analytics_intent_metric_name

        out["name"] = (
            aws_sdk_lex_models_v2.types.analytics_intent_metric_name.deserialize_json(
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
