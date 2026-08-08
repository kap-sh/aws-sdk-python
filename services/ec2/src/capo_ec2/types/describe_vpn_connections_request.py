"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpnConnectionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.vpn_connection_id_string_list


class DescribeVpnConnectionsRequest(TypedDict, closed=True):
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>customer-gateway-configuration</code> - The configuration information for the customer gateway.</p> </li> <li> <p> <code>customer-gateway-id</code> - The ID of a customer gateway associated with the VPN connection.</p> </li> <li> <p> <code>state</code> - The state of the VPN connection (<code>pending</code> | <code>available</code> | <code>deleting</code> | <code>deleted</code>).</p> </li> <li> <p> <code>option.static-routes-only</code> - Indicates whether the connection has static routes only. Used for devices that do not support Border Gateway Protocol (BGP).</p> </li> <li> <p> <code>route.destination-cidr-block</code> - The destination CIDR block. This corresponds to the subnet used in a customer data center.</p> </li> <li> <p> <code>bgp-asn</code> - The BGP Autonomous System Number (ASN) associated with a BGP device.</p> </li> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> <li> <p> <code>type</code> - The type of VPN connection. Currently the only supported type is <code>ipsec.1</code>.</p> </li> <li> <p> <code>vpn-connection-id</code> - The ID of the VPN connection.</p> </li> <li> <p> <code>vpn-gateway-id</code> - The ID of a virtual private gateway associated with the VPN connection.</p> </li> <li> <p> <code>transit-gateway-id</code> - The ID of a transit gateway associated with the VPN connection.</p> </li> </ul>"""
    vpn_connection_ids: NotRequired[
        "capo_ec2.types.vpn_connection_id_string_list.VpnConnectionIdStringList"
    ]
    """<p>One or more VPN connection IDs.</p> <p>Default: Describes your VPN connections.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpnConnectionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "vpn_connection_ids" in value:
        import capo_ec2.types.vpn_connection_id_string_list

        capo_ec2.types.vpn_connection_id_string_list.serialize_ec2_query(
            value["vpn_connection_ids"], pairs, f"{key_prefix}VpnConnectionId"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DescribeVpnConnectionsRequest:
    out: DescribeVpnConnectionsRequest = {}  # type: ignore[typeddict-item]
    if el.find("Filter") is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(el, "Filter")
    if el.find("VpnConnectionId") is not None:
        import capo_ec2.types.vpn_connection_id_string_list

        out["vpn_connection_ids"] = (
            capo_ec2.types.vpn_connection_id_string_list.deserialize_ec2_query(
                el, "VpnConnectionId"
            )
        )
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
