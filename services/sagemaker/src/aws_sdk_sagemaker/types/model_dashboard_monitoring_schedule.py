"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelDashboardMonitoringSchedule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.batch_transform_input
    import aws_sdk_sagemaker.types.endpoint_name
    import aws_sdk_sagemaker.types.failure_reason
    import aws_sdk_sagemaker.types.monitoring_alert_summary_list
    import aws_sdk_sagemaker.types.monitoring_execution_summary
    import aws_sdk_sagemaker.types.monitoring_schedule_arn
    import aws_sdk_sagemaker.types.monitoring_schedule_config
    import aws_sdk_sagemaker.types.monitoring_schedule_name
    import aws_sdk_sagemaker.types.monitoring_type
    import aws_sdk_sagemaker.types.schedule_status
    import aws_sdk_sagemaker.types.timestamp


class ModelDashboardMonitoringSchedule(TypedDict):
    monitoring_schedule_arn: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_schedule_arn.MonitoringScheduleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a monitoring schedule.</p>"""
    monitoring_schedule_name: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_schedule_name.MonitoringScheduleName"
    ]
    """<p>The name of a monitoring schedule.</p>"""
    monitoring_schedule_status: NotRequired[
        "aws_sdk_sagemaker.types.schedule_status.ScheduleStatus"
    ]
    """<p>The status of the monitoring schedule.</p>"""
    monitoring_type: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_type.MonitoringType"
    ]
    """<p>The monitor type of a model monitor.</p>"""
    failure_reason: NotRequired["aws_sdk_sagemaker.types.failure_reason.FailureReason"]
    """<p>If a monitoring job failed, provides the reason.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the monitoring schedule was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the monitoring schedule was last updated.</p>"""
    monitoring_schedule_config: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_schedule_config.MonitoringScheduleConfig"
    ]
    endpoint_name: NotRequired["aws_sdk_sagemaker.types.endpoint_name.EndpointName"]
    """<p>The endpoint which is monitored.</p>"""
    monitoring_alert_summaries: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_alert_summary_list.MonitoringAlertSummaryList"
    ]
    """<p>A JSON array where each element is a summary for a monitoring alert.</p>"""
    last_monitoring_execution_summary: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_execution_summary.MonitoringExecutionSummary"
    ]
    batch_transform_input: NotRequired[
        "aws_sdk_sagemaker.types.batch_transform_input.BatchTransformInput"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelDashboardMonitoringSchedule) -> dict:
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
    if "monitoring_alert_summaries" in value:
        import aws_sdk_sagemaker.types.monitoring_alert_summary_list

        out["MonitoringAlertSummaries"] = (
            aws_sdk_sagemaker.types.monitoring_alert_summary_list.serialize_aws_json_1_1(
                value["monitoring_alert_summaries"]
            )
        )
    if "last_monitoring_execution_summary" in value:
        import aws_sdk_sagemaker.types.monitoring_execution_summary

        out["LastMonitoringExecutionSummary"] = (
            aws_sdk_sagemaker.types.monitoring_execution_summary.serialize_aws_json_1_1(
                value["last_monitoring_execution_summary"]
            )
        )
    if "batch_transform_input" in value:
        import aws_sdk_sagemaker.types.batch_transform_input

        out["BatchTransformInput"] = (
            aws_sdk_sagemaker.types.batch_transform_input.serialize_aws_json_1_1(
                value["batch_transform_input"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelDashboardMonitoringSchedule:
    out: ModelDashboardMonitoringSchedule = {}  # type: ignore[typeddict-item]
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
    if "MonitoringAlertSummaries" in data:
        import aws_sdk_sagemaker.types.monitoring_alert_summary_list

        out["monitoring_alert_summaries"] = (
            aws_sdk_sagemaker.types.monitoring_alert_summary_list.deserialize_aws_json_1_1(
                data["MonitoringAlertSummaries"]
            )
        )
    if "LastMonitoringExecutionSummary" in data:
        import aws_sdk_sagemaker.types.monitoring_execution_summary

        out["last_monitoring_execution_summary"] = (
            aws_sdk_sagemaker.types.monitoring_execution_summary.deserialize_aws_json_1_1(
                data["LastMonitoringExecutionSummary"]
            )
        )
    if "BatchTransformInput" in data:
        import aws_sdk_sagemaker.types.batch_transform_input

        out["batch_transform_input"] = (
            aws_sdk_sagemaker.types.batch_transform_input.deserialize_aws_json_1_1(
                data["BatchTransformInput"]
            )
        )
    return out
