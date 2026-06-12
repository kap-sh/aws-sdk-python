"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterSchedulerConfigSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_arn
    import aws_sdk_sagemaker.types.cluster_scheduler_config_arn
    import aws_sdk_sagemaker.types.cluster_scheduler_config_id
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.integer
    import aws_sdk_sagemaker.types.scheduler_resource_status
    import aws_sdk_sagemaker.types.timestamp


class ClusterSchedulerConfigSummary(TypedDict):
    cluster_scheduler_config_arn: NotRequired[
        "aws_sdk_sagemaker.types.cluster_scheduler_config_arn.ClusterSchedulerConfigArn"
    ]
    """<p>ARN of the cluster policy.</p>"""
    cluster_scheduler_config_id: NotRequired[
        "aws_sdk_sagemaker.types.cluster_scheduler_config_id.ClusterSchedulerConfigId"
    ]
    """<p>ID of the cluster policy.</p>"""
    cluster_scheduler_config_version: NotRequired[
        "aws_sdk_sagemaker.types.integer.Integer"
    ]
    """<p>Version of the cluster policy.</p>"""
    name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>Name of the cluster policy.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Creation time of the cluster policy.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Last modified time of the cluster policy.</p>"""
    status: NotRequired[
        "aws_sdk_sagemaker.types.scheduler_resource_status.SchedulerResourceStatus"
    ]
    """<p>Status of the cluster policy.</p>"""
    cluster_arn: NotRequired["aws_sdk_sagemaker.types.cluster_arn.ClusterArn"]
    """<p>ARN of the cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterSchedulerConfigSummary) -> dict:
    out: dict = {}
    if "cluster_scheduler_config_arn" in value:
        out["ClusterSchedulerConfigArn"] = value["cluster_scheduler_config_arn"]
    if "cluster_scheduler_config_id" in value:
        out["ClusterSchedulerConfigId"] = value["cluster_scheduler_config_id"]
    if "cluster_scheduler_config_version" in value:
        out["ClusterSchedulerConfigVersion"] = value["cluster_scheduler_config_version"]
    if "name" in value:
        out["Name"] = value["name"]
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
    if "status" in value:
        import aws_sdk_sagemaker.types.scheduler_resource_status

        out["Status"] = (
            aws_sdk_sagemaker.types.scheduler_resource_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterSchedulerConfigSummary:
    out: ClusterSchedulerConfigSummary = {}  # type: ignore[typeddict-item]
    if "ClusterSchedulerConfigArn" in data:
        out["cluster_scheduler_config_arn"] = data["ClusterSchedulerConfigArn"]
    if "ClusterSchedulerConfigId" in data:
        out["cluster_scheduler_config_id"] = data["ClusterSchedulerConfigId"]
    if "ClusterSchedulerConfigVersion" in data:
        out["cluster_scheduler_config_version"] = data["ClusterSchedulerConfigVersion"]
    if "Name" in data:
        out["name"] = data["Name"]
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
    if "Status" in data:
        import aws_sdk_sagemaker.types.scheduler_resource_status

        out["status"] = (
            aws_sdk_sagemaker.types.scheduler_resource_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    return out
