"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeMonitoringScheduleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.endpoint_name
    import aws_sdk_sagemaker.types.failure_reason
    import aws_sdk_sagemaker.types.monitoring_execution_summary
    import aws_sdk_sagemaker.types.monitoring_schedule_arn
    import aws_sdk_sagemaker.types.monitoring_schedule_config
    import aws_sdk_sagemaker.types.monitoring_schedule_name
    import aws_sdk_sagemaker.types.monitoring_type
    import aws_sdk_sagemaker.types.schedule_status
    import aws_sdk_sagemaker.types.timestamp


class DescribeMonitoringScheduleResponse(TypedDict):
    monitoring_schedule_arn: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_schedule_arn.MonitoringScheduleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the monitoring schedule.</p>"""
    monitoring_schedule_name: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_schedule_name.MonitoringScheduleName"
    ]
    """<p>Name of the monitoring schedule.</p>"""
    monitoring_schedule_status: NotRequired[
        "aws_sdk_sagemaker.types.schedule_status.ScheduleStatus"
    ]
    """<p>The status of an monitoring job.</p>"""
    monitoring_type: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_type.MonitoringType"
    ]
    """<p>The type of the monitoring job that this schedule runs. This is one of the following values.</p> <ul> <li> <p> <code>DATA_QUALITY</code> - The schedule is for a data quality monitoring job.</p> </li> <li> <p> <code>MODEL_QUALITY</code> - The schedule is for a model quality monitoring job.</p> </li> <li> <p> <code>MODEL_BIAS</code> - The schedule is for a bias monitoring job.</p> </li> <li> <p> <code>MODEL_EXPLAINABILITY</code> - The schedule is for an explainability monitoring job.</p> </li> </ul>"""
    failure_reason: NotRequired["aws_sdk_sagemaker.types.failure_reason.FailureReason"]
    """<p>A string, up to one KB in size, that contains the reason a monitoring job failed, if it failed.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The time at which the monitoring job was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The time at which the monitoring job was last modified.</p>"""
    monitoring_schedule_config: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_schedule_config.MonitoringScheduleConfig"
    ]
    """<p>The configuration object that specifies the monitoring schedule and defines the monitoring job.</p>"""
    endpoint_name: NotRequired["aws_sdk_sagemaker.types.endpoint_name.EndpointName"]
    """<p> The name of the endpoint for the monitoring job.</p>"""
    last_monitoring_execution_summary: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_execution_summary.MonitoringExecutionSummary"
    ]
    """<p>Describes metadata on the last execution to run, if there was one.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMonitoringScheduleResponse) -> dict:
    out: dict = {}
    if "monitoring_schedule_arn" in value:
        out["MonitoringScheduleArn"] = value["monitoring_schedule_arn"]
    if "monitoring_schedule_name" in value:
        out["MonitoringScheduleName"] = value["monitoring_schedule_name"]
    if "monitoring_schedule_status" in value:
        import aws_sdk_sagemaker.types.schedule_status

        out["MonitoringScheduleStatus"] = (
            aws_sdk_sagemaker.types.schedule_status.serialize_aws_json_1_1(
                value["monitoring_schedule_status"]
            )
        )
    if "monitoring_type" in value:
        import aws_sdk_sagemaker.types.monitoring_type

        out["MonitoringType"] = (
            aws_sdk_sagemaker.types.monitoring_type.serialize_aws_json_1_1(
                value["monitoring_type"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "monitoring_schedule_config" in value:
        import aws_sdk_sagemaker.types.monitoring_schedule_config

        out["MonitoringScheduleConfig"] = (
            aws_sdk_sagemaker.types.monitoring_schedule_config.serialize_aws_json_1_1(
                value["monitoring_schedule_config"]
            )
        )
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "last_monitoring_execution_summary" in value:
        import aws_sdk_sagemaker.types.monitoring_execution_summary

        out["LastMonitoringExecutionSummary"] = (
            aws_sdk_sagemaker.types.monitoring_execution_summary.serialize_aws_json_1_1(
                value["last_monitoring_execution_summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMonitoringScheduleResponse:
    out: DescribeMonitoringScheduleResponse = {}  # type: ignore[typeddict-item]
    if "MonitoringScheduleArn" in data:
        out["monitoring_schedule_arn"] = data["MonitoringScheduleArn"]
    if "MonitoringScheduleName" in data:
        out["monitoring_schedule_name"] = data["MonitoringScheduleName"]
    if "MonitoringScheduleStatus" in data:
        import aws_sdk_sagemaker.types.schedule_status

        out["monitoring_schedule_status"] = (
            aws_sdk_sagemaker.types.schedule_status.deserialize_aws_json_1_1(
                data["MonitoringScheduleStatus"]
            )
        )
    if "MonitoringType" in data:
        import aws_sdk_sagemaker.types.monitoring_type

        out["monitoring_type"] = (
            aws_sdk_sagemaker.types.monitoring_type.deserialize_aws_json_1_1(
                data["MonitoringType"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "MonitoringScheduleConfig" in data:
        import aws_sdk_sagemaker.types.monitoring_schedule_config

        out["monitoring_schedule_config"] = (
            aws_sdk_sagemaker.types.monitoring_schedule_config.deserialize_aws_json_1_1(
                data["MonitoringScheduleConfig"]
            )
        )
    if "EndpointName" in data:
        out["endpoint_name"] = data["EndpointName"]
    if "LastMonitoringExecutionSummary" in data:
        import aws_sdk_sagemaker.types.monitoring_execution_summary

        out["last_monitoring_execution_summary"] = (
            aws_sdk_sagemaker.types.monitoring_execution_summary.deserialize_aws_json_1_1(
                data["LastMonitoringExecutionSummary"]
            )
        )
    return out
