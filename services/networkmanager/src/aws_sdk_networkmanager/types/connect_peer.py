"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectPeer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.attachment_id
    import aws_sdk_networkmanager.types.connect_peer_configuration
    import aws_sdk_networkmanager.types.connect_peer_error_list
    import aws_sdk_networkmanager.types.connect_peer_id
    import aws_sdk_networkmanager.types.connect_peer_state
    import aws_sdk_networkmanager.types.core_network_id
    import aws_sdk_networkmanager.types.date_time
    import aws_sdk_networkmanager.types.external_region_code
    import aws_sdk_networkmanager.types.subnet_arn
    import aws_sdk_networkmanager.types.tag_list


class ConnectPeer(TypedDict):
    core_network_id: NotRequired[
        "aws_sdk_networkmanager.types.core_network_id.CoreNetworkId"
    ]
    """<p>The ID of a core network.</p>"""
    connect_attachment_id: NotRequired[
        "aws_sdk_networkmanager.types.attachment_id.AttachmentId"
    ]
    """<p>The ID of the attachment to connect.</p>"""
    connect_peer_id: NotRequired[
        "aws_sdk_networkmanager.types.connect_peer_id.ConnectPeerId"
    ]
    """<p>The ID of the Connect peer.</p>"""
    edge_location: NotRequired[
        "aws_sdk_networkmanager.types.external_region_code.ExternalRegionCode"
    ]
    """<p>The Connect peer Regions where edges are located.</p>"""
    state: NotRequired[
        "aws_sdk_networkmanager.types.connect_peer_state.ConnectPeerState"
    ]
    """<p>The state of the Connect peer.</p>"""
    created_at: NotRequired["aws_sdk_networkmanager.types.date_time.DateTime"]
    """<p>The timestamp when the Connect peer was created.</p>"""
    configuration: NotRequired[
        "aws_sdk_networkmanager.types.connect_peer_configuration.ConnectPeerConfiguration"
    ]
    """<p>The configuration of the Connect peer.</p>"""
    tags: NotRequired["aws_sdk_networkmanager.types.tag_list.TagList"]
    """<p>The list of key-value tags associated with the Connect peer.</p>"""
    subnet_arn: NotRequired["aws_sdk_networkmanager.types.subnet_arn.SubnetArn"]
    """<p>The subnet ARN for the Connect peer. This only applies only when the protocol is NO_ENCAP.</p>"""
    last_modification_errors: NotRequired[
        "aws_sdk_networkmanager.types.connect_peer_error_list.ConnectPeerErrorList"
    ]
    """<p>Describes the error associated with the attachment request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectPeer) -> dict:
    out: dict = {}
    if "core_network_id" in value:
        out["CoreNetworkId"] = value["core_network_id"]
    if "connect_attachment_id" in value:
        out["ConnectAttachmentId"] = value["connect_attachment_id"]
    if "connect_peer_id" in value:
        out["ConnectPeerId"] = value["connect_peer_id"]
    if "edge_location" in value:
        out["EdgeLocation"] = value["edge_location"]
    if "state" in value:
        import aws_sdk_networkmanager.types.connect_peer_state

        out["State"] = aws_sdk_networkmanager.types.connect_peer_state.serialize_json(
            value["state"]
        )
    if "created_at" in value:
        import aws_sdk_networkmanager.types.date_time

        out["CreatedAt"] = aws_sdk_networkmanager.types.date_time.serialize_json(
            value["created_at"]
        )
    if "configuration" in value:
        import aws_sdk_networkmanager.types.connect_peer_configuration

        out["Configuration"] = (
            aws_sdk_networkmanager.types.connect_peer_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "tags" in value:
        import aws_sdk_networkmanager.types.tag_list

        out["Tags"] = aws_sdk_networkmanager.types.tag_list.serialize_json(
            value["tags"]
        )
    if "subnet_arn" in value:
        out["SubnetArn"] = value["subnet_arn"]
    if "last_modification_errors" in value:
        import aws_sdk_networkmanager.types.connect_peer_error_list

        out["LastModificationErrors"] = (
            aws_sdk_networkmanager.types.connect_peer_error_list.serialize_json(
                value["last_modification_errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectPeer:
    out: ConnectPeer = {}  # type: ignore[typeddict-item]
    if "CoreNetworkId" in data:
        out["core_network_id"] = data["CoreNetworkId"]
    if "ConnectAttachmentId" in data:
        out["connect_attachment_id"] = data["ConnectAttachmentId"]
    if "ConnectPeerId" in data:
        out["connect_peer_id"] = data["ConnectPeerId"]
    if "EdgeLocation" in data:
        out["edge_location"] = data["EdgeLocation"]
    if "State" in data:
        import aws_sdk_networkmanager.types.connect_peer_state

        out["state"] = aws_sdk_networkmanager.types.connect_peer_state.deserialize_json(
            data["State"]
        )
    if "CreatedAt" in data:
        import aws_sdk_networkmanager.types.date_time

        out["created_at"] = aws_sdk_networkmanager.types.date_time.deserialize_json(
            data["CreatedAt"]
        )
    if "Configuration" in data:
        import aws_sdk_networkmanager.types.connect_peer_configuration

        out["configuration"] = (
            aws_sdk_networkmanager.types.connect_peer_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    if "Tags" in data:
        import aws_sdk_networkmanager.types.tag_list

        out["tags"] = aws_sdk_networkmanager.types.tag_list.deserialize_json(
            data["Tags"]
        )
    if "SubnetArn" in data:
        out["subnet_arn"] = data["SubnetArn"]
    if "LastModificationErrors" in data:
        import aws_sdk_networkmanager.types.connect_peer_error_list

        out["last_modification_errors"] = (
            aws_sdk_networkmanager.types.connect_peer_error_list.deserialize_json(
                data["LastModificationErrors"]
            )
        )
    return out
