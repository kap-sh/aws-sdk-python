"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectPeer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment_id
    import capo_networkmanager.types.connect_peer_configuration
    import capo_networkmanager.types.connect_peer_error_list
    import capo_networkmanager.types.connect_peer_id
    import capo_networkmanager.types.connect_peer_state
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.date_time
    import capo_networkmanager.types.external_region_code
    import capo_networkmanager.types.subnet_arn
    import capo_networkmanager.types.tag_list


class ConnectPeer(TypedDict, closed=True):
    core_network_id: NotRequired[
        "capo_networkmanager.types.core_network_id.CoreNetworkId"
    ]
    """<p>The ID of a core network.</p>"""
    connect_attachment_id: NotRequired[
        "capo_networkmanager.types.attachment_id.AttachmentId"
    ]
    """<p>The ID of the attachment to connect.</p>"""
    connect_peer_id: NotRequired[
        "capo_networkmanager.types.connect_peer_id.ConnectPeerId"
    ]
    """<p>The ID of the Connect peer.</p>"""
    edge_location: NotRequired[
        "capo_networkmanager.types.external_region_code.ExternalRegionCode"
    ]
    """<p>The Connect peer Regions where edges are located.</p>"""
    state: NotRequired["capo_networkmanager.types.connect_peer_state.ConnectPeerState"]
    """<p>The state of the Connect peer.</p>"""
    created_at: NotRequired["capo_networkmanager.types.date_time.DateTime"]
    """<p>The timestamp when the Connect peer was created.</p>"""
    configuration: NotRequired[
        "capo_networkmanager.types.connect_peer_configuration.ConnectPeerConfiguration"
    ]
    """<p>The configuration of the Connect peer.</p>"""
    tags: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>The list of key-value tags associated with the Connect peer.</p>"""
    subnet_arn: NotRequired["capo_networkmanager.types.subnet_arn.SubnetArn"]
    """<p>The subnet ARN for the Connect peer. This only applies only when the protocol is NO_ENCAP.</p>"""
    last_modification_errors: NotRequired[
        "capo_networkmanager.types.connect_peer_error_list.ConnectPeerErrorList"
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
        import capo_networkmanager.types.connect_peer_state

        out["State"] = capo_networkmanager.types.connect_peer_state.serialize_json(
            value["state"]
        )
    if "created_at" in value:
        import capo_networkmanager.types.date_time

        out["CreatedAt"] = capo_networkmanager.types.date_time.serialize_json(
            value["created_at"]
        )
    if "configuration" in value:
        import capo_networkmanager.types.connect_peer_configuration

        out["Configuration"] = (
            capo_networkmanager.types.connect_peer_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "tags" in value:
        import capo_networkmanager.types.tag_list

        out["Tags"] = capo_networkmanager.types.tag_list.serialize_json(value["tags"])
    if "subnet_arn" in value:
        out["SubnetArn"] = value["subnet_arn"]
    if "last_modification_errors" in value:
        import capo_networkmanager.types.connect_peer_error_list

        out["LastModificationErrors"] = (
            capo_networkmanager.types.connect_peer_error_list.serialize_json(
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
        import capo_networkmanager.types.connect_peer_state

        out["state"] = capo_networkmanager.types.connect_peer_state.deserialize_json(
            data["State"]
        )
    if "CreatedAt" in data:
        import capo_networkmanager.types.date_time

        out["created_at"] = capo_networkmanager.types.date_time.deserialize_json(
            data["CreatedAt"]
        )
    if "Configuration" in data:
        import capo_networkmanager.types.connect_peer_configuration

        out["configuration"] = (
            capo_networkmanager.types.connect_peer_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    if "Tags" in data:
        import capo_networkmanager.types.tag_list

        out["tags"] = capo_networkmanager.types.tag_list.deserialize_json(data["Tags"])
    if "SubnetArn" in data:
        out["subnet_arn"] = data["SubnetArn"]
    if "LastModificationErrors" in data:
        import capo_networkmanager.types.connect_peer_error_list

        out["last_modification_errors"] = (
            capo_networkmanager.types.connect_peer_error_list.deserialize_json(
                data["LastModificationErrors"]
            )
        )
    return out
