"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateComputeQuotaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.activation_state
    import aws_sdk_sagemaker.types.cluster_arn
    import aws_sdk_sagemaker.types.compute_quota_config
    import aws_sdk_sagemaker.types.compute_quota_target
    import aws_sdk_sagemaker.types.entity_description
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.tag_list


class CreateComputeQuotaRequest(TypedDict, closed=True):
    name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>Name to the compute allocation definition.</p>"""
    description: NotRequired[
        "aws_sdk_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>Description of the compute allocation definition.</p>"""
    cluster_arn: NotRequired["aws_sdk_sagemaker.types.cluster_arn.ClusterArn"]
    """<p>ARN of the cluster.</p>"""
    compute_quota_config: NotRequired[
        "aws_sdk_sagemaker.types.compute_quota_config.ComputeQuotaConfig"
    ]
    """<p>Configuration of the compute allocation definition. This includes the resource sharing option, and the setting to preempt low priority tasks.</p>"""
    compute_quota_target: NotRequired[
        "aws_sdk_sagemaker.types.compute_quota_target.ComputeQuotaTarget"
    ]
    """<p>The target entity to allocate compute resources to.</p>"""
    activation_state: NotRequired[
        "aws_sdk_sagemaker.types.activation_state.ActivationState"
    ]
    """<p>The state of the compute allocation being described. Use to enable or disable compute allocation.</p> <p>Default is <code>Enabled</code>.</p>"""
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    """<p>Tags of the compute allocation definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateComputeQuotaRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "compute_quota_config" in value:
        import aws_sdk_sagemaker.types.compute_quota_config

        out["ComputeQuotaConfig"] = (
            aws_sdk_sagemaker.types.compute_quota_config.serialize_aws_json_1_1(
                value["compute_quota_config"]
            )
        )
    if "compute_quota_target" in value:
        import aws_sdk_sagemaker.types.compute_quota_target

        out["ComputeQuotaTarget"] = (
            aws_sdk_sagemaker.types.compute_quota_target.serialize_aws_json_1_1(
                value["compute_quota_target"]
            )
        )
    if "activation_state" in value:
        import aws_sdk_sagemaker.types.activation_state

        out["ActivationState"] = (
            aws_sdk_sagemaker.types.activation_state.serialize_aws_json_1_1(
                value["activation_state"]
            )
        )
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateComputeQuotaRequest:
    out: CreateComputeQuotaRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    if "ComputeQuotaConfig" in data:
        import aws_sdk_sagemaker.types.compute_quota_config

        out["compute_quota_config"] = (
            aws_sdk_sagemaker.types.compute_quota_config.deserialize_aws_json_1_1(
                data["ComputeQuotaConfig"]
            )
        )
    if "ComputeQuotaTarget" in data:
        import aws_sdk_sagemaker.types.compute_quota_target

        out["compute_quota_target"] = (
            aws_sdk_sagemaker.types.compute_quota_target.deserialize_aws_json_1_1(
                data["ComputeQuotaTarget"]
            )
        )
    if "ActivationState" in data:
        import aws_sdk_sagemaker.types.activation_state

        out["activation_state"] = (
            aws_sdk_sagemaker.types.activation_state.deserialize_aws_json_1_1(
                data["ActivationState"]
            )
        )
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
