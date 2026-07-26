"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMulticastDeregisteredGroupSources``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.value_string_list


class TransitGatewayMulticastDeregisteredGroupSources(TypedDict, closed=True):
    transit_gateway_multicast_domain_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the transit gateway multicast domain.</p>"""
    deregistered_network_interface_ids: NotRequired[
        "capo_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The network interface IDs of the non-registered members.</p>"""
    group_ip_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The IP address assigned to the transit gateway multicast group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayMulticastDeregisteredGroupSources,
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
    if "deregistered_network_interface_ids" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["deregistered_network_interface_ids"],
            pairs,
            f"{prefix}.DeregisteredNetworkInterfaceIds",
        )
    if "group_ip_address" in value:
        pairs.append((f"{prefix}.GroupIpAddress", str(value["group_ip_address"])))


def deserialize_ec2_query(
    el: Element,
) -> TransitGatewayMulticastDeregisteredGroupSources:
    out: TransitGatewayMulticastDeregisteredGroupSources = {}  # type: ignore[typeddict-item]
    child_transit_gateway_multicast_domain_id = el.find(
        "TransitGatewayMulticastDomainId"
    )
    if child_transit_gateway_multicast_domain_id is not None:
        out["transit_gateway_multicast_domain_id"] = str(
            child_transit_gateway_multicast_domain_id.text or ""
        )
    if el.find("DeregisteredNetworkInterfaceIds") is not None:
        import capo_ec2.types.value_string_list

        out["deregistered_network_interface_ids"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                el, "DeregisteredNetworkInterfaceIds"
            )
        )
    child_group_ip_address = el.find("GroupIpAddress")
    if child_group_ip_address is not None:
        out["group_ip_address"] = str(child_group_ip_address.text or "")
    return out
