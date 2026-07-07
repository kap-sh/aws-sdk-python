"""Generated from Smithy shape ``com.amazonaws.ec2#SecondaryNetwork``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.secondary_network_id
    import aws_sdk_ec2.types.secondary_network_ipv4_cidr_block_association_list
    import aws_sdk_ec2.types.secondary_network_state
    import aws_sdk_ec2.types.secondary_network_type
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class SecondaryNetwork(TypedDict, closed=True):
    secondary_network_id: NotRequired[
        "aws_sdk_ec2.types.secondary_network_id.SecondaryNetworkId"
    ]
    """<p>The ID of the secondary network.</p>"""
    secondary_network_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the secondary network.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the secondary network.</p>"""
    type: NotRequired["aws_sdk_ec2.types.secondary_network_type.SecondaryNetworkType"]
    """<p>The type of the secondary network.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.secondary_network_state.SecondaryNetworkState"
    ]
    """<p>The state of the secondary network.</p>"""
    state_reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason for the current state of the secondary network.</p>"""
    ipv4_cidr_block_associations: NotRequired[
        "aws_sdk_ec2.types.secondary_network_ipv4_cidr_block_association_list.SecondaryNetworkIpv4CidrBlockAssociationList"
    ]
    """<p>Information about the IPv4 CIDR blocks associated with the secondary network.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the secondary network.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecondaryNetwork, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "secondary_network_id" in value:
        pairs.append(
            (f"{prefix}.SecondaryNetworkId", str(value["secondary_network_id"]))
        )
    if "secondary_network_arn" in value:
        pairs.append(
            (f"{prefix}.SecondaryNetworkArn", str(value["secondary_network_arn"]))
        )
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "type" in value:
        import aws_sdk_ec2.types.secondary_network_type

        aws_sdk_ec2.types.secondary_network_type.serialize_ec2_query(
            value["type"], pairs, f"{prefix}.Type"
        )
    if "state" in value:
        import aws_sdk_ec2.types.secondary_network_state

        aws_sdk_ec2.types.secondary_network_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "state_reason" in value:
        pairs.append((f"{prefix}.StateReason", str(value["state_reason"])))
    if "ipv4_cidr_block_associations" in value:
        import aws_sdk_ec2.types.secondary_network_ipv4_cidr_block_association_list

        aws_sdk_ec2.types.secondary_network_ipv4_cidr_block_association_list.serialize_ec2_query(
            value["ipv4_cidr_block_associations"],
            pairs,
            f"{prefix}.Ipv4CidrBlockAssociationSet",
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> SecondaryNetwork:
    out: SecondaryNetwork = {}  # type: ignore[typeddict-item]
    child_secondary_network_id = el.find("SecondaryNetworkId")
    if child_secondary_network_id is not None:
        out["secondary_network_id"] = str(child_secondary_network_id.text or "")
    child_secondary_network_arn = el.find("SecondaryNetworkArn")
    if child_secondary_network_arn is not None:
        out["secondary_network_arn"] = str(child_secondary_network_arn.text or "")
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_type = el.find("Type")
    if child_type is not None:
        import aws_sdk_ec2.types.secondary_network_type

        out["type"] = aws_sdk_ec2.types.secondary_network_type.deserialize_ec2_query(
            child_type
        )
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.secondary_network_state

        out["state"] = aws_sdk_ec2.types.secondary_network_state.deserialize_ec2_query(
            child_state
        )
    child_state_reason = el.find("StateReason")
    if child_state_reason is not None:
        out["state_reason"] = str(child_state_reason.text or "")
    if el.find("Ipv4CidrBlockAssociationSet") is not None:
        import aws_sdk_ec2.types.secondary_network_ipv4_cidr_block_association_list

        out["ipv4_cidr_block_associations"] = (
            aws_sdk_ec2.types.secondary_network_ipv4_cidr_block_association_list.deserialize_ec2_query(
                el, "Ipv4CidrBlockAssociationSet"
            )
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
