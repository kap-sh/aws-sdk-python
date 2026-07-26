"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.model_package_summary

ModelPackageSummaryList: TypeAlias = list[
    "capo_sagemaker.types.model_package_summary.ModelPackageSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelPackageSummaryList) -> list:
    import capo_sagemaker.types.model_package_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.model_package_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ModelPackageSummaryList:
    import capo_sagemaker.types.model_package_summary

    out: ModelPackageSummaryList = []
    for item in data:
        out.append(
            capo_sagemaker.types.model_package_summary.deserialize_aws_json_1_1(item)
        )
    return out
