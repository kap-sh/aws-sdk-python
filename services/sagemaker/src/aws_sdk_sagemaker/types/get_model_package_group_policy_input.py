"""Generated from Smithy shape ``com.amazonaws.sagemaker#GetModelPackageGroupPolicyInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name


class GetModelPackageGroupPolicyInput(TypedDict):
    model_package_group_name: NotRequired[
        "aws_sdk_sagemaker.types.entity_name.EntityName"
    ]
    """<p>The name of the model group for which to get the resource policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetModelPackageGroupPolicyInput) -> dict:
    out: dict = {}
    if "model_package_group_name" in value:
        out["ModelPackageGroupName"] = value["model_package_group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetModelPackageGroupPolicyInput:
    out: GetModelPackageGroupPolicyInput = {}  # type: ignore[typeddict-item]
    if "ModelPackageGroupName" in data:
        out["model_package_group_name"] = data["ModelPackageGroupName"]
    return out
