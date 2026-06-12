"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateSiteToSiteVpnAttachmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.client_token
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.core_network_id
    import aws_sdk_networkmanager.types.tag_list
    import aws_sdk_networkmanager.types.vpn_connection_arn


class CreateSiteToSiteVpnAttachmentRequest(TypedDict):
    core_network_id: "aws_sdk_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of a core network where you're creating a site-to-site VPN attachment.</p>"""
    vpn_connection_arn: (
        "aws_sdk_networkmanager.types.vpn_connection_arn.VpnConnectionArn"
    )
    """<p>The ARN identifying the VPN attachment.</p>"""
    routing_policy_label: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The routing policy label to apply to the Site-to-Site VPN attachment for traffic routing decisions.</p>"""
    tags: NotRequired["aws_sdk_networkmanager.types.tag_list.TagList"]
    """<p>The tags associated with the request.</p>"""
    client_token: NotRequired["aws_sdk_networkmanager.types.client_token.ClientToken"]
    """<p>The client token associated with the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSiteToSiteVpnAttachmentRequest) -> dict:
    out: dict = {}
    out["CoreNetworkId"] = value["core_network_id"]
    out["VpnConnectionArn"] = value["vpn_connection_arn"]
    if "routing_policy_label" in value:
        out["RoutingPolicyLabel"] = value["routing_policy_label"]
    if "tags" in value:
        import aws_sdk_networkmanager.types.tag_list

        out["Tags"] = aws_sdk_networkmanager.types.tag_list.serialize_json(
            value["tags"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateSiteToSiteVpnAttachmentRequest:
    out: CreateSiteToSiteVpnAttachmentRequest = {}  # type: ignore[typeddict-item]
    if "CoreNetworkId" in data:
        out["core_network_id"] = data["CoreNetworkId"]
    else:
        raise DeserializationError(
            "CreateSiteToSiteVpnAttachmentRequest.core_network_id required"
        )
    if "VpnConnectionArn" in data:
        out["vpn_connection_arn"] = data["VpnConnectionArn"]
    else:
        raise DeserializationError(
            "CreateSiteToSiteVpnAttachmentRequest.vpn_connection_arn required"
        )
    if "RoutingPolicyLabel" in data:
        out["routing_policy_label"] = data["RoutingPolicyLabel"]
    if "Tags" in data:
        import aws_sdk_networkmanager.types.tag_list

        out["tags"] = aws_sdk_networkmanager.types.tag_list.deserialize_json(
            data["Tags"]
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
