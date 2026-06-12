"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.batch_describe_model_package_summary
    import aws_sdk_sagemaker.types.model_package_arn

ModelPackageSummaries: TypeAlias = dict[
    "aws_sdk_sagemaker.types.model_package_arn.ModelPackageArn",
    "aws_sdk_sagemaker.types.batch_describe_model_package_summary.BatchDescribeModelPackageSummary",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ModelPackageSummaries) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_sagemaker.types.batch_describe_model_package_summary

        out[key] = (
            aws_sdk_sagemaker.types.batch_describe_model_package_summary.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelPackageSummaries:
    out: ModelPackageSummaries = {}
    for key, value in data.items():
        import aws_sdk_sagemaker.types.batch_describe_model_package_summary

        out[key] = (
            aws_sdk_sagemaker.types.batch_describe_model_package_summary.deserialize_aws_json_1_1(
                value
            )
        )
    return out
