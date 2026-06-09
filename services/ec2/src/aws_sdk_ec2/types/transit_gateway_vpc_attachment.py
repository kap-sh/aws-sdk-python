"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayVpcAttachment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.transit_gateway_attachment_state
    import aws_sdk_ec2.types.transit_gateway_vpc_attachment_options
    import aws_sdk_ec2.types.value_string_list


class TransitGatewayVpcAttachment(TypedDict):
    transit_gateway_attachment_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the attachment.</p>"""
    transit_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""
    vpc_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the VPC.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_state.TransitGatewayAttachmentState"
    ]
    """<p>The state of the VPC attachment. Note that the <code>initiating</code> state has been deprecated.</p>"""
    subnet_ids: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The IDs of the subnets.</p>"""
    creation_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The creation time.</p>"""
    options: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_vpc_attachment_options.TransitGatewayVpcAttachmentOptions"
    ]
    """<p>The VPC attachment options.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags for the VPC attachment.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayVpcAttachment, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "transit_gateway_id" in value:
        pairs.append((f"{prefix}.TransitGatewayId", str(value["transit_gateway_id"])))
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "vpc_owner_id" in value:
        pairs.append((f"{prefix}.VpcOwnerId", str(value["vpc_owner_id"])))
    if "state" in value:
        import aws_sdk_ec2.types.transit_gateway_attachment_state

        aws_sdk_ec2.types.transit_gateway_attachment_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "subnet_ids" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["subnet_ids"], pairs, f"{prefix}.SubnetIds"
        )
    if "creation_time" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["creation_time"], pairs, f"{prefix}.CreationTime"
        )
    if "options" in value:
        import aws_sdk_ec2.types.transit_gateway_vpc_attachment_options

        aws_sdk_ec2.types.transit_gateway_vpc_attachment_options.serialize_ec2_query(
            value["options"], pairs, f"{prefix}.Options"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayVpcAttachment:
    out: TransitGatewayVpcAttachment = {}  # type: ignore[typeddict-item]
    child_transit_gateway_attachment_id = el.find("TransitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_vpc_owner_id = el.find("VpcOwnerId")
    if child_vpc_owner_id is not None:
        out["vpc_owner_id"] = str(child_vpc_owner_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.transit_gateway_attachment_state

        out["state"] = (
            aws_sdk_ec2.types.transit_gateway_attachment_state.deserialize_ec2_query(
                child_state
            )
        )
    if el.find("SubnetIds") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["subnet_ids"] = aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
            el, "SubnetIds"
        )
    child_creation_time = el.find("CreationTime")
    if child_creation_time is not None:
        import aws_sdk_ec2.types.date_time

        out["creation_time"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_creation_time
        )
    child_options = el.find("Options")
    if child_options is not None:
        import aws_sdk_ec2.types.transit_gateway_vpc_attachment_options

        out["options"] = (
            aws_sdk_ec2.types.transit_gateway_vpc_attachment_options.deserialize_ec2_query(
                child_options
            )
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
