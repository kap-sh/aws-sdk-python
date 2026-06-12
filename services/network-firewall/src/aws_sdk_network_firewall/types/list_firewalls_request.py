"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListFirewallsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.pagination_max_results
    import aws_sdk_network_firewall.types.pagination_token
    import aws_sdk_network_firewall.types.vpc_ids


class ListFirewallsRequest(TypedDict):
    next_token: NotRequired[
        "aws_sdk_network_firewall.types.pagination_token.PaginationToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""
    vpc_ids: NotRequired["aws_sdk_network_firewall.types.vpc_ids.VpcIds"]
    """<p>The unique identifiers of the VPCs that you want Network Firewall to retrieve the firewalls for. Leave this blank to retrieve all firewalls that you have defined.</p>"""
    max_results: NotRequired[
        "aws_sdk_network_firewall.types.pagination_max_results.PaginationMaxResults"
    ]
    """<p>The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListFirewallsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "vpc_ids" in value:
        import aws_sdk_network_firewall.types.vpc_ids

        out["VpcIds"] = aws_sdk_network_firewall.types.vpc_ids.serialize_aws_json_1_0(
            value["vpc_ids"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListFirewallsRequest:
    out: ListFirewallsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "VpcIds" in data:
        import aws_sdk_network_firewall.types.vpc_ids

        out["vpc_ids"] = (
            aws_sdk_network_firewall.types.vpc_ids.deserialize_aws_json_1_0(
                data["VpcIds"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
