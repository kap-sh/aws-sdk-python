"""Generated from Smithy shape ``com.amazonaws.sagemaker#MlflowAppSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.mlflow_app_summary

MlflowAppSummaries: TypeAlias = list[
    "aws_sdk_sagemaker.types.mlflow_app_summary.MlflowAppSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MlflowAppSummaries) -> list:
    import aws_sdk_sagemaker.types.mlflow_app_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.mlflow_app_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MlflowAppSummaries:
    import aws_sdk_sagemaker.types.mlflow_app_summary

    out: MlflowAppSummaries = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.mlflow_app_summary.deserialize_aws_json_1_1(item)
        )
    return out
