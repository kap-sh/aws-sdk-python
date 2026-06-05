"""Generated from Smithy shape ``com.amazonaws.ec2#DeregisterTransitGatewayMulticastGroupSourcesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_multicast_domain_id
    import aws_sdk_ec2.types.transit_gateway_network_interface_id_list


class DeregisterTransitGatewayMulticastGroupSourcesRequest(TypedDict):
    transit_gateway_multicast_domain_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_multicast_domain_id.TransitGatewayMulticastDomainId"
    ]
    """<p>The ID of the transit gateway multicast domain.</p>"""
    group_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IP address assigned to the transit gateway multicast group.</p>"""
    network_interface_ids: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_network_interface_id_list.TransitGatewayNetworkInterfaceIdList"
    ]
    """<p>The IDs of the group sources' network interfaces.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeregisterTransitGatewayMulticastGroupSourcesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_multicast_domain_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayMulticastDomainId",
                str(value["transit_gateway_multicast_domain_id"]),
            )
        )
    if "group_ip_address" in value:
        pairs.append((f"{prefix}.GroupIpAddress", str(value["group_ip_address"])))
    if "network_interface_ids" in value:
        import aws_sdk_ec2.types.transit_gateway_network_interface_id_list

        aws_sdk_ec2.types.transit_gateway_network_interface_id_list.serialize_ec2_query(
            value["network_interface_ids"], pairs, f"{prefix}.NetworkInterfaceIds"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> DeregisterTransitGatewayMulticastGroupSourcesRequest:
    out: DeregisterTransitGatewayMulticastGroupSourcesRequest = {}  # type: ignore[typeddict-item]
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
    if el.find("NetworkInterfaceIds") is not None:
        import aws_sdk_ec2.types.transit_gateway_network_interface_id_list

        out["network_interface_ids"] = (
            aws_sdk_ec2.types.transit_gateway_network_interface_id_list.deserialize_ec2_query(
                el, "NetworkInterfaceIds"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
