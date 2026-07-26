"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeleteCoreNetworkPrefixListAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.prefix_list_arn


class DeleteCoreNetworkPrefixListAssociationResponse(TypedDict, closed=True):
    core_network_id: NotRequired[
        "capo_networkmanager.types.core_network_id.CoreNetworkId"
    ]
    """<p>The ID of the core network from which the prefix list association was deleted.</p>"""
    prefix_list_arn: NotRequired[
        "capo_networkmanager.types.prefix_list_arn.PrefixListArn"
    ]
    """<p>The ARN of the prefix list that was disassociated from the core network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCoreNetworkPrefixListAssociationResponse) -> dict:
    out: dict = {}
    if "core_network_id" in value:
        out["CoreNetworkId"] = value["core_network_id"]
    if "prefix_list_arn" in value:
        out["PrefixListArn"] = value["prefix_list_arn"]
    return out


def deserialize_json(data: dict) -> DeleteCoreNetworkPrefixListAssociationResponse:
    out: DeleteCoreNetworkPrefixListAssociationResponse = {}  # type: ignore[typeddict-item]
    if "CoreNetworkId" in data:
        out["core_network_id"] = data["CoreNetworkId"]
    if "PrefixListArn" in data:
        out["prefix_list_arn"] = data["PrefixListArn"]
    return out
