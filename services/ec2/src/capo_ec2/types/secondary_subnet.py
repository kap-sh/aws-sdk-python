"""Generated from Smithy shape ``com.amazonaws.ec2#SecondarySubnet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.availability_zone_id
    import capo_ec2.types.availability_zone_name
    import capo_ec2.types.secondary_network_id
    import capo_ec2.types.secondary_network_type
    import capo_ec2.types.secondary_subnet_id
    import capo_ec2.types.secondary_subnet_ipv4_cidr_block_association_list
    import capo_ec2.types.secondary_subnet_state
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class SecondarySubnet(TypedDict, closed=True):
    secondary_subnet_id: NotRequired[
        "capo_ec2.types.secondary_subnet_id.SecondarySubnetId"
    ]
    """<p>The ID of the secondary subnet.</p>"""
    secondary_subnet_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the secondary subnet.</p>"""
    secondary_network_id: NotRequired[
        "capo_ec2.types.secondary_network_id.SecondaryNetworkId"
    ]
    """<p>The ID of the secondary network.</p>"""
    secondary_network_type: NotRequired[
        "capo_ec2.types.secondary_network_type.SecondaryNetworkType"
    ]
    """<p>The type of the secondary network.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the secondary subnet.</p>"""
    availability_zone_id: NotRequired[
        "capo_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone of the secondary subnet.</p>"""
    availability_zone: NotRequired[
        "capo_ec2.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>The Availability Zone of the secondary subnet.</p>"""
    ipv4_cidr_block_associations: NotRequired[
        "capo_ec2.types.secondary_subnet_ipv4_cidr_block_association_list.SecondarySubnetIpv4CidrBlockAssociationList"
    ]
    """<p>Information about the IPv4 CIDR blocks associated with the secondary subnet.</p>"""
    state: NotRequired["capo_ec2.types.secondary_subnet_state.SecondarySubnetState"]
    """<p>The state of the secondary subnet.</p>"""
    state_reason: NotRequired["capo_ec2.types.string.String"]
    """<p>The reason for the current state of the secondary subnet.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the secondary subnet.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecondarySubnet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "secondary_subnet_id" in value:
        pairs.append(
            (f"{key_prefix}SecondarySubnetId", str(value["secondary_subnet_id"]))
        )
    if "secondary_subnet_arn" in value:
        pairs.append(
            (f"{key_prefix}SecondarySubnetArn", str(value["secondary_subnet_arn"]))
        )
    if "secondary_network_id" in value:
        pairs.append(
            (f"{key_prefix}SecondaryNetworkId", str(value["secondary_network_id"]))
        )
    if "secondary_network_type" in value:
        import capo_ec2.types.secondary_network_type

        capo_ec2.types.secondary_network_type.serialize_ec2_query(
            value["secondary_network_type"], pairs, f"{key_prefix}SecondaryNetworkType"
        )
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "ipv4_cidr_block_associations" in value:
        import capo_ec2.types.secondary_subnet_ipv4_cidr_block_association_list

        capo_ec2.types.secondary_subnet_ipv4_cidr_block_association_list.serialize_ec2_query(
            value["ipv4_cidr_block_associations"],
            pairs,
            f"{key_prefix}Ipv4CidrBlockAssociationSet",
        )
    if "state" in value:
        import capo_ec2.types.secondary_subnet_state

        capo_ec2.types.secondary_subnet_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "state_reason" in value:
        pairs.append((f"{key_prefix}StateReason", str(value["state_reason"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> SecondarySubnet:
    out: SecondarySubnet = {}  # type: ignore[typeddict-item]
    child_secondary_subnet_id = el.find("secondarySubnetId")
    if child_secondary_subnet_id is not None:
        out["secondary_subnet_id"] = str(child_secondary_subnet_id.text or "")
    child_secondary_subnet_arn = el.find("secondarySubnetArn")
    if child_secondary_subnet_arn is not None:
        out["secondary_subnet_arn"] = str(child_secondary_subnet_arn.text or "")
    child_secondary_network_id = el.find("secondaryNetworkId")
    if child_secondary_network_id is not None:
        out["secondary_network_id"] = str(child_secondary_network_id.text or "")
    child_secondary_network_type = el.find("secondaryNetworkType")
    if child_secondary_network_type is not None:
        import capo_ec2.types.secondary_network_type

        out["secondary_network_type"] = (
            capo_ec2.types.secondary_network_type.deserialize_ec2_query(
                child_secondary_network_type
            )
        )
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_availability_zone_id = el.find("availabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    if el.find("ipv4CidrBlockAssociationSet") is not None:
        import capo_ec2.types.secondary_subnet_ipv4_cidr_block_association_list

        out["ipv4_cidr_block_associations"] = (
            capo_ec2.types.secondary_subnet_ipv4_cidr_block_association_list.deserialize_ec2_query(
                el, "ipv4CidrBlockAssociationSet"
            )
        )
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.secondary_subnet_state

        out["state"] = capo_ec2.types.secondary_subnet_state.deserialize_ec2_query(
            child_state
        )
    child_state_reason = el.find("stateReason")
    if child_state_reason is not None:
        out["state_reason"] = str(child_state_reason.text or "")
    if el.find("tagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "tagSet")
    return out
