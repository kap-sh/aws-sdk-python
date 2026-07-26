"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListProxiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.pagination_token
    import capo_network_firewall.types.proxies


class ListProxiesResponse(TypedDict, closed=True):
    proxies: NotRequired["capo_network_firewall.types.proxies.Proxies"]
    """<p>The metadata for the proxies. Depending on your setting for max results and the number of proxies that you have, this might not be the full list. </p>"""
    next_token: NotRequired[
        "capo_network_firewall.types.pagination_token.PaginationToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListProxiesResponse) -> dict:
    out: dict = {}
    if "proxies" in value:
        import capo_network_firewall.types.proxies

        out["Proxies"] = capo_network_firewall.types.proxies.serialize_aws_json_1_0(
            value["proxies"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListProxiesResponse:
    out: ListProxiesResponse = {}  # type: ignore[typeddict-item]
    if "Proxies" in data:
        import capo_network_firewall.types.proxies

        out["proxies"] = capo_network_firewall.types.proxies.deserialize_aws_json_1_0(
            data["Proxies"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
