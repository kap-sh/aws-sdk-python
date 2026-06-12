"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSDatabaseProjectedMetric``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.metric_values
    import aws_sdk_compute_optimizer.types.rdsdb_metric_name
    import aws_sdk_compute_optimizer.types.timestamps


class RDSDatabaseProjectedMetric(TypedDict):
    name: NotRequired[
        "aws_sdk_compute_optimizer.types.rdsdb_metric_name.RDSDBMetricName"
    ]
    """<p> The name of the projected metric. </p>"""
    timestamps: NotRequired["aws_sdk_compute_optimizer.types.timestamps.Timestamps"]
    """<p> The timestamps of the projected metric. </p>"""
    values: NotRequired["aws_sdk_compute_optimizer.types.metric_values.MetricValues"]
    """<p> The values for the projected metric. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSDatabaseProjectedMetric) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_compute_optimizer.types.rdsdb_metric_name

        out["name"] = (
            aws_sdk_compute_optimizer.types.rdsdb_metric_name.serialize_aws_json_1_0(
                value["name"]
            )
        )
    if "timestamps" in value:
        import aws_sdk_compute_optimizer.types.timestamps

        out["timestamps"] = (
            aws_sdk_compute_optimizer.types.timestamps.serialize_aws_json_1_0(
                value["timestamps"]
            )
        )
    if "values" in value:
        import aws_sdk_compute_optimizer.types.metric_values

        out["values"] = (
            aws_sdk_compute_optimizer.types.metric_values.serialize_aws_json_1_0(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RDSDatabaseProjectedMetric:
    out: RDSDatabaseProjectedMetric = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_compute_optimizer.types.rdsdb_metric_name

        out["name"] = (
            aws_sdk_compute_optimizer.types.rdsdb_metric_name.deserialize_aws_json_1_0(
                data["name"]
            )
        )
    if "timestamps" in data:
        import aws_sdk_compute_optimizer.types.timestamps

        out["timestamps"] = (
            aws_sdk_compute_optimizer.types.timestamps.deserialize_aws_json_1_0(
                data["timestamps"]
            )
        )
    if "values" in data:
        import aws_sdk_compute_optimizer.types.metric_values

        out["values"] = (
            aws_sdk_compute_optimizer.types.metric_values.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    return out
