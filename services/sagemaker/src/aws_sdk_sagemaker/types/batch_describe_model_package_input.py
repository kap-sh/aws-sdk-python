"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchDescribeModelPackageInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_package_arn_list


class BatchDescribeModelPackageInput(TypedDict):
    model_package_arn_list: NotRequired[
        "aws_sdk_sagemaker.types.model_package_arn_list.ModelPackageArnList"
    ]
    """<p>The list of Amazon Resource Name (ARN) of the model package groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDescribeModelPackageInput) -> dict:
    out: dict = {}
    if "model_package_arn_list" in value:
        import aws_sdk_sagemaker.types.model_package_arn_list

        out["ModelPackageArnList"] = (
            aws_sdk_sagemaker.types.model_package_arn_list.serialize_aws_json_1_1(
                value["model_package_arn_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDescribeModelPackageInput:
    out: BatchDescribeModelPackageInput = {}  # type: ignore[typeddict-item]
    if "ModelPackageArnList" in data:
        import aws_sdk_sagemaker.types.model_package_arn_list

        out["model_package_arn_list"] = (
            aws_sdk_sagemaker.types.model_package_arn_list.deserialize_aws_json_1_1(
                data["ModelPackageArnList"]
            )
        )
    return out
