"""Generated from Smithy shape ``com.amazonaws.lightsail#GetRelationalDatabaseMetricDataResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.metric_datapoint_list
    import capo_lightsail.types.relational_database_metric_name


class GetRelationalDatabaseMetricDataResult(TypedDict, closed=True):
    metric_name: NotRequired[
        "capo_lightsail.types.relational_database_metric_name.RelationalDatabaseMetricName"
    ]
    """<p>The name of the metric returned.</p>"""
    metric_data: NotRequired[
        "capo_lightsail.types.metric_datapoint_list.MetricDatapointList"
    ]
    """<p>An array of objects that describe the metric data returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRelationalDatabaseMetricDataResult) -> dict:
    out: dict = {}
    if "metric_name" in value:
        import capo_lightsail.types.relational_database_metric_name

        out["metricName"] = (
            capo_lightsail.types.relational_database_metric_name.serialize_aws_json_1_1(
                value["metric_name"]
            )
        )
    if "metric_data" in value:
        import capo_lightsail.types.metric_datapoint_list

        out["metricData"] = (
            capo_lightsail.types.metric_datapoint_list.serialize_aws_json_1_1(
                value["metric_data"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRelationalDatabaseMetricDataResult:
    out: GetRelationalDatabaseMetricDataResult = {}  # type: ignore[typeddict-item]
    if "metricName" in data:
        import capo_lightsail.types.relational_database_metric_name

        out["metric_name"] = (
            capo_lightsail.types.relational_database_metric_name.deserialize_aws_json_1_1(
                data["metricName"]
            )
        )
    if "metricData" in data:
        import capo_lightsail.types.metric_datapoint_list

        out["metric_data"] = (
            capo_lightsail.types.metric_datapoint_list.deserialize_aws_json_1_1(
                data["metricData"]
            )
        )
    return out
