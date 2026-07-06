"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateModelPackageOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_package_arn


class CreateModelPackageOutput(TypedDict, closed=True):
    model_package_arn: NotRequired[
        "aws_sdk_sagemaker.types.model_package_arn.ModelPackageArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the new model package.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateModelPackageOutput) -> dict:
    out: dict = {}
    if "model_package_arn" in value:
        out["ModelPackageArn"] = value["model_package_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateModelPackageOutput:
    out: CreateModelPackageOutput = {}  # type: ignore[typeddict-item]
    if "ModelPackageArn" in data:
        out["model_package_arn"] = data["ModelPackageArn"]
    return out
