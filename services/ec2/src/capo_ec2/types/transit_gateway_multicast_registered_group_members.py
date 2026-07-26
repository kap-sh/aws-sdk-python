"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMulticastRegisteredGroupMembers``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.value_string_list


class TransitGatewayMulticastRegisteredGroupMembers(TypedDict, closed=True):
    transit_gateway_multicast_domain_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the transit gateway multicast domain.</p>"""
    registered_network_interface_ids: NotRequired[
        "capo_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The ID of the registered network interfaces.</p>"""
    group_ip_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The IP address assigned to the transit gateway multicast group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayMulticastRegisteredGroupMembers,
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
    if "registered_network_interface_ids" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["registered_network_interface_ids"],
            pairs,
            f"{prefix}.RegisteredNetworkInterfaceIds",
        )
    if "group_ip_address" in value:
        pairs.append((f"{prefix}.GroupIpAddress", str(value["group_ip_address"])))


def deserialize_ec2_query(el: Element) -> TransitGatewayMulticastRegisteredGroupMembers:
    out: TransitGatewayMulticastRegisteredGroupMembers = {}  # type: ignore[typeddict-item]
    child_transit_gateway_multicast_domain_id = el.find(
        "TransitGatewayMulticastDomainId"
    )
    if child_transit_gateway_multicast_domain_id is not None:
        out["transit_gateway_multicast_domain_id"] = str(
            child_transit_gateway_multicast_domain_id.text or ""
        )
    if el.find("RegisteredNetworkInterfaceIds") is not None:
        import capo_ec2.types.value_string_list

        out["registered_network_interface_ids"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                el, "RegisteredNetworkInterfaceIds"
            )
        )
    child_group_ip_address = el.find("GroupIpAddress")
    if child_group_ip_address is not None:
        out["group_ip_address"] = str(child_group_ip_address.text or "")
    return out
