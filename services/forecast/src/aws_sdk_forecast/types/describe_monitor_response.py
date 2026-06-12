"""Generated from Smithy shape ``com.amazonaws.forecast#DescribeMonitorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn
    import aws_sdk_forecast.types.baseline
    import aws_sdk_forecast.types.evaluation_state
    import aws_sdk_forecast.types.long
    import aws_sdk_forecast.types.message
    import aws_sdk_forecast.types.name
    import aws_sdk_forecast.types.status
    import aws_sdk_forecast.types.timestamp


class DescribeMonitorResponse(TypedDict):
    monitor_name: NotRequired["aws_sdk_forecast.types.name.Name"]
    """<p>The name of the monitor.</p>"""
    monitor_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the monitor resource described.</p>"""
    resource_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the auto predictor being monitored.</p>"""
    status: NotRequired["aws_sdk_forecast.types.status.Status"]
    """<p>The status of the monitor resource.</p>"""
    last_evaluation_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>The timestamp of the latest evaluation completed by the monitor.</p>"""
    last_evaluation_state: NotRequired[
        "aws_sdk_forecast.types.evaluation_state.EvaluationState"
    ]
    """<p>The state of the monitor's latest evaluation.</p>"""
    baseline: NotRequired["aws_sdk_forecast.types.baseline.Baseline"]
    """<p>Metrics you can use as a baseline for comparison purposes. Use these values you interpret monitoring results for an auto predictor.</p>"""
    message: NotRequired["aws_sdk_forecast.types.message.Message"]
    """<p>An error message, if any, for the monitor.</p>"""
    creation_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>The timestamp for when the monitor resource was created.</p>"""
    last_modification_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>The timestamp of the latest modification to the monitor.</p>"""
    estimated_evaluation_time_remaining_in_minutes: NotRequired[
        "aws_sdk_forecast.types.long.Long"
    ]
    """<p>The estimated number of minutes remaining before the monitor resource finishes its current evaluation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMonitorResponse) -> dict:
    out: dict = {}
    if "monitor_name" in value:
        out["MonitorName"] = value["monitor_name"]
    if "monitor_arn" in value:
        out["MonitorArn"] = value["monitor_arn"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "status" in value:
        out["Status"] = value["status"]
    if "last_evaluation_time" in value:
        import aws_sdk_forecast.types.timestamp

        out["LastEvaluationTime"] = (
            aws_sdk_forecast.types.timestamp.serialize_aws_json_1_1(
                value["last_evaluation_time"]
            )
        )
    if "last_evaluation_state" in value:
        out["LastEvaluationState"] = value["last_evaluation_state"]
    if "baseline" in value:
        import aws_sdk_forecast.types.baseline

        out["Baseline"] = aws_sdk_forecast.types.baseline.serialize_aws_json_1_1(
            value["baseline"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "creation_time" in value:
        import aws_sdk_forecast.types.timestamp

        out["CreationTime"] = aws_sdk_forecast.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modification_time" in value:
        import aws_sdk_forecast.types.timestamp

        out["LastModificationTime"] = (
            aws_sdk_forecast.types.timestamp.serialize_aws_json_1_1(
                value["last_modification_time"]
            )
        )
    if "estimated_evaluation_time_remaining_in_minutes" in value:
        out["EstimatedEvaluationTimeRemainingInMinutes"] = value[
            "estimated_evaluation_time_remaining_in_minutes"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMonitorResponse:
    out: DescribeMonitorResponse = {}  # type: ignore[typeddict-item]
    if "MonitorName" in data:
        out["monitor_name"] = data["MonitorName"]
    if "MonitorArn" in data:
        out["monitor_arn"] = data["MonitorArn"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "LastEvaluationTime" in data:
        import aws_sdk_forecast.types.timestamp

        out["last_evaluation_time"] = (
            aws_sdk_forecast.types.timestamp.deserialize_aws_json_1_1(
                data["LastEvaluationTime"]
            )
        )
    if "LastEvaluationState" in data:
        out["last_evaluation_state"] = data["LastEvaluationState"]
    if "Baseline" in data:
        import aws_sdk_forecast.types.baseline

        out["baseline"] = aws_sdk_forecast.types.baseline.deserialize_aws_json_1_1(
            data["Baseline"]
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "CreationTime" in data:
        import aws_sdk_forecast.types.timestamp

        out["creation_time"] = (
            aws_sdk_forecast.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModificationTime" in data:
        import aws_sdk_forecast.types.timestamp

        out["last_modification_time"] = (
            aws_sdk_forecast.types.timestamp.deserialize_aws_json_1_1(
                data["LastModificationTime"]
            )
        )
    if "EstimatedEvaluationTimeRemainingInMinutes" in data:
        out["estimated_evaluation_time_remaining_in_minutes"] = data[
            "EstimatedEvaluationTimeRemainingInMinutes"
        ]
    return out
