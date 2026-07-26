"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.batch_describe_model_package_summary
    import capo_sagemaker.types.model_package_arn

ModelPackageSummaries: TypeAlias = dict[
    "capo_sagemaker.types.model_package_arn.ModelPackageArn",
    "capo_sagemaker.types.batch_describe_model_package_summary.BatchDescribeModelPackageSummary",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ModelPackageSummaries) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_sagemaker.types.batch_describe_model_package_summary

        out[key] = (
            capo_sagemaker.types.batch_describe_model_package_summary.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelPackageSummaries:
    out: ModelPackageSummaries = {}
    for key, value in data.items():
        import capo_sagemaker.types.batch_describe_model_package_summary

        out[key] = (
            capo_sagemaker.types.batch_describe_model_package_summary.deserialize_aws_json_1_1(
                value
            )
        )
    return out
