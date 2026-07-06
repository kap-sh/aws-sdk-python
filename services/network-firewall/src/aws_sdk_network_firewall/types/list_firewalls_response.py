"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListFirewallsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.firewalls
    import aws_sdk_network_firewall.types.pagination_token


class ListFirewallsResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_network_firewall.types.pagination_token.PaginationToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""
    firewalls: NotRequired["aws_sdk_network_firewall.types.firewalls.Firewalls"]
    """<p>The firewall metadata objects for the VPCs that you specified. Depending on your setting for max results and the number of firewalls you have, a single call might not be the full list. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListFirewallsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "firewalls" in value:
        import aws_sdk_network_firewall.types.firewalls

        out["Firewalls"] = (
            aws_sdk_network_firewall.types.firewalls.serialize_aws_json_1_0(
                value["firewalls"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListFirewallsResponse:
    out: ListFirewallsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Firewalls" in data:
        import aws_sdk_network_firewall.types.firewalls

        out["firewalls"] = (
            aws_sdk_network_firewall.types.firewalls.deserialize_aws_json_1_0(
                data["Firewalls"]
            )
        )
    return out
