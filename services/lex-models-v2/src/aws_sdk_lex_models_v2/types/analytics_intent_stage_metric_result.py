"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentStageMetricResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_intent_stage_metric_name
    import aws_sdk_lex_models_v2.types.analytics_metric_statistic
    import aws_sdk_lex_models_v2.types.analytics_metric_value


class AnalyticsIntentStageMetricResult(TypedDict):
    name: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_intent_stage_metric_name.AnalyticsIntentStageMetricName"
    ]
    """<p>The metric that you requested.</p> <ul> <li> <p> <code>Count</code> – The number of times the intent stage occurred.</p> </li> <li> <p> <code>Success</code> – The number of times the intent stage succeeded.</p> </li> <li> <p> <code>Failure</code> – The number of times the intent stage failed.</p> </li> <li> <p> <code>Dropped</code> – The number of times the user dropped the intent stage.</p> </li> <li> <p> <code>Retry</code> – The number of times the bot tried to elicit a response from the user at this stage.</p> </li> </ul>"""
    statistic: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_metric_statistic.AnalyticsMetricStatistic"
    ]
    """<p>The summary statistic that you requested to calculate.</p> <ul> <li> <p> <code>Sum</code> – The total count for the category you provide in <code>name</code>.</p> </li> <li> <p> <code>Average</code> – The total count divided by the number of intent stages in the category you provide in <code>name</code>.</p> </li> <li> <p> <code>Max</code> – The highest count in the category you provide in <code>name</code>.</p> </li> </ul>"""
    value: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_metric_value.AnalyticsMetricValue"
    ]
    """<p>The value of the summary statistic for the metric that you requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentStageMetricResult) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_lex_models_v2.types.analytics_intent_stage_metric_name

        out["name"] = (
            aws_sdk_lex_models_v2.types.analytics_intent_stage_metric_name.serialize_json(
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


def deserialize_json(data: dict) -> AnalyticsIntentStageMetricResult:
    out: AnalyticsIntentStageMetricResult = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_lex_models_v2.types.analytics_intent_stage_metric_name

        out["name"] = (
            aws_sdk_lex_models_v2.types.analytics_intent_stage_metric_name.deserialize_json(
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
