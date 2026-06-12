"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateCoreNetworkPrefixListAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.client_token
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.core_network_id
    import aws_sdk_networkmanager.types.prefix_list_arn


class CreateCoreNetworkPrefixListAssociationRequest(TypedDict):
    core_network_id: "aws_sdk_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of the core network to associate with the prefix list.</p>"""
    prefix_list_arn: "aws_sdk_networkmanager.types.prefix_list_arn.PrefixListArn"
    """<p>The ARN of the prefix list to associate with the core network.</p>"""
    prefix_list_alias: (
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    )
    """<p>An optional alias for the prefix list association.</p>"""
    client_token: NotRequired["aws_sdk_networkmanager.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCoreNetworkPrefixListAssociationRequest) -> dict:
    out: dict = {}
    out["CoreNetworkId"] = value["core_network_id"]
    out["PrefixListArn"] = value["prefix_list_arn"]
    out["PrefixListAlias"] = value["prefix_list_alias"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateCoreNetworkPrefixListAssociationRequest:
    out: CreateCoreNetworkPrefixListAssociationRequest = {}  # type: ignore[typeddict-item]
    if "CoreNetworkId" in data:
        out["core_network_id"] = data["CoreNetworkId"]
    else:
        raise DeserializationError(
            "CreateCoreNetworkPrefixListAssociationRequest.core_network_id required"
        )
    if "PrefixListArn" in data:
        out["prefix_list_arn"] = data["PrefixListArn"]
    else:
        raise DeserializationError(
            "CreateCoreNetworkPrefixListAssociationRequest.prefix_list_arn required"
        )
    if "PrefixListAlias" in data:
        out["prefix_list_alias"] = data["PrefixListAlias"]
    else:
        raise DeserializationError(
            "CreateCoreNetworkPrefixListAssociationRequest.prefix_list_alias required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
