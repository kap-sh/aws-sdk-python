"""Generated from Smithy shape ``com.amazonaws.ec2#RegisterTransitGatewayMulticastGroupSourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string
    import capo_ec2.types.transit_gateway_multicast_domain_id
    import capo_ec2.types.transit_gateway_network_interface_id_list


class RegisterTransitGatewayMulticastGroupSourcesRequest(TypedDict, closed=True):
    transit_gateway_multicast_domain_id: NotRequired[
        "capo_ec2.types.transit_gateway_multicast_domain_id.TransitGatewayMulticastDomainId"
    ]
    """<p>The ID of the transit gateway multicast domain.</p>"""
    group_ip_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The IP address assigned to the transit gateway multicast group.</p>"""
    network_interface_ids: NotRequired[
        "capo_ec2.types.transit_gateway_network_interface_id_list.TransitGatewayNetworkInterfaceIdList"
    ]
    """<p>The group sources' network interface IDs to register with the transit gateway multicast group.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RegisterTransitGatewayMulticastGroupSourcesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_multicast_domain_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayMulticastDomainId",
                str(value["transit_gateway_multicast_domain_id"]),
            )
        )
    if "group_ip_address" in value:
        pairs.append((f"{key_prefix}GroupIpAddress", str(value["group_ip_address"])))
    if "network_interface_ids" in value:
        import capo_ec2.types.transit_gateway_network_interface_id_list

        capo_ec2.types.transit_gateway_network_interface_id_list.serialize_ec2_query(
            value["network_interface_ids"], pairs, f"{key_prefix}NetworkInterfaceIds"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> RegisterTransitGatewayMulticastGroupSourcesRequest:
    out: RegisterTransitGatewayMulticastGroupSourcesRequest = {}  # type: ignore[typeddict-item]
    child_transit_gateway_multicast_domain_id = el.find(
        "TransitGatewayMulticastDomainId"
    )
    if child_transit_gateway_multicast_domain_id is not None:
        out["transit_gateway_multicast_domain_id"] = str(
            child_transit_gateway_multicast_domain_id.text or ""
        )
    child_group_ip_address = el.find("GroupIpAddress")
    if child_group_ip_address is not None:
        out["group_ip_address"] = str(child_group_ip_address.text or "")
    child_network_interface_ids = el.find("NetworkInterfaceIds")
    if child_network_interface_ids is not None:
        import capo_ec2.types.transit_gateway_network_interface_id_list

        out["network_interface_ids"] = (
            capo_ec2.types.transit_gateway_network_interface_id_list.deserialize_ec2_query(
                child_network_interface_ids
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
