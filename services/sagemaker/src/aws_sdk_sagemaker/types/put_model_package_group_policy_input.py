"""Generated from Smithy shape ``com.amazonaws.sagemaker#PutModelPackageGroupPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.policy_string


class PutModelPackageGroupPolicyInput(TypedDict, closed=True):
    model_package_group_name: NotRequired[
        "aws_sdk_sagemaker.types.entity_name.EntityName"
    ]
    """<p>The name of the model group to add a resource policy to.</p>"""
    resource_policy: NotRequired["aws_sdk_sagemaker.types.policy_string.PolicyString"]
    """<p>The resource policy for the model group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutModelPackageGroupPolicyInput) -> dict:
    out: dict = {}
    if "model_package_group_name" in value:
        out["ModelPackageGroupName"] = value["model_package_group_name"]
    if "resource_policy" in value:
        out["ResourcePolicy"] = value["resource_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutModelPackageGroupPolicyInput:
    out: PutModelPackageGroupPolicyInput = {}  # type: ignore[typeddict-item]
    if "ModelPackageGroupName" in data:
        out["model_package_group_name"] = data["ModelPackageGroupName"]
    if "ResourcePolicy" in data:
        out["resource_policy"] = data["ResourcePolicy"]
    return out
