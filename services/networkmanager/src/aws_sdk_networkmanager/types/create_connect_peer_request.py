"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateConnectPeerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.attachment_id
    import aws_sdk_networkmanager.types.bgp_options
    import aws_sdk_networkmanager.types.client_token
    import aws_sdk_networkmanager.types.constrained_string_list
    import aws_sdk_networkmanager.types.ip_address
    import aws_sdk_networkmanager.types.subnet_arn
    import aws_sdk_networkmanager.types.tag_list


class CreateConnectPeerRequest(TypedDict, closed=True):
    connect_attachment_id: "aws_sdk_networkmanager.types.attachment_id.AttachmentId"
    """<p>The ID of the connection attachment.</p>"""
    core_network_address: NotRequired[
        "aws_sdk_networkmanager.types.ip_address.IPAddress"
    ]
    """<p>A Connect peer core network address. This only applies only when the protocol is <code>GRE</code>.</p>"""
    peer_address: "aws_sdk_networkmanager.types.ip_address.IPAddress"
    """<p>The Connect peer address.</p>"""
    bgp_options: NotRequired["aws_sdk_networkmanager.types.bgp_options.BgpOptions"]
    """<p>The Connect peer BGP options. This only applies only when the protocol is <code>GRE</code>.</p>"""
    inside_cidr_blocks: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>The inside IP addresses used for BGP peering.</p>"""
    tags: NotRequired["aws_sdk_networkmanager.types.tag_list.TagList"]
    """<p>The tags associated with the peer request.</p>"""
    client_token: NotRequired["aws_sdk_networkmanager.types.client_token.ClientToken"]
    """<p>The client token associated with the request.</p>"""
    subnet_arn: NotRequired["aws_sdk_networkmanager.types.subnet_arn.SubnetArn"]
    """<p>The subnet ARN for the Connect peer. This only applies only when the protocol is NO_ENCAP.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectPeerRequest) -> dict:
    out: dict = {}
    out["ConnectAttachmentId"] = value["connect_attachment_id"]
    if "core_network_address" in value:
        out["CoreNetworkAddress"] = value["core_network_address"]
    out["PeerAddress"] = value["peer_address"]
    if "bgp_options" in value:
        import aws_sdk_networkmanager.types.bgp_options

        out["BgpOptions"] = aws_sdk_networkmanager.types.bgp_options.serialize_json(
            value["bgp_options"]
        )
    if "inside_cidr_blocks" in value:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["InsideCidrBlocks"] = (
            aws_sdk_networkmanager.types.constrained_string_list.serialize_json(
                value["inside_cidr_blocks"]
            )
        )
    if "tags" in value:
        import aws_sdk_networkmanager.types.tag_list

        out["Tags"] = aws_sdk_networkmanager.types.tag_list.serialize_json(
            value["tags"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "subnet_arn" in value:
        out["SubnetArn"] = value["subnet_arn"]
    return out


def deserialize_json(data: dict) -> CreateConnectPeerRequest:
    out: CreateConnectPeerRequest = {}  # type: ignore[typeddict-item]
    if "ConnectAttachmentId" in data:
        out["connect_attachment_id"] = data["ConnectAttachmentId"]
    else:
        raise DeserializationError(
            "CreateConnectPeerRequest.connect_attachment_id required"
        )
    if "CoreNetworkAddress" in data:
        out["core_network_address"] = data["CoreNetworkAddress"]
    if "PeerAddress" in data:
        out["peer_address"] = data["PeerAddress"]
    else:
        raise DeserializationError("CreateConnectPeerRequest.peer_address required")
    if "BgpOptions" in data:
        import aws_sdk_networkmanager.types.bgp_options

        out["bgp_options"] = aws_sdk_networkmanager.types.bgp_options.deserialize_json(
            data["BgpOptions"]
        )
    if "InsideCidrBlocks" in data:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["inside_cidr_blocks"] = (
            aws_sdk_networkmanager.types.constrained_string_list.deserialize_json(
                data["InsideCidrBlocks"]
            )
        )
    if "Tags" in data:
        import aws_sdk_networkmanager.types.tag_list

        out["tags"] = aws_sdk_networkmanager.types.tag_list.deserialize_json(
            data["Tags"]
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "SubnetArn" in data:
        out["subnet_arn"] = data["SubnetArn"]
    return out
