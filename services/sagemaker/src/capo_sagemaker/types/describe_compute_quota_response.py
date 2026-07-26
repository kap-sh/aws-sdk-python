"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeComputeQuotaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.activation_state
    import capo_sagemaker.types.cluster_arn
    import capo_sagemaker.types.compute_quota_arn
    import capo_sagemaker.types.compute_quota_config
    import capo_sagemaker.types.compute_quota_id
    import capo_sagemaker.types.compute_quota_target
    import capo_sagemaker.types.entity_description
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.integer
    import capo_sagemaker.types.scheduler_resource_status
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.user_context


class DescribeComputeQuotaResponse(TypedDict, closed=True):
    compute_quota_arn: NotRequired[
        "capo_sagemaker.types.compute_quota_arn.ComputeQuotaArn"
    ]
    """<p>ARN of the compute allocation definition.</p>"""
    compute_quota_id: NotRequired[
        "capo_sagemaker.types.compute_quota_id.ComputeQuotaId"
    ]
    """<p>ID of the compute allocation definition.</p>"""
    name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>Name of the compute allocation definition.</p>"""
    description: NotRequired[
        "capo_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>Description of the compute allocation definition.</p>"""
    compute_quota_version: NotRequired["capo_sagemaker.types.integer.Integer"]
    """<p>Version of the compute allocation definition.</p>"""
    status: NotRequired[
        "capo_sagemaker.types.scheduler_resource_status.SchedulerResourceStatus"
    ]
    """<p>Status of the compute allocation definition.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>Failure reason of the compute allocation definition.</p>"""
    cluster_arn: NotRequired["capo_sagemaker.types.cluster_arn.ClusterArn"]
    """<p>ARN of the cluster.</p>"""
    compute_quota_config: NotRequired[
        "capo_sagemaker.types.compute_quota_config.ComputeQuotaConfig"
    ]
    """<p>Configuration of the compute allocation definition. This includes the resource sharing option, and the setting to preempt low priority tasks.</p>"""
    compute_quota_target: NotRequired[
        "capo_sagemaker.types.compute_quota_target.ComputeQuotaTarget"
    ]
    """<p>The target entity to allocate compute resources to.</p>"""
    activation_state: NotRequired[
        "capo_sagemaker.types.activation_state.ActivationState"
    ]
    """<p>The state of the compute allocation being described. Use to enable or disable compute allocation.</p> <p>Default is <code>Enabled</code>.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Creation time of the compute allocation configuration.</p>"""
    created_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Last modified time of the compute allocation configuration.</p>"""
    last_modified_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeComputeQuotaResponse) -> dict:
    out: dict = {}
    if "compute_quota_arn" in value:
        out["ComputeQuotaArn"] = value["compute_quota_arn"]
    if "compute_quota_id" in value:
        out["ComputeQuotaId"] = value["compute_quota_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "compute_quota_version" in value:
        out["ComputeQuotaVersion"] = value["compute_quota_version"]
    if "status" in value:
        import capo_sagemaker.types.scheduler_resource_status

        out["Status"] = (
            capo_sagemaker.types.scheduler_resource_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "compute_quota_config" in value:
        import capo_sagemaker.types.compute_quota_config

        out["ComputeQuotaConfig"] = (
            capo_sagemaker.types.compute_quota_config.serialize_aws_json_1_1(
                value["compute_quota_config"]
            )
        )
    if "compute_quota_target" in value:
        import capo_sagemaker.types.compute_quota_target

        out["ComputeQuotaTarget"] = (
            capo_sagemaker.types.compute_quota_target.serialize_aws_json_1_1(
                value["compute_quota_target"]
            )
        )
    if "activation_state" in value:
        import capo_sagemaker.types.activation_state

        out["ActivationState"] = (
            capo_sagemaker.types.activation_state.serialize_aws_json_1_1(
                value["activation_state"]
            )
        )
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


def deserialize_aws_json_1_1(data: dict) -> DescribeComputeQuotaResponse:
    out: DescribeComputeQuotaResponse = {}  # type: ignore[typeddict-item]
    if "ComputeQuotaArn" in data:
        out["compute_quota_arn"] = data["ComputeQuotaArn"]
    if "ComputeQuotaId" in data:
        out["compute_quota_id"] = data["ComputeQuotaId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ComputeQuotaVersion" in data:
        out["compute_quota_version"] = data["ComputeQuotaVersion"]
    if "Status" in data:
        import capo_sagemaker.types.scheduler_resource_status

        out["status"] = (
            capo_sagemaker.types.scheduler_resource_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    if "ComputeQuotaConfig" in data:
        import capo_sagemaker.types.compute_quota_config

        out["compute_quota_config"] = (
            capo_sagemaker.types.compute_quota_config.deserialize_aws_json_1_1(
                data["ComputeQuotaConfig"]
            )
        )
    if "ComputeQuotaTarget" in data:
        import capo_sagemaker.types.compute_quota_target

        out["compute_quota_target"] = (
            capo_sagemaker.types.compute_quota_target.deserialize_aws_json_1_1(
                data["ComputeQuotaTarget"]
            )
        )
    if "ActivationState" in data:
        import capo_sagemaker.types.activation_state

        out["activation_state"] = (
            capo_sagemaker.types.activation_state.deserialize_aws_json_1_1(
                data["ActivationState"]
            )
        )
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
