"""Generated from Smithy shape ``com.amazonaws.forecast#MonitorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn
    import aws_sdk_forecast.types.name
    import aws_sdk_forecast.types.status
    import aws_sdk_forecast.types.timestamp


class MonitorSummary(TypedDict, closed=True):
    monitor_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the monitor resource.</p>"""
    monitor_name: NotRequired["aws_sdk_forecast.types.name.Name"]
    """<p>The name of the monitor resource.</p>"""
    resource_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the predictor being monitored.</p>"""
    status: NotRequired["aws_sdk_forecast.types.status.Status"]
    """<p>The status of the monitor. States include:</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>ACTIVE_STOPPING</code>, <code>ACTIVE_STOPPED</code> </p> </li> <li> <p> <code>UPDATE_IN_PROGRESS</code> </p> </li> <li> <p> <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>CREATE_FAILED</code> </p> </li> <li> <p> <code>DELETE_PENDING</code>, <code>DELETE_IN_PROGRESS</code>, <code>DELETE_FAILED</code> </p> </li> </ul>"""
    creation_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>When the monitor resource was created.</p>"""
    last_modification_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>The last time the monitor resource was modified. The timestamp depends on the status of the job:</p> <ul> <li> <p> <code>CREATE_PENDING</code> - The <code>CreationTime</code>.</p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> - The current timestamp.</p> </li> <li> <p> <code>STOPPED</code> - When the resource stopped.</p> </li> <li> <p> <code>ACTIVE</code> or <code>CREATE_FAILED</code> - When the monitor creation finished or failed.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitorSummary) -> dict:
    out: dict = {}
    if "monitor_arn" in value:
        out["MonitorArn"] = value["monitor_arn"]
    if "monitor_name" in value:
        out["MonitorName"] = value["monitor_name"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "status" in value:
        out["Status"] = value["status"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitorSummary:
    out: MonitorSummary = {}  # type: ignore[typeddict-item]
    if "MonitorArn" in data:
        out["monitor_arn"] = data["MonitorArn"]
    if "MonitorName" in data:
        out["monitor_name"] = data["MonitorName"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "Status" in data:
        out["status"] = data["Status"]
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
    return out
