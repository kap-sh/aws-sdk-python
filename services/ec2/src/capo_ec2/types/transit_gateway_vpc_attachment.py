"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayVpcAttachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.transit_gateway_attachment_state
    import capo_ec2.types.transit_gateway_vpc_attachment_options
    import capo_ec2.types.value_string_list


class TransitGatewayVpcAttachment(TypedDict, closed=True):
    transit_gateway_attachment_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the attachment.</p>"""
    transit_gateway_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the transit gateway.</p>"""
    vpc_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""
    vpc_owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the VPC.</p>"""
    state: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_state.TransitGatewayAttachmentState"
    ]
    """<p>The state of the VPC attachment. Note that the <code>initiating</code> state has been deprecated.</p>"""
    subnet_ids: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The IDs of the subnets.</p>"""
    creation_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The creation time.</p>"""
    options: NotRequired[
        "capo_ec2.types.transit_gateway_vpc_attachment_options.TransitGatewayVpcAttachmentOptions"
    ]
    """<p>The VPC attachment options.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags for the VPC attachment.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayVpcAttachment, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "transit_gateway_id" in value:
        pairs.append(
            (f"{key_prefix}TransitGatewayId", str(value["transit_gateway_id"]))
        )
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "vpc_owner_id" in value:
        pairs.append((f"{key_prefix}VpcOwnerId", str(value["vpc_owner_id"])))
    if "state" in value:
        import capo_ec2.types.transit_gateway_attachment_state

        capo_ec2.types.transit_gateway_attachment_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "subnet_ids" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["subnet_ids"], pairs, f"{key_prefix}SubnetIds"
        )
    if "creation_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["creation_time"], pairs, f"{key_prefix}CreationTime"
        )
    if "options" in value:
        import capo_ec2.types.transit_gateway_vpc_attachment_options

        capo_ec2.types.transit_gateway_vpc_attachment_options.serialize_ec2_query(
            value["options"], pairs, f"{key_prefix}Options"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayVpcAttachment:
    out: TransitGatewayVpcAttachment = {}  # type: ignore[typeddict-item]
    child_transit_gateway_attachment_id = el.find("transitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
    child_transit_gateway_id = el.find("transitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_vpc_id = el.find("vpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_vpc_owner_id = el.find("vpcOwnerId")
    if child_vpc_owner_id is not None:
        out["vpc_owner_id"] = str(child_vpc_owner_id.text or "")
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.transit_gateway_attachment_state

        out["state"] = (
            capo_ec2.types.transit_gateway_attachment_state.deserialize_ec2_query(
                child_state
            )
        )
    if el.find("subnetIds") is not None:
        import capo_ec2.types.value_string_list

        out["subnet_ids"] = capo_ec2.types.value_string_list.deserialize_ec2_query(
            el, "subnetIds"
        )
    child_creation_time = el.find("creationTime")
    if child_creation_time is not None:
        import capo_ec2.types.date_time

        out["creation_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_creation_time
        )
    child_options = el.find("options")
    if child_options is not None:
        import capo_ec2.types.transit_gateway_vpc_attachment_options

        out["options"] = (
            capo_ec2.types.transit_gateway_vpc_attachment_options.deserialize_ec2_query(
                child_options
            )
        )
    if el.find("tagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "tagSet")
    return out
