"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpnGatewaysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.vpn_gateway_id_string_list


class DescribeVpnGatewaysRequest(TypedDict, closed=True):
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>amazon-side-asn</code> - The Autonomous System Number (ASN) for the Amazon side of the gateway.</p> </li> <li> <p> <code>attachment.state</code> - The current state of the attachment between the gateway and the VPC (<code>attaching</code> | <code>attached</code> | <code>detaching</code> | <code>detached</code>).</p> </li> <li> <p> <code>attachment.vpc-id</code> - The ID of an attached VPC.</p> </li> <li> <p> <code>availability-zone</code> - The Availability Zone for the virtual private gateway (if applicable).</p> </li> <li> <p> <code>state</code> - The state of the virtual private gateway (<code>pending</code> | <code>available</code> | <code>deleting</code> | <code>deleted</code>).</p> </li> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> <li> <p> <code>type</code> - The type of virtual private gateway. Currently the only supported type is <code>ipsec.1</code>.</p> </li> <li> <p> <code>vpn-gateway-id</code> - The ID of the virtual private gateway.</p> </li> </ul>"""
    vpn_gateway_ids: NotRequired[
        "capo_ec2.types.vpn_gateway_id_string_list.VpnGatewayIdStringList"
    ]
    """<p>One or more virtual private gateway IDs.</p> <p>Default: Describes all your virtual private gateways.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpnGatewaysRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )
    if "vpn_gateway_ids" in value:
        import capo_ec2.types.vpn_gateway_id_string_list

        capo_ec2.types.vpn_gateway_id_string_list.serialize_ec2_query(
            value["vpn_gateway_ids"], pairs, f"{key_prefix}VpnGatewayIds"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DescribeVpnGatewaysRequest:
    out: DescribeVpnGatewaysRequest = {}  # type: ignore[typeddict-item]
    if el.find("Filters") is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(el, "Filters")
    if el.find("VpnGatewayIds") is not None:
        import capo_ec2.types.vpn_gateway_id_string_list

        out["vpn_gateway_ids"] = (
            capo_ec2.types.vpn_gateway_id_string_list.deserialize_ec2_query(
                el, "VpnGatewayIds"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
