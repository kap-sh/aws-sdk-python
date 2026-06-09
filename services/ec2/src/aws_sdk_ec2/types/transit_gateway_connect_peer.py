"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayConnectPeer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.transit_gateway_attachment_id
    import aws_sdk_ec2.types.transit_gateway_connect_peer_configuration
    import aws_sdk_ec2.types.transit_gateway_connect_peer_id
    import aws_sdk_ec2.types.transit_gateway_connect_peer_state


class TransitGatewayConnectPeer(TypedDict):
    transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the Connect attachment.</p>"""
    transit_gateway_connect_peer_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_connect_peer_id.TransitGatewayConnectPeerId"
    ]
    """<p>The ID of the Connect peer.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_connect_peer_state.TransitGatewayConnectPeerState"
    ]
    """<p>The state of the Connect peer.</p>"""
    creation_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The creation time.</p>"""
    connect_peer_configuration: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_connect_peer_configuration.TransitGatewayConnectPeerConfiguration"
    ]
    """<p>The Connect peer details.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags for the Connect peer.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayConnectPeer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "transit_gateway_connect_peer_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayConnectPeerId",
                str(value["transit_gateway_connect_peer_id"]),
            )
        )
    if "state" in value:
        import aws_sdk_ec2.types.transit_gateway_connect_peer_state

        aws_sdk_ec2.types.transit_gateway_connect_peer_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "creation_time" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["creation_time"], pairs, f"{prefix}.CreationTime"
        )
    if "connect_peer_configuration" in value:
        import aws_sdk_ec2.types.transit_gateway_connect_peer_configuration

        aws_sdk_ec2.types.transit_gateway_connect_peer_configuration.serialize_ec2_query(
            value["connect_peer_configuration"],
            pairs,
            f"{prefix}.ConnectPeerConfiguration",
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayConnectPeer:
    out: TransitGatewayConnectPeer = {}  # type: ignore[typeddict-item]
    child_transit_gateway_attachment_id = el.find("TransitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
    child_transit_gateway_connect_peer_id = el.find("TransitGatewayConnectPeerId")
    if child_transit_gateway_connect_peer_id is not None:
        out["transit_gateway_connect_peer_id"] = str(
            child_transit_gateway_connect_peer_id.text or ""
        )
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.transit_gateway_connect_peer_state

        out["state"] = (
            aws_sdk_ec2.types.transit_gateway_connect_peer_state.deserialize_ec2_query(
                child_state
            )
        )
    child_creation_time = el.find("CreationTime")
    if child_creation_time is not None:
        import aws_sdk_ec2.types.date_time

        out["creation_time"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_creation_time
        )
    child_connect_peer_configuration = el.find("ConnectPeerConfiguration")
    if child_connect_peer_configuration is not None:
        import aws_sdk_ec2.types.transit_gateway_connect_peer_configuration

        out["connect_peer_configuration"] = (
            aws_sdk_ec2.types.transit_gateway_connect_peer_configuration.deserialize_ec2_query(
                child_connect_peer_configuration
            )
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
