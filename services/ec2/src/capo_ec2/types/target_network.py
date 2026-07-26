"""Generated from Smithy shape ``com.amazonaws.ec2#TargetNetwork``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.association_status
    import capo_ec2.types.client_vpn_availability_zone_id_set
    import capo_ec2.types.client_vpn_availability_zone_set
    import capo_ec2.types.string
    import capo_ec2.types.value_string_list


class TargetNetwork(TypedDict, closed=True):
    association_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the association.</p>"""
    vpc_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC in which the target network (subnet) is located.</p>"""
    target_network_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the subnet specified as the target network.</p>"""
    client_vpn_endpoint_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Client VPN endpoint with which the target network is associated.</p>"""
    status: NotRequired["capo_ec2.types.association_status.AssociationStatus"]
    """<p>The current state of the target network association.</p>"""
    security_groups: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The IDs of the security groups applied to the target network association.</p>"""
    availability_zones: NotRequired[
        "capo_ec2.types.client_vpn_availability_zone_set.ClientVpnAvailabilityZoneSet"
    ]
    """<p>The Availability Zone names for the target network association, if the Client VPN endpoint uses a Transit Gateway.</p>"""
    availability_zone_ids: NotRequired[
        "capo_ec2.types.client_vpn_availability_zone_id_set.ClientVpnAvailabilityZoneIdSet"
    ]
    """<p>The Availability Zone IDs for the target network association, if the Client VPN endpoint uses a Transit Gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TargetNetwork, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "association_id" in value:
        pairs.append((f"{prefix}.AssociationId", str(value["association_id"])))
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "target_network_id" in value:
        pairs.append((f"{prefix}.TargetNetworkId", str(value["target_network_id"])))
    if "client_vpn_endpoint_id" in value:
        pairs.append(
            (f"{prefix}.ClientVpnEndpointId", str(value["client_vpn_endpoint_id"]))
        )
    if "status" in value:
        import capo_ec2.types.association_status

        capo_ec2.types.association_status.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "security_groups" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["security_groups"], pairs, f"{prefix}.SecurityGroups"
        )
    if "availability_zones" in value:
        import capo_ec2.types.client_vpn_availability_zone_set

        capo_ec2.types.client_vpn_availability_zone_set.serialize_ec2_query(
            value["availability_zones"], pairs, f"{prefix}.AvailabilityZoneSet"
        )
    if "availability_zone_ids" in value:
        import capo_ec2.types.client_vpn_availability_zone_id_set

        capo_ec2.types.client_vpn_availability_zone_id_set.serialize_ec2_query(
            value["availability_zone_ids"], pairs, f"{prefix}.AvailabilityZoneIdSet"
        )


def deserialize_ec2_query(el: Element) -> TargetNetwork:
    out: TargetNetwork = {}  # type: ignore[typeddict-item]
    child_association_id = el.find("AssociationId")
    if child_association_id is not None:
        out["association_id"] = str(child_association_id.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_target_network_id = el.find("TargetNetworkId")
    if child_target_network_id is not None:
        out["target_network_id"] = str(child_target_network_id.text or "")
    child_client_vpn_endpoint_id = el.find("ClientVpnEndpointId")
    if child_client_vpn_endpoint_id is not None:
        out["client_vpn_endpoint_id"] = str(child_client_vpn_endpoint_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_ec2.types.association_status

        out["status"] = capo_ec2.types.association_status.deserialize_ec2_query(
            child_status
        )
    if el.find("SecurityGroups") is not None:
        import capo_ec2.types.value_string_list

        out["security_groups"] = capo_ec2.types.value_string_list.deserialize_ec2_query(
            el, "SecurityGroups"
        )
    if el.find("AvailabilityZoneSet") is not None:
        import capo_ec2.types.client_vpn_availability_zone_set

        out["availability_zones"] = (
            capo_ec2.types.client_vpn_availability_zone_set.deserialize_ec2_query(
                el, "AvailabilityZoneSet"
            )
        )
    if el.find("AvailabilityZoneIdSet") is not None:
        import capo_ec2.types.client_vpn_availability_zone_id_set

        out["availability_zone_ids"] = (
            capo_ec2.types.client_vpn_availability_zone_id_set.deserialize_ec2_query(
                el, "AvailabilityZoneIdSet"
            )
        )
    return out
