"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_package_arn

ModelPackageArnList: TypeAlias = list[
    "aws_sdk_sagemaker.types.model_package_arn.ModelPackageArn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelPackageArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ModelPackageArnList:
    return list(data)
