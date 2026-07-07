"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteModelPackageGroupPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name


class DeleteModelPackageGroupPolicyInput(TypedDict, closed=True):
    model_package_group_name: NotRequired[
        "aws_sdk_sagemaker.types.entity_name.EntityName"
    ]
    """<p>The name of the model group for which to delete the policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteModelPackageGroupPolicyInput) -> dict:
    out: dict = {}
    if "model_package_group_name" in value:
        out["ModelPackageGroupName"] = value["model_package_group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteModelPackageGroupPolicyInput:
    out: DeleteModelPackageGroupPolicyInput = {}  # type: ignore[typeddict-item]
    if "ModelPackageGroupName" in data:
        out["model_package_group_name"] = data["ModelPackageGroupName"]
    return out
