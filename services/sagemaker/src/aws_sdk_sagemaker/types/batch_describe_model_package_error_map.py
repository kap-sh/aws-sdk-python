"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchDescribeModelPackageErrorMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.batch_describe_model_package_error
    import aws_sdk_sagemaker.types.model_package_arn

BatchDescribeModelPackageErrorMap: TypeAlias = dict[
    "aws_sdk_sagemaker.types.model_package_arn.ModelPackageArn",
    "aws_sdk_sagemaker.types.batch_describe_model_package_error.BatchDescribeModelPackageError",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    input_to_serialize: BatchDescribeModelPackageErrorMap,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_sagemaker.types.batch_describe_model_package_error

        out[key] = (
            aws_sdk_sagemaker.types.batch_describe_model_package_error.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDescribeModelPackageErrorMap:
    out: BatchDescribeModelPackageErrorMap = {}
    for key, value in data.items():
        import aws_sdk_sagemaker.types.batch_describe_model_package_error

        out[key] = (
            aws_sdk_sagemaker.types.batch_describe_model_package_error.deserialize_aws_json_1_1(
                value
            )
        )
    return out
