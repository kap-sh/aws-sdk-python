"""Generated from Smithy shape ``com.amazonaws.apprunner#ListVpcIngressConnectionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.list_vpc_ingress_connections_filter
    import aws_sdk_apprunner.types.max_results
    import aws_sdk_apprunner.types.next_token


class ListVpcIngressConnectionsRequest(TypedDict):
    filter: NotRequired[
        "aws_sdk_apprunner.types.list_vpc_ingress_connections_filter.ListVpcIngressConnectionsFilter"
    ]
    """<p>The VPC Ingress Connections to be listed based on either the Service Arn or Vpc Endpoint Id, or both.</p>"""
    max_results: NotRequired["aws_sdk_apprunner.types.max_results.MaxResults"]
    """<p>The maximum number of results to include in each response (result page). It's used for a paginated request.</p> <p>If you don't specify <code>MaxResults</code>, the request retrieves all available results in a single response.</p>"""
    next_token: NotRequired["aws_sdk_apprunner.types.next_token.NextToken"]
    """<p>A token from a previous result page. It's used for a paginated request. The request retrieves the next result page. All other parameter values must be identical to the ones that are specified in the initial request.</p> <p>If you don't specify <code>NextToken</code>, the request retrieves the first result page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListVpcIngressConnectionsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_apprunner.types.list_vpc_ingress_connections_filter

        out["Filter"] = (
            aws_sdk_apprunner.types.list_vpc_ingress_connections_filter.serialize_aws_json_1_0(
                value["filter"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListVpcIngressConnectionsRequest:
    out: ListVpcIngressConnectionsRequest = {}  # type: ignore[typeddict-item]
    if "Filter" in data:
        import aws_sdk_apprunner.types.list_vpc_ingress_connections_filter

        out["filter"] = (
            aws_sdk_apprunner.types.list_vpc_ingress_connections_filter.deserialize_aws_json_1_0(
                data["Filter"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
