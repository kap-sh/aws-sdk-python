"""Generated from Smithy shape ``com.amazonaws.sagemaker#EndpointSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint_summary

EndpointSummaryList: TypeAlias = list[
    "capo_sagemaker.types.endpoint_summary.EndpointSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointSummaryList) -> list:
    import capo_sagemaker.types.endpoint_summary

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.endpoint_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EndpointSummaryList:
    import capo_sagemaker.types.endpoint_summary

    out: EndpointSummaryList = []
    for item in data:
        out.append(capo_sagemaker.types.endpoint_summary.deserialize_aws_json_1_1(item))
    return out
