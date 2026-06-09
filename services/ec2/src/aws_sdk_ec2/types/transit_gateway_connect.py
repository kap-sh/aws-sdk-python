"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayConnect``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.transit_gateway_attachment_id
    import aws_sdk_ec2.types.transit_gateway_attachment_state
    import aws_sdk_ec2.types.transit_gateway_connect_options
    import aws_sdk_ec2.types.transit_gateway_id


class TransitGatewayConnect(TypedDict):
    transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the Connect attachment.</p>"""
    transport_transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the attachment from which the Connect attachment was created.</p>"""
    transit_gateway_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the transit gateway.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_state.TransitGatewayAttachmentState"
    ]
    """<p>The state of the attachment.</p>"""
    creation_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The creation time.</p>"""
    options: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_connect_options.TransitGatewayConnectOptions"
    ]
    """<p>The Connect attachment options.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags for the attachment.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayConnect, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "transport_transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{prefix}.TransportTransitGatewayAttachmentId",
                str(value["transport_transit_gateway_attachment_id"]),
            )
        )
    if "transit_gateway_id" in value:
        pairs.append((f"{prefix}.TransitGatewayId", str(value["transit_gateway_id"])))
    if "state" in value:
        import aws_sdk_ec2.types.transit_gateway_attachment_state

        aws_sdk_ec2.types.transit_gateway_attachment_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "creation_time" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["creation_time"], pairs, f"{prefix}.CreationTime"
        )
    if "options" in value:
        import aws_sdk_ec2.types.transit_gateway_connect_options

        aws_sdk_ec2.types.transit_gateway_connect_options.serialize_ec2_query(
            value["options"], pairs, f"{prefix}.Options"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayConnect:
    out: TransitGatewayConnect = {}  # type: ignore[typeddict-item]
    child_transit_gateway_attachment_id = el.find("TransitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
    child_transport_transit_gateway_attachment_id = el.find(
        "TransportTransitGatewayAttachmentId"
    )
    if child_transport_transit_gateway_attachment_id is not None:
        out["transport_transit_gateway_attachment_id"] = str(
            child_transport_transit_gateway_attachment_id.text or ""
        )
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.transit_gateway_attachment_state

        out["state"] = (
            aws_sdk_ec2.types.transit_gateway_attachment_state.deserialize_ec2_query(
                child_state
            )
        )
    child_creation_time = el.find("CreationTime")
    if child_creation_time is not None:
        import aws_sdk_ec2.types.date_time

        out["creation_time"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_creation_time
        )
    child_options = el.find("Options")
    if child_options is not None:
        import aws_sdk_ec2.types.transit_gateway_connect_options

        out["options"] = (
            aws_sdk_ec2.types.transit_gateway_connect_options.deserialize_ec2_query(
                child_options
            )
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
