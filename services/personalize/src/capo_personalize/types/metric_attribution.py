"""Generated from Smithy shape ``com.amazonaws.personalize#MetricAttribution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.date
    import capo_personalize.types.failure_reason
    import capo_personalize.types.metric_attribution_output
    import capo_personalize.types.name
    import capo_personalize.types.status


class MetricAttribution(TypedDict, closed=True):
    name: NotRequired["capo_personalize.types.name.Name"]
    """<p>The metric attribution's name.</p>"""
    metric_attribution_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The metric attribution's Amazon Resource Name (ARN).</p>"""
    dataset_group_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The metric attribution's dataset group Amazon Resource Name (ARN).</p>"""
    metrics_output_config: NotRequired[
        "capo_personalize.types.metric_attribution_output.MetricAttributionOutput"
    ]
    """<p>The metric attribution's output configuration.</p>"""
    status: NotRequired["capo_personalize.types.status.Status"]
    """<p>The metric attribution's status.</p>"""
    creation_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The metric attribution's creation date time.</p>"""
    last_updated_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The metric attribution's last updated date time.</p>"""
    failure_reason: NotRequired["capo_personalize.types.failure_reason.FailureReason"]
    """<p>The metric attribution's failure reason.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricAttribution) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "metric_attribution_arn" in value:
        out["metricAttributionArn"] = value["metric_attribution_arn"]
    if "dataset_group_arn" in value:
        out["datasetGroupArn"] = value["dataset_group_arn"]
    if "metrics_output_config" in value:
        import capo_personalize.types.metric_attribution_output

        out["metricsOutputConfig"] = (
            capo_personalize.types.metric_attribution_output.serialize_aws_json_1_1(
                value["metrics_output_config"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "creation_date_time" in value:
        import capo_personalize.types.date

        out["creationDateTime"] = capo_personalize.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import capo_personalize.types.date

        out["lastUpdatedDateTime"] = capo_personalize.types.date.serialize_aws_json_1_1(
            value["last_updated_date_time"]
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricAttribution:
    out: MetricAttribution = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "metricAttributionArn" in data:
        out["metric_attribution_arn"] = data["metricAttributionArn"]
    if "datasetGroupArn" in data:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    if "metricsOutputConfig" in data:
        import capo_personalize.types.metric_attribution_output

        out["metrics_output_config"] = (
            capo_personalize.types.metric_attribution_output.deserialize_aws_json_1_1(
                data["metricsOutputConfig"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    if "creationDateTime" in data:
        import capo_personalize.types.date

        out["creation_date_time"] = (
            capo_personalize.types.date.deserialize_aws_json_1_1(
                data["creationDateTime"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import capo_personalize.types.date

        out["last_updated_date_time"] = (
            capo_personalize.types.date.deserialize_aws_json_1_1(
                data["lastUpdatedDateTime"]
            )
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    return out
