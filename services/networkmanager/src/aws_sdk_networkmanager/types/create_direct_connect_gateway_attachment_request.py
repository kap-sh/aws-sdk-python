"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateDirectConnectGatewayAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.client_token
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.core_network_id
    import aws_sdk_networkmanager.types.direct_connect_gateway_arn
    import aws_sdk_networkmanager.types.external_region_code_list
    import aws_sdk_networkmanager.types.tag_list


class CreateDirectConnectGatewayAttachmentRequest(TypedDict, closed=True):
    core_network_id: "aws_sdk_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of the Cloud WAN core network that the Direct Connect gateway attachment should be attached to.</p>"""
    direct_connect_gateway_arn: "aws_sdk_networkmanager.types.direct_connect_gateway_arn.DirectConnectGatewayArn"
    """<p>The ARN of the Direct Connect gateway attachment.</p>"""
    routing_policy_label: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The routing policy label to apply to the Direct Connect Gateway attachment for traffic routing decisions.</p>"""
    edge_locations: (
        "aws_sdk_networkmanager.types.external_region_code_list.ExternalRegionCodeList"
    )
    """<p>One or more core network edge locations that the Direct Connect gateway attachment is associated with. </p>"""
    tags: NotRequired["aws_sdk_networkmanager.types.tag_list.TagList"]
    """<p>The key value tags to apply to the Direct Connect gateway attachment during creation.</p>"""
    client_token: NotRequired["aws_sdk_networkmanager.types.client_token.ClientToken"]
    """<p>client token</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDirectConnectGatewayAttachmentRequest) -> dict:
    out: dict = {}
    out["CoreNetworkId"] = value["core_network_id"]
    out["DirectConnectGatewayArn"] = value["direct_connect_gateway_arn"]
    if "routing_policy_label" in value:
        out["RoutingPolicyLabel"] = value["routing_policy_label"]
    import aws_sdk_networkmanager.types.external_region_code_list

    out["EdgeLocations"] = (
        aws_sdk_networkmanager.types.external_region_code_list.serialize_json(
            value["edge_locations"]
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


def deserialize_json(data: dict) -> CreateDirectConnectGatewayAttachmentRequest:
    out: CreateDirectConnectGatewayAttachmentRequest = {}  # type: ignore[typeddict-item]
    if "CoreNetworkId" in data:
        out["core_network_id"] = data["CoreNetworkId"]
    else:
        raise DeserializationError(
            "CreateDirectConnectGatewayAttachmentRequest.core_network_id required"
        )
    if "DirectConnectGatewayArn" in data:
        out["direct_connect_gateway_arn"] = data["DirectConnectGatewayArn"]
    else:
        raise DeserializationError(
            "CreateDirectConnectGatewayAttachmentRequest.direct_connect_gateway_arn required"
        )
    if "RoutingPolicyLabel" in data:
        out["routing_policy_label"] = data["RoutingPolicyLabel"]
    if "EdgeLocations" in data:
        import aws_sdk_networkmanager.types.external_region_code_list

        out["edge_locations"] = (
            aws_sdk_networkmanager.types.external_region_code_list.deserialize_json(
                data["EdgeLocations"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDirectConnectGatewayAttachmentRequest.edge_locations required"
        )
    if "Tags" in data:
        import aws_sdk_networkmanager.types.tag_list

        out["tags"] = aws_sdk_networkmanager.types.tag_list.deserialize_json(
            data["Tags"]
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
