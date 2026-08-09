"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeClientVpnEndpointsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.endpoint_set
    import capo_ec2.types.next_token


class DescribeClientVpnEndpointsResult(TypedDict, closed=True):
    client_vpn_endpoints: NotRequired["capo_ec2.types.endpoint_set.EndpointSet"]
    """<p>Information about the Client VPN endpoints.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeClientVpnEndpointsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "client_vpn_endpoints" in value:
        import capo_ec2.types.endpoint_set

        capo_ec2.types.endpoint_set.serialize_ec2_query(
            value["client_vpn_endpoints"], pairs, f"{key_prefix}ClientVpnEndpoint"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeClientVpnEndpointsResult:
    out: DescribeClientVpnEndpointsResult = {}  # type: ignore[typeddict-item]
    child_client_vpn_endpoints = el.find("clientVpnEndpoint")
    if child_client_vpn_endpoints is not None:
        import capo_ec2.types.endpoint_set

        out["client_vpn_endpoints"] = capo_ec2.types.endpoint_set.deserialize_ec2_query(
            child_client_vpn_endpoints
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
