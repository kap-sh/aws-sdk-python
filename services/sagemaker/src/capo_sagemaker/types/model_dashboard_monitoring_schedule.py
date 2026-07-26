"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelDashboardMonitoringSchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.batch_transform_input
    import capo_sagemaker.types.endpoint_name
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.monitoring_alert_summary_list
    import capo_sagemaker.types.monitoring_execution_summary
    import capo_sagemaker.types.monitoring_schedule_arn
    import capo_sagemaker.types.monitoring_schedule_config
    import capo_sagemaker.types.monitoring_schedule_name
    import capo_sagemaker.types.monitoring_type
    import capo_sagemaker.types.schedule_status
    import capo_sagemaker.types.timestamp


class ModelDashboardMonitoringSchedule(TypedDict, closed=True):
    monitoring_schedule_arn: NotRequired[
        "capo_sagemaker.types.monitoring_schedule_arn.MonitoringScheduleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a monitoring schedule.</p>"""
    monitoring_schedule_name: NotRequired[
        "capo_sagemaker.types.monitoring_schedule_name.MonitoringScheduleName"
    ]
    """<p>The name of a monitoring schedule.</p>"""
    monitoring_schedule_status: NotRequired[
        "capo_sagemaker.types.schedule_status.ScheduleStatus"
    ]
    """<p>The status of the monitoring schedule.</p>"""
    monitoring_type: NotRequired["capo_sagemaker.types.monitoring_type.MonitoringType"]
    """<p>The monitor type of a model monitor.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>If a monitoring job failed, provides the reason.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the monitoring schedule was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the monitoring schedule was last updated.</p>"""
    monitoring_schedule_config: NotRequired[
        "capo_sagemaker.types.monitoring_schedule_config.MonitoringScheduleConfig"
    ]
    endpoint_name: NotRequired["capo_sagemaker.types.endpoint_name.EndpointName"]
    """<p>The endpoint which is monitored.</p>"""
    monitoring_alert_summaries: NotRequired[
        "capo_sagemaker.types.monitoring_alert_summary_list.MonitoringAlertSummaryList"
    ]
    """<p>A JSON array where each element is a summary for a monitoring alert.</p>"""
    last_monitoring_execution_summary: NotRequired[
        "capo_sagemaker.types.monitoring_execution_summary.MonitoringExecutionSummary"
    ]
    batch_transform_input: NotRequired[
        "capo_sagemaker.types.batch_transform_input.BatchTransformInput"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelDashboardMonitoringSchedule) -> dict:
    out: dict = {}
    if "monitoring_schedule_arn" in value:
        out["MonitoringScheduleArn"] = value["monitoring_schedule_arn"]
    if "monitoring_schedule_name" in value:
        out["MonitoringScheduleName"] = value["monitoring_schedule_name"]
    if "monitoring_schedule_status" in value:
        import capo_sagemaker.types.schedule_status

        out["MonitoringScheduleStatus"] = (
            capo_sagemaker.types.schedule_status.serialize_aws_json_1_1(
                value["monitoring_schedule_status"]
            )
        )
    if "monitoring_type" in value:
        import capo_sagemaker.types.monitoring_type

        out["MonitoringType"] = (
            capo_sagemaker.types.monitoring_type.serialize_aws_json_1_1(
                value["monitoring_type"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "monitoring_schedule_config" in value:
        import capo_sagemaker.types.monitoring_schedule_config

        out["MonitoringScheduleConfig"] = (
            capo_sagemaker.types.monitoring_schedule_config.serialize_aws_json_1_1(
                value["monitoring_schedule_config"]
            )
        )
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "monitoring_alert_summaries" in value:
        import capo_sagemaker.types.monitoring_alert_summary_list

        out["MonitoringAlertSummaries"] = (
            capo_sagemaker.types.monitoring_alert_summary_list.serialize_aws_json_1_1(
                value["monitoring_alert_summaries"]
            )
        )
    if "last_monitoring_execution_summary" in value:
        import capo_sagemaker.types.monitoring_execution_summary

        out["LastMonitoringExecutionSummary"] = (
            capo_sagemaker.types.monitoring_execution_summary.serialize_aws_json_1_1(
                value["last_monitoring_execution_summary"]
            )
        )
    if "batch_transform_input" in value:
        import capo_sagemaker.types.batch_transform_input

        out["BatchTransformInput"] = (
            capo_sagemaker.types.batch_transform_input.serialize_aws_json_1_1(
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
        import capo_sagemaker.types.schedule_status

        out["monitoring_schedule_status"] = (
            capo_sagemaker.types.schedule_status.deserialize_aws_json_1_1(
                data["MonitoringScheduleStatus"]
            )
        )
    if "MonitoringType" in data:
        import capo_sagemaker.types.monitoring_type

        out["monitoring_type"] = (
            capo_sagemaker.types.monitoring_type.deserialize_aws_json_1_1(
                data["MonitoringType"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "MonitoringScheduleConfig" in data:
        import capo_sagemaker.types.monitoring_schedule_config

        out["monitoring_schedule_config"] = (
            capo_sagemaker.types.monitoring_schedule_config.deserialize_aws_json_1_1(
                data["MonitoringScheduleConfig"]
            )
        )
    if "EndpointName" in data:
        out["endpoint_name"] = data["EndpointName"]
    if "MonitoringAlertSummaries" in data:
        import capo_sagemaker.types.monitoring_alert_summary_list

        out["monitoring_alert_summaries"] = (
            capo_sagemaker.types.monitoring_alert_summary_list.deserialize_aws_json_1_1(
                data["MonitoringAlertSummaries"]
            )
        )
    if "LastMonitoringExecutionSummary" in data:
        import capo_sagemaker.types.monitoring_execution_summary

        out["last_monitoring_execution_summary"] = (
            capo_sagemaker.types.monitoring_execution_summary.deserialize_aws_json_1_1(
                data["LastMonitoringExecutionSummary"]
            )
        )
    if "BatchTransformInput" in data:
        import capo_sagemaker.types.batch_transform_input

        out["batch_transform_input"] = (
            capo_sagemaker.types.batch_transform_input.deserialize_aws_json_1_1(
                data["BatchTransformInput"]
            )
        )
    return out
