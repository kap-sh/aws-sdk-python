"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringJobDefinitionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint_name
    import capo_sagemaker.types.monitoring_job_definition_arn
    import capo_sagemaker.types.monitoring_job_definition_name
    import capo_sagemaker.types.timestamp


class MonitoringJobDefinitionSummary(TypedDict, closed=True):
    monitoring_job_definition_name: NotRequired[
        "capo_sagemaker.types.monitoring_job_definition_name.MonitoringJobDefinitionName"
    ]
    """<p>The name of the monitoring job.</p>"""
    monitoring_job_definition_arn: NotRequired[
        "capo_sagemaker.types.monitoring_job_definition_arn.MonitoringJobDefinitionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the monitoring job.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time that the monitoring job was created.</p>"""
    endpoint_name: NotRequired["capo_sagemaker.types.endpoint_name.EndpointName"]
    """<p>The name of the endpoint that the job monitors.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringJobDefinitionSummary) -> dict:
    out: dict = {}
    if "monitoring_job_definition_name" in value:
        out["MonitoringJobDefinitionName"] = value["monitoring_job_definition_name"]
    if "monitoring_job_definition_arn" in value:
        out["MonitoringJobDefinitionArn"] = value["monitoring_job_definition_arn"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringJobDefinitionSummary:
    out: MonitoringJobDefinitionSummary = {}  # type: ignore[typeddict-item]
    if "MonitoringJobDefinitionName" in data:
        out["monitoring_job_definition_name"] = data["MonitoringJobDefinitionName"]
    if "MonitoringJobDefinitionArn" in data:
        out["monitoring_job_definition_arn"] = data["MonitoringJobDefinitionArn"]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "EndpointName" in data:
        out["endpoint_name"] = data["EndpointName"]
    return out
