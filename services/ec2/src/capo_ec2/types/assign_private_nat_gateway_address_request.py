"""Generated from Smithy shape ``com.amazonaws.ec2#AssignPrivateNatGatewayAddressRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.ip_list
    import capo_ec2.types.nat_gateway_id
    import capo_ec2.types.private_ip_address_count


class AssignPrivateNatGatewayAddressRequest(TypedDict, closed=True):
    nat_gateway_id: NotRequired["capo_ec2.types.nat_gateway_id.NatGatewayId"]
    """<p>The ID of the NAT gateway.</p>"""
    private_ip_addresses: NotRequired["capo_ec2.types.ip_list.IpList"]
    """<p>The private IPv4 addresses you want to assign to the private NAT gateway.</p>"""
    private_ip_address_count: NotRequired[
        "capo_ec2.types.private_ip_address_count.PrivateIpAddressCount"
    ]
    """<p>The number of private IP addresses to assign to the NAT gateway. You can't specify this parameter when also specifying private IP addresses.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssignPrivateNatGatewayAddressRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "nat_gateway_id" in value:
        pairs.append((f"{prefix}.NatGatewayId", str(value["nat_gateway_id"])))
    if "private_ip_addresses" in value:
        import capo_ec2.types.ip_list

        capo_ec2.types.ip_list.serialize_ec2_query(
            value["private_ip_addresses"], pairs, f"{prefix}.PrivateIpAddresses"
        )
    if "private_ip_address_count" in value:
        pairs.append(
            (f"{prefix}.PrivateIpAddressCount", str(value["private_ip_address_count"]))
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> AssignPrivateNatGatewayAddressRequest:
    out: AssignPrivateNatGatewayAddressRequest = {}  # type: ignore[typeddict-item]
    child_nat_gateway_id = el.find("NatGatewayId")
    if child_nat_gateway_id is not None:
        out["nat_gateway_id"] = str(child_nat_gateway_id.text or "")
    if el.find("PrivateIpAddresses") is not None:
        import capo_ec2.types.ip_list

        out["private_ip_addresses"] = capo_ec2.types.ip_list.deserialize_ec2_query(
            el, "PrivateIpAddresses"
        )
    child_private_ip_address_count = el.find("PrivateIpAddressCount")
    if child_private_ip_address_count is not None:
        out["private_ip_address_count"] = int(child_private_ip_address_count.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
