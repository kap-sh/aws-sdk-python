"""Generated from Smithy shape ``com.amazonaws.glue#MetricBasedObservation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_quality_metric_values
    import aws_sdk_glue.types.hash_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.new_rules


class MetricBasedObservation(TypedDict):
    metric_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the data quality metric used for generating the observation.</p>"""
    statistic_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The Statistic ID.</p>"""
    metric_values: NotRequired[
        "aws_sdk_glue.types.data_quality_metric_values.DataQualityMetricValues"
    ]
    """<p>An object of type <code>DataQualityMetricValues</code> representing the analysis of the data quality metric value.</p>"""
    new_rules: NotRequired["aws_sdk_glue.types.new_rules.NewRules"]
    """<p>A list of new data quality rules generated as part of the observation based on the data quality metric value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricBasedObservation) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "statistic_id" in value:
        out["StatisticId"] = value["statistic_id"]
    if "metric_values" in value:
        import aws_sdk_glue.types.data_quality_metric_values

        out["MetricValues"] = (
            aws_sdk_glue.types.data_quality_metric_values.serialize_aws_json_1_1(
                value["metric_values"]
            )
        )
    if "new_rules" in value:
        import aws_sdk_glue.types.new_rules

        out["NewRules"] = aws_sdk_glue.types.new_rules.serialize_aws_json_1_1(
            value["new_rules"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricBasedObservation:
    out: MetricBasedObservation = {}  # type: ignore[typeddict-item]
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    if "StatisticId" in data:
        out["statistic_id"] = data["StatisticId"]
    if "MetricValues" in data:
        import aws_sdk_glue.types.data_quality_metric_values

        out["metric_values"] = (
            aws_sdk_glue.types.data_quality_metric_values.deserialize_aws_json_1_1(
                data["MetricValues"]
            )
        )
    if "NewRules" in data:
        import aws_sdk_glue.types.new_rules

        out["new_rules"] = aws_sdk_glue.types.new_rules.deserialize_aws_json_1_1(
            data["NewRules"]
        )
    return out
