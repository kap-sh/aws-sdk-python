"""Generated from Smithy shape ``com.amazonaws.sagemaker#EndpointSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.endpoint_summary

EndpointSummaryList: TypeAlias = list[
    "aws_sdk_sagemaker.types.endpoint_summary.EndpointSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointSummaryList) -> list:
    import aws_sdk_sagemaker.types.endpoint_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.endpoint_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EndpointSummaryList:
    import aws_sdk_sagemaker.types.endpoint_summary

    out: EndpointSummaryList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.endpoint_summary.deserialize_aws_json_1_1(item)
        )
    return out
