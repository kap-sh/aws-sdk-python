"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#VpcEndpointSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchserverless.types.vpc_endpoint_summary

VpcEndpointSummaries: TypeAlias = list[
    "capo_opensearchserverless.types.vpc_endpoint_summary.VpcEndpointSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcEndpointSummaries) -> list:
    import capo_opensearchserverless.types.vpc_endpoint_summary

    out: list = []
    for item in value:
        out.append(
            capo_opensearchserverless.types.vpc_endpoint_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> VpcEndpointSummaries:
    import capo_opensearchserverless.types.vpc_endpoint_summary

    out: VpcEndpointSummaries = []
    for item in data:
        out.append(
            capo_opensearchserverless.types.vpc_endpoint_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
