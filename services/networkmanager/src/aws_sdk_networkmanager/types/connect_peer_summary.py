"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectPeerSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.attachment_id
    import aws_sdk_networkmanager.types.connect_peer_id
    import aws_sdk_networkmanager.types.connect_peer_state
    import aws_sdk_networkmanager.types.core_network_id
    import aws_sdk_networkmanager.types.date_time
    import aws_sdk_networkmanager.types.external_region_code
    import aws_sdk_networkmanager.types.subnet_arn
    import aws_sdk_networkmanager.types.tag_list


class ConnectPeerSummary(TypedDict, closed=True):
    core_network_id: NotRequired[
        "aws_sdk_networkmanager.types.core_network_id.CoreNetworkId"
    ]
    """<p>The ID of a core network.</p>"""
    connect_attachment_id: NotRequired[
        "aws_sdk_networkmanager.types.attachment_id.AttachmentId"
    ]
    """<p>The ID of a Connect peer attachment.</p>"""
    connect_peer_id: NotRequired[
        "aws_sdk_networkmanager.types.connect_peer_id.ConnectPeerId"
    ]
    """<p>The ID of a Connect peer.</p>"""
    edge_location: NotRequired[
        "aws_sdk_networkmanager.types.external_region_code.ExternalRegionCode"
    ]
    """<p>The Region where the edge is located.</p>"""
    connect_peer_state: NotRequired[
        "aws_sdk_networkmanager.types.connect_peer_state.ConnectPeerState"
    ]
    """<p>The state of a Connect peer.</p>"""
    created_at: NotRequired["aws_sdk_networkmanager.types.date_time.DateTime"]
    """<p>The timestamp when a Connect peer was created.</p>"""
    tags: NotRequired["aws_sdk_networkmanager.types.tag_list.TagList"]
    """<p>The list of key-value tags associated with the Connect peer summary.</p>"""
    subnet_arn: NotRequired["aws_sdk_networkmanager.types.subnet_arn.SubnetArn"]
    """<p>The subnet ARN for the Connect peer summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectPeerSummary) -> dict:
    out: dict = {}
    if "core_network_id" in value:
        out["CoreNetworkId"] = value["core_network_id"]
    if "connect_attachment_id" in value:
        out["ConnectAttachmentId"] = value["connect_attachment_id"]
    if "connect_peer_id" in value:
        out["ConnectPeerId"] = value["connect_peer_id"]
    if "edge_location" in value:
        out["EdgeLocation"] = value["edge_location"]
    if "connect_peer_state" in value:
        import aws_sdk_networkmanager.types.connect_peer_state

        out["ConnectPeerState"] = (
            aws_sdk_networkmanager.types.connect_peer_state.serialize_json(
                value["connect_peer_state"]
            )
        )
    if "created_at" in value:
        import aws_sdk_networkmanager.types.date_time

        out["CreatedAt"] = aws_sdk_networkmanager.types.date_time.serialize_json(
            value["created_at"]
        )
    if "tags" in value:
        import aws_sdk_networkmanager.types.tag_list

        out["Tags"] = aws_sdk_networkmanager.types.tag_list.serialize_json(
            value["tags"]
        )
    if "subnet_arn" in value:
        out["SubnetArn"] = value["subnet_arn"]
    return out


def deserialize_json(data: dict) -> ConnectPeerSummary:
    out: ConnectPeerSummary = {}  # type: ignore[typeddict-item]
    if "CoreNetworkId" in data:
        out["core_network_id"] = data["CoreNetworkId"]
    if "ConnectAttachmentId" in data:
        out["connect_attachment_id"] = data["ConnectAttachmentId"]
    if "ConnectPeerId" in data:
        out["connect_peer_id"] = data["ConnectPeerId"]
    if "EdgeLocation" in data:
        out["edge_location"] = data["EdgeLocation"]
    if "ConnectPeerState" in data:
        import aws_sdk_networkmanager.types.connect_peer_state

        out["connect_peer_state"] = (
            aws_sdk_networkmanager.types.connect_peer_state.deserialize_json(
                data["ConnectPeerState"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_networkmanager.types.date_time

        out["created_at"] = aws_sdk_networkmanager.types.date_time.deserialize_json(
            data["CreatedAt"]
        )
    if "Tags" in data:
        import aws_sdk_networkmanager.types.tag_list

        out["tags"] = aws_sdk_networkmanager.types.tag_list.deserialize_json(
            data["Tags"]
        )
    if "SubnetArn" in data:
        out["subnet_arn"] = data["SubnetArn"]
    return out
