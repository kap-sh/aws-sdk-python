"""Generated from Smithy shape ``com.amazonaws.ec2#SecondaryNetwork``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.secondary_network_id
    import capo_ec2.types.secondary_network_ipv4_cidr_block_association_list
    import capo_ec2.types.secondary_network_state
    import capo_ec2.types.secondary_network_type
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class SecondaryNetwork(TypedDict, closed=True):
    secondary_network_id: NotRequired[
        "capo_ec2.types.secondary_network_id.SecondaryNetworkId"
    ]
    """<p>The ID of the secondary network.</p>"""
    secondary_network_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the secondary network.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the secondary network.</p>"""
    type: NotRequired["capo_ec2.types.secondary_network_type.SecondaryNetworkType"]
    """<p>The type of the secondary network.</p>"""
    state: NotRequired["capo_ec2.types.secondary_network_state.SecondaryNetworkState"]
    """<p>The state of the secondary network.</p>"""
    state_reason: NotRequired["capo_ec2.types.string.String"]
    """<p>The reason for the current state of the secondary network.</p>"""
    ipv4_cidr_block_associations: NotRequired[
        "capo_ec2.types.secondary_network_ipv4_cidr_block_association_list.SecondaryNetworkIpv4CidrBlockAssociationList"
    ]
    """<p>Information about the IPv4 CIDR blocks associated with the secondary network.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the secondary network.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecondaryNetwork, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "secondary_network_id" in value:
        pairs.append(
            (f"{key_prefix}SecondaryNetworkId", str(value["secondary_network_id"]))
        )
    if "secondary_network_arn" in value:
        pairs.append(
            (f"{key_prefix}SecondaryNetworkArn", str(value["secondary_network_arn"]))
        )
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "type" in value:
        import capo_ec2.types.secondary_network_type

        capo_ec2.types.secondary_network_type.serialize_ec2_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "state" in value:
        import capo_ec2.types.secondary_network_state

        capo_ec2.types.secondary_network_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "state_reason" in value:
        pairs.append((f"{key_prefix}StateReason", str(value["state_reason"])))
    if "ipv4_cidr_block_associations" in value:
        import capo_ec2.types.secondary_network_ipv4_cidr_block_association_list

        capo_ec2.types.secondary_network_ipv4_cidr_block_association_list.serialize_ec2_query(
            value["ipv4_cidr_block_associations"],
            pairs,
            f"{key_prefix}Ipv4CidrBlockAssociationSet",
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> SecondaryNetwork:
    out: SecondaryNetwork = {}  # type: ignore[typeddict-item]
    child_secondary_network_id = el.find("secondaryNetworkId")
    if child_secondary_network_id is not None:
        out["secondary_network_id"] = str(child_secondary_network_id.text or "")
    child_secondary_network_arn = el.find("secondaryNetworkArn")
    if child_secondary_network_arn is not None:
        out["secondary_network_arn"] = str(child_secondary_network_arn.text or "")
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_type = el.find("type")
    if child_type is not None:
        import capo_ec2.types.secondary_network_type

        out["type"] = capo_ec2.types.secondary_network_type.deserialize_ec2_query(
            child_type
        )
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.secondary_network_state

        out["state"] = capo_ec2.types.secondary_network_state.deserialize_ec2_query(
            child_state
        )
    child_state_reason = el.find("stateReason")
    if child_state_reason is not None:
        out["state_reason"] = str(child_state_reason.text or "")
    child_ipv4_cidr_block_associations = el.find("ipv4CidrBlockAssociationSet")
    if child_ipv4_cidr_block_associations is not None:
        import capo_ec2.types.secondary_network_ipv4_cidr_block_association_list

        out["ipv4_cidr_block_associations"] = (
            capo_ec2.types.secondary_network_ipv4_cidr_block_association_list.deserialize_ec2_query(
                child_ipv4_cidr_block_associations
            )
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    return out
