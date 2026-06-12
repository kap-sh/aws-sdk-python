"""Generated from Smithy shape ``com.amazonaws.sagemaker#AlgorithmSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.algorithm_summary

AlgorithmSummaryList: TypeAlias = list[
    "aws_sdk_sagemaker.types.algorithm_summary.AlgorithmSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlgorithmSummaryList) -> list:
    import aws_sdk_sagemaker.types.algorithm_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.algorithm_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AlgorithmSummaryList:
    import aws_sdk_sagemaker.types.algorithm_summary

    out: AlgorithmSummaryList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.algorithm_summary.deserialize_aws_json_1_1(item)
        )
    return out
