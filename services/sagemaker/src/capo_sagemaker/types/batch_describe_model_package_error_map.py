"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchDescribeModelPackageErrorMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.batch_describe_model_package_error
    import capo_sagemaker.types.model_package_arn

BatchDescribeModelPackageErrorMap: TypeAlias = dict[
    "capo_sagemaker.types.model_package_arn.ModelPackageArn",
    "capo_sagemaker.types.batch_describe_model_package_error.BatchDescribeModelPackageError",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    input_to_serialize: BatchDescribeModelPackageErrorMap,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_sagemaker.types.batch_describe_model_package_error

        out[key] = (
            capo_sagemaker.types.batch_describe_model_package_error.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDescribeModelPackageErrorMap:
    out: BatchDescribeModelPackageErrorMap = {}
    for key, value in data.items():
        import capo_sagemaker.types.batch_describe_model_package_error

        out[key] = (
            capo_sagemaker.types.batch_describe_model_package_error.deserialize_aws_json_1_1(
                value
            )
        )
    return out
