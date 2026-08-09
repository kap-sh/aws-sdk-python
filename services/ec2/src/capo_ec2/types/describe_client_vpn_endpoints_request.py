"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeClientVpnEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.client_vpn_endpoint_id_list
    import capo_ec2.types.describe_client_vpn_endpoint_max_results
    import capo_ec2.types.filter_list
    import capo_ec2.types.next_token


class DescribeClientVpnEndpointsRequest(TypedDict, closed=True):
    client_vpn_endpoint_ids: NotRequired[
        "capo_ec2.types.client_vpn_endpoint_id_list.ClientVpnEndpointIdList"
    ]
    """<p>The ID of the Client VPN endpoint.</p>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_client_vpn_endpoint_max_results.DescribeClientVpnEndpointMaxResults"
    ]
    """<p>The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the nextToken value.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to retrieve the next page of results.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters. Filter names and values are case-sensitive.</p> <ul> <li> <p> <code>endpoint-id</code> - The ID of the Client VPN endpoint.</p> </li> <li> <p> <code>transport-protocol</code> - The transport protocol (<code>tcp</code> | <code>udp</code>).</p> </li> </ul>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeClientVpnEndpointsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "client_vpn_endpoint_ids" in value:
        import capo_ec2.types.client_vpn_endpoint_id_list

        capo_ec2.types.client_vpn_endpoint_id_list.serialize_ec2_query(
            value["client_vpn_endpoint_ids"], pairs, f"{key_prefix}ClientVpnEndpointId"
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DescribeClientVpnEndpointsRequest:
    out: DescribeClientVpnEndpointsRequest = {}  # type: ignore[typeddict-item]
    child_client_vpn_endpoint_ids = el.find("ClientVpnEndpointId")
    if child_client_vpn_endpoint_ids is not None:
        import capo_ec2.types.client_vpn_endpoint_id_list

        out["client_vpn_endpoint_ids"] = (
            capo_ec2.types.client_vpn_endpoint_id_list.deserialize_ec2_query(
                child_client_vpn_endpoint_ids
            )
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
