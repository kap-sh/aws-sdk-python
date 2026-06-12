"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeleteCoreNetworkPrefixListAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.core_network_id
    import aws_sdk_networkmanager.types.prefix_list_arn


class DeleteCoreNetworkPrefixListAssociationRequest(TypedDict):
    core_network_id: "aws_sdk_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of the core network from which to delete the prefix list association.</p>"""
    prefix_list_arn: "aws_sdk_networkmanager.types.prefix_list_arn.PrefixListArn"
    """<p>The ARN of the prefix list to disassociate from the core network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCoreNetworkPrefixListAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCoreNetworkPrefixListAssociationRequest:
    out: DeleteCoreNetworkPrefixListAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
