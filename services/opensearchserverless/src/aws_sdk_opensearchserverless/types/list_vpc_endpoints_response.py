"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#ListVpcEndpointsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.vpc_endpoint_summaries


class ListVpcEndpointsResponse(TypedDict):
    vpc_endpoint_summaries: NotRequired[
        "aws_sdk_opensearchserverless.types.vpc_endpoint_summaries.VpcEndpointSummaries"
    ]
    """<p>Details about each VPC endpoint, including the name and current status.</p>"""
    next_token: NotRequired["str"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListVpcEndpointsResponse) -> dict:
    out: dict = {}
    if "vpc_endpoint_summaries" in value:
        import aws_sdk_opensearchserverless.types.vpc_endpoint_summaries

        out["vpcEndpointSummaries"] = (
            aws_sdk_opensearchserverless.types.vpc_endpoint_summaries.serialize_aws_json_1_0(
                value["vpc_endpoint_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListVpcEndpointsResponse:
    out: ListVpcEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "vpcEndpointSummaries" in data:
        import aws_sdk_opensearchserverless.types.vpc_endpoint_summaries

        out["vpc_endpoint_summaries"] = (
            aws_sdk_opensearchserverless.types.vpc_endpoint_summaries.deserialize_aws_json_1_0(
                data["vpcEndpointSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
