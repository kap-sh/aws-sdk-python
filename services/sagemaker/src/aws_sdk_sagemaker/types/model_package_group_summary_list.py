"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageGroupSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_package_group_summary

ModelPackageGroupSummaryList: TypeAlias = list[
    "aws_sdk_sagemaker.types.model_package_group_summary.ModelPackageGroupSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelPackageGroupSummaryList) -> list:
    import aws_sdk_sagemaker.types.model_package_group_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.model_package_group_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ModelPackageGroupSummaryList:
    import aws_sdk_sagemaker.types.model_package_group_summary

    out: ModelPackageGroupSummaryList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.model_package_group_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
