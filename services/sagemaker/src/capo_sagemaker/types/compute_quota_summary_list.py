"""Generated from Smithy shape ``com.amazonaws.sagemaker#ComputeQuotaSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.compute_quota_summary

ComputeQuotaSummaryList: TypeAlias = list[
    "capo_sagemaker.types.compute_quota_summary.ComputeQuotaSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeQuotaSummaryList) -> list:
    import capo_sagemaker.types.compute_quota_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.compute_quota_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ComputeQuotaSummaryList:
    import capo_sagemaker.types.compute_quota_summary

    out: ComputeQuotaSummaryList = []
    for item in data:
        out.append(
            capo_sagemaker.types.compute_quota_summary.deserialize_aws_json_1_1(item)
        )
    return out
