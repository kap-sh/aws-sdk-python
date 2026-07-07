"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#ListVpcEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.vpc_endpoint_filters


class ListVpcEndpointsRequest(TypedDict, closed=True):
    vpc_endpoint_filters: NotRequired[
        "aws_sdk_opensearchserverless.types.vpc_endpoint_filters.VpcEndpointFilters"
    ]
    """<p>Filter the results according to the current status of the VPC endpoint. Possible statuses are <code>CREATING</code>, <code>DELETING</code>, <code>UPDATING</code>, <code>ACTIVE</code>, and <code>FAILED</code>.</p>"""
    next_token: NotRequired["str"]
    """<p>If your initial <code>ListVpcEndpoints</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListVpcEndpoints</code> operations, which returns results in the next page. </p>"""
    max_results: NotRequired["int"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 20.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListVpcEndpointsRequest) -> dict:
    out: dict = {}
    if "vpc_endpoint_filters" in value:
        import aws_sdk_opensearchserverless.types.vpc_endpoint_filters

        out["vpcEndpointFilters"] = (
            aws_sdk_opensearchserverless.types.vpc_endpoint_filters.serialize_aws_json_1_0(
                value["vpc_endpoint_filters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListVpcEndpointsRequest:
    out: ListVpcEndpointsRequest = {}  # type: ignore[typeddict-item]
    if "vpcEndpointFilters" in data:
        import aws_sdk_opensearchserverless.types.vpc_endpoint_filters

        out["vpc_endpoint_filters"] = (
            aws_sdk_opensearchserverless.types.vpc_endpoint_filters.deserialize_aws_json_1_0(
                data["vpcEndpointFilters"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
