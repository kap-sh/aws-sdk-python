"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringExecutionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint_name
    import capo_sagemaker.types.execution_status
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.monitoring_job_definition_name
    import capo_sagemaker.types.monitoring_schedule_name
    import capo_sagemaker.types.monitoring_type
    import capo_sagemaker.types.processing_job_arn
    import capo_sagemaker.types.timestamp


class MonitoringExecutionSummary(TypedDict, closed=True):
    monitoring_schedule_name: NotRequired[
        "capo_sagemaker.types.monitoring_schedule_name.MonitoringScheduleName"
    ]
    """<p>The name of the monitoring schedule.</p>"""
    scheduled_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time the monitoring job was scheduled.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time at which the monitoring job was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates the last time the monitoring job was modified.</p>"""
    monitoring_execution_status: NotRequired[
        "capo_sagemaker.types.execution_status.ExecutionStatus"
    ]
    """<p>The status of the monitoring job.</p>"""
    processing_job_arn: NotRequired[
        "capo_sagemaker.types.processing_job_arn.ProcessingJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the monitoring job.</p>"""
    endpoint_name: NotRequired["capo_sagemaker.types.endpoint_name.EndpointName"]
    """<p>The name of the endpoint used to run the monitoring job.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>Contains the reason a monitoring job failed, if it failed.</p>"""
    monitoring_job_definition_name: NotRequired[
        "capo_sagemaker.types.monitoring_job_definition_name.MonitoringJobDefinitionName"
    ]
    """<p>The name of the monitoring job.</p>"""
    monitoring_type: NotRequired["capo_sagemaker.types.monitoring_type.MonitoringType"]
    """<p>The type of the monitoring job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringExecutionSummary) -> dict:
    out: dict = {}
    if "monitoring_schedule_name" in value:
        out["MonitoringScheduleName"] = value["monitoring_schedule_name"]
    if "scheduled_time" in value:
        import capo_sagemaker.types.timestamp

        out["ScheduledTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["scheduled_time"]
        )
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
    if "monitoring_execution_status" in value:
        import capo_sagemaker.types.execution_status

        out["MonitoringExecutionStatus"] = (
            capo_sagemaker.types.execution_status.serialize_aws_json_1_1(
                value["monitoring_execution_status"]
            )
        )
    if "processing_job_arn" in value:
        out["ProcessingJobArn"] = value["processing_job_arn"]
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "monitoring_job_definition_name" in value:
        out["MonitoringJobDefinitionName"] = value["monitoring_job_definition_name"]
    if "monitoring_type" in value:
        import capo_sagemaker.types.monitoring_type

        out["MonitoringType"] = (
            capo_sagemaker.types.monitoring_type.serialize_aws_json_1_1(
                value["monitoring_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringExecutionSummary:
    out: MonitoringExecutionSummary = {}  # type: ignore[typeddict-item]
    if "MonitoringScheduleName" in data:
        out["monitoring_schedule_name"] = data["MonitoringScheduleName"]
    if "ScheduledTime" in data:
        import capo_sagemaker.types.timestamp

        out["scheduled_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["ScheduledTime"]
        )
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
    if "MonitoringExecutionStatus" in data:
        import capo_sagemaker.types.execution_status

        out["monitoring_execution_status"] = (
            capo_sagemaker.types.execution_status.deserialize_aws_json_1_1(
                data["MonitoringExecutionStatus"]
            )
        )
    if "ProcessingJobArn" in data:
        out["processing_job_arn"] = data["ProcessingJobArn"]
    if "EndpointName" in data:
        out["endpoint_name"] = data["EndpointName"]
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "MonitoringJobDefinitionName" in data:
        out["monitoring_job_definition_name"] = data["MonitoringJobDefinitionName"]
    if "MonitoringType" in data:
        import capo_sagemaker.types.monitoring_type

        out["monitoring_type"] = (
            capo_sagemaker.types.monitoring_type.deserialize_aws_json_1_1(
                data["MonitoringType"]
            )
        )
    return out
