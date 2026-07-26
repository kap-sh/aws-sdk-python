"""Generated from Smithy shape ``com.amazonaws.sagemaker#GetModelPackageGroupPolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.policy_string


class GetModelPackageGroupPolicyOutput(TypedDict, closed=True):
    resource_policy: NotRequired["capo_sagemaker.types.policy_string.PolicyString"]
    """<p>The resource policy for the model group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetModelPackageGroupPolicyOutput) -> dict:
    out: dict = {}
    if "resource_policy" in value:
        out["ResourcePolicy"] = value["resource_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetModelPackageGroupPolicyOutput:
    out: GetModelPackageGroupPolicyOutput = {}  # type: ignore[typeddict-item]
    if "ResourcePolicy" in data:
        out["resource_policy"] = data["ResourcePolicy"]
    return out
