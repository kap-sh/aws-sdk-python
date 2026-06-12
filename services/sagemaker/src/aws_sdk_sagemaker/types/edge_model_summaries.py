"""Generated from Smithy shape ``com.amazonaws.sagemaker#EdgeModelSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.edge_model_summary

EdgeModelSummaries: TypeAlias = list[
    "aws_sdk_sagemaker.types.edge_model_summary.EdgeModelSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdgeModelSummaries) -> list:
    import aws_sdk_sagemaker.types.edge_model_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.edge_model_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EdgeModelSummaries:
    import aws_sdk_sagemaker.types.edge_model_summary

    out: EdgeModelSummaries = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.edge_model_summary.deserialize_aws_json_1_1(item)
        )
    return out
