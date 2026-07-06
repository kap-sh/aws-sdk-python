"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateConnectAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.attachment_id
    import aws_sdk_networkmanager.types.client_token
    import aws_sdk_networkmanager.types.connect_attachment_options
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.core_network_id
    import aws_sdk_networkmanager.types.external_region_code
    import aws_sdk_networkmanager.types.tag_list


class CreateConnectAttachmentRequest(TypedDict, closed=True):
    core_network_id: "aws_sdk_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of a core network where you want to create the attachment. </p>"""
    edge_location: (
        "aws_sdk_networkmanager.types.external_region_code.ExternalRegionCode"
    )
    """<p>The Region where the edge is located.</p>"""
    transport_attachment_id: "aws_sdk_networkmanager.types.attachment_id.AttachmentId"
    """<p>The ID of the attachment between the two connections.</p>"""
    routing_policy_label: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The routing policy label to apply to the Connect attachment for traffic routing decisions.</p>"""
    options: "aws_sdk_networkmanager.types.connect_attachment_options.ConnectAttachmentOptions"
    """<p>Options for creating an attachment.</p>"""
    tags: NotRequired["aws_sdk_networkmanager.types.tag_list.TagList"]
    """<p>The list of key-value tags associated with the request.</p>"""
    client_token: NotRequired["aws_sdk_networkmanager.types.client_token.ClientToken"]
    """<p>The client token associated with the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectAttachmentRequest) -> dict:
    out: dict = {}
    out["CoreNetworkId"] = value["core_network_id"]
    out["EdgeLocation"] = value["edge_location"]
    out["TransportAttachmentId"] = value["transport_attachment_id"]
    if "routing_policy_label" in value:
        out["RoutingPolicyLabel"] = value["routing_policy_label"]
    import aws_sdk_networkmanager.types.connect_attachment_options

    out["Options"] = (
        aws_sdk_networkmanager.types.connect_attachment_options.serialize_json(
            value["options"]
        )
    )
    if "tags" in value:
        import aws_sdk_networkmanager.types.tag_list

        out["Tags"] = aws_sdk_networkmanager.types.tag_list.serialize_json(
            value["tags"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateConnectAttachmentRequest:
    out: CreateConnectAttachmentRequest = {}  # type: ignore[typeddict-item]
    if "CoreNetworkId" in data:
        out["core_network_id"] = data["CoreNetworkId"]
    else:
        raise DeserializationError(
            "CreateConnectAttachmentRequest.core_network_id required"
        )
    if "EdgeLocation" in data:
        out["edge_location"] = data["EdgeLocation"]
    else:
        raise DeserializationError(
            "CreateConnectAttachmentRequest.edge_location required"
        )
    if "TransportAttachmentId" in data:
        out["transport_attachment_id"] = data["TransportAttachmentId"]
    else:
        raise DeserializationError(
            "CreateConnectAttachmentRequest.transport_attachment_id required"
        )
    if "RoutingPolicyLabel" in data:
        out["routing_policy_label"] = data["RoutingPolicyLabel"]
    if "Options" in data:
        import aws_sdk_networkmanager.types.connect_attachment_options

        out["options"] = (
            aws_sdk_networkmanager.types.connect_attachment_options.deserialize_json(
                data["Options"]
            )
        )
    else:
        raise DeserializationError("CreateConnectAttachmentRequest.options required")
    if "Tags" in data:
        import aws_sdk_networkmanager.types.tag_list

        out["tags"] = aws_sdk_networkmanager.types.tag_list.deserialize_json(
            data["Tags"]
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
