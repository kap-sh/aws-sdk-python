"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateComputeQuotaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.activation_state
    import aws_sdk_sagemaker.types.compute_quota_config
    import aws_sdk_sagemaker.types.compute_quota_id
    import aws_sdk_sagemaker.types.compute_quota_target
    import aws_sdk_sagemaker.types.entity_description
    import aws_sdk_sagemaker.types.integer


class UpdateComputeQuotaRequest(TypedDict, closed=True):
    compute_quota_id: NotRequired[
        "aws_sdk_sagemaker.types.compute_quota_id.ComputeQuotaId"
    ]
    """<p>ID of the compute allocation definition.</p>"""
    target_version: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>Target version.</p>"""
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
    description: NotRequired[
        "aws_sdk_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>Description of the compute allocation definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateComputeQuotaRequest) -> dict:
    out: dict = {}
    if "compute_quota_id" in value:
        out["ComputeQuotaId"] = value["compute_quota_id"]
    if "target_version" in value:
        out["TargetVersion"] = value["target_version"]
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
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateComputeQuotaRequest:
    out: UpdateComputeQuotaRequest = {}  # type: ignore[typeddict-item]
    if "ComputeQuotaId" in data:
        out["compute_quota_id"] = data["ComputeQuotaId"]
    if "TargetVersion" in data:
        out["target_version"] = data["TargetVersion"]
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
    if "Description" in data:
        out["description"] = data["Description"]
    return out
