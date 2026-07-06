"""Generated from Smithy shape ``com.amazonaws.sagemaker#PutModelPackageGroupPolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_package_group_arn


class PutModelPackageGroupPolicyOutput(TypedDict, closed=True):
    model_package_group_arn: NotRequired[
        "aws_sdk_sagemaker.types.model_package_group_arn.ModelPackageGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model package group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutModelPackageGroupPolicyOutput) -> dict:
    out: dict = {}
    if "model_package_group_arn" in value:
        out["ModelPackageGroupArn"] = value["model_package_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutModelPackageGroupPolicyOutput:
    out: PutModelPackageGroupPolicyOutput = {}  # type: ignore[typeddict-item]
    if "ModelPackageGroupArn" in data:
        out["model_package_group_arn"] = data["ModelPackageGroupArn"]
    return out
