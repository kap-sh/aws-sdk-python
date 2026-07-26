"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeClusterSchedulerConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_arn
    import capo_sagemaker.types.cluster_scheduler_config_arn
    import capo_sagemaker.types.cluster_scheduler_config_id
    import capo_sagemaker.types.entity_description
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.integer
    import capo_sagemaker.types.scheduler_config
    import capo_sagemaker.types.scheduler_resource_status
    import capo_sagemaker.types.status_details_map
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.user_context


class DescribeClusterSchedulerConfigResponse(TypedDict, closed=True):
    cluster_scheduler_config_arn: NotRequired[
        "capo_sagemaker.types.cluster_scheduler_config_arn.ClusterSchedulerConfigArn"
    ]
    """<p>ARN of the cluster policy.</p>"""
    cluster_scheduler_config_id: NotRequired[
        "capo_sagemaker.types.cluster_scheduler_config_id.ClusterSchedulerConfigId"
    ]
    """<p>ID of the cluster policy.</p>"""
    name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>Name of the cluster policy.</p>"""
    cluster_scheduler_config_version: NotRequired[
        "capo_sagemaker.types.integer.Integer"
    ]
    """<p>Version of the cluster policy.</p>"""
    status: NotRequired[
        "capo_sagemaker.types.scheduler_resource_status.SchedulerResourceStatus"
    ]
    """<p>Status of the cluster policy.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>Failure reason of the cluster policy.</p>"""
    status_details: NotRequired[
        "capo_sagemaker.types.status_details_map.StatusDetailsMap"
    ]
    """<p>Additional details about the status of the cluster policy. This field provides context when the policy is in a non-active state, such as during creation, updates, or if failures occur.</p>"""
    cluster_arn: NotRequired["capo_sagemaker.types.cluster_arn.ClusterArn"]
    """<p>ARN of the cluster where the cluster policy is applied.</p>"""
    scheduler_config: NotRequired[
        "capo_sagemaker.types.scheduler_config.SchedulerConfig"
    ]
    """<p>Cluster policy configuration. This policy is used for task prioritization and fair-share allocation. This helps prioritize critical workloads and distributes idle compute across entities.</p>"""
    description: NotRequired[
        "capo_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>Description of the cluster policy.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Creation time of the cluster policy.</p>"""
    created_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Last modified time of the cluster policy.</p>"""
    last_modified_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClusterSchedulerConfigResponse) -> dict:
    out: dict = {}
    if "cluster_scheduler_config_arn" in value:
        out["ClusterSchedulerConfigArn"] = value["cluster_scheduler_config_arn"]
    if "cluster_scheduler_config_id" in value:
        out["ClusterSchedulerConfigId"] = value["cluster_scheduler_config_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "cluster_scheduler_config_version" in value:
        out["ClusterSchedulerConfigVersion"] = value["cluster_scheduler_config_version"]
    if "status" in value:
        import capo_sagemaker.types.scheduler_resource_status

        out["Status"] = (
            capo_sagemaker.types.scheduler_resource_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "status_details" in value:
        import capo_sagemaker.types.status_details_map

        out["StatusDetails"] = (
            capo_sagemaker.types.status_details_map.serialize_aws_json_1_1(
                value["status_details"]
            )
        )
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "scheduler_config" in value:
        import capo_sagemaker.types.scheduler_config

        out["SchedulerConfig"] = (
            capo_sagemaker.types.scheduler_config.serialize_aws_json_1_1(
                value["scheduler_config"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "created_by" in value:
        import capo_sagemaker.types.user_context

        out["CreatedBy"] = capo_sagemaker.types.user_context.serialize_aws_json_1_1(
            value["created_by"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "last_modified_by" in value:
        import capo_sagemaker.types.user_context

        out["LastModifiedBy"] = (
            capo_sagemaker.types.user_context.serialize_aws_json_1_1(
                value["last_modified_by"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClusterSchedulerConfigResponse:
    out: DescribeClusterSchedulerConfigResponse = {}  # type: ignore[typeddict-item]
    if "ClusterSchedulerConfigArn" in data:
        out["cluster_scheduler_config_arn"] = data["ClusterSchedulerConfigArn"]
    if "ClusterSchedulerConfigId" in data:
        out["cluster_scheduler_config_id"] = data["ClusterSchedulerConfigId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ClusterSchedulerConfigVersion" in data:
        out["cluster_scheduler_config_version"] = data["ClusterSchedulerConfigVersion"]
    if "Status" in data:
        import capo_sagemaker.types.scheduler_resource_status

        out["status"] = (
            capo_sagemaker.types.scheduler_resource_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "StatusDetails" in data:
        import capo_sagemaker.types.status_details_map

        out["status_details"] = (
            capo_sagemaker.types.status_details_map.deserialize_aws_json_1_1(
                data["StatusDetails"]
            )
        )
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    if "SchedulerConfig" in data:
        import capo_sagemaker.types.scheduler_config

        out["scheduler_config"] = (
            capo_sagemaker.types.scheduler_config.deserialize_aws_json_1_1(
                data["SchedulerConfig"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "CreatedBy" in data:
        import capo_sagemaker.types.user_context

        out["created_by"] = capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
            data["CreatedBy"]
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "LastModifiedBy" in data:
        import capo_sagemaker.types.user_context

        out["last_modified_by"] = (
            capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["LastModifiedBy"]
            )
        )
    return out
