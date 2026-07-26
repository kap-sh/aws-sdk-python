"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateCoreNetworkPrefixListAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.prefix_list_arn


class CreateCoreNetworkPrefixListAssociationResponse(TypedDict, closed=True):
    core_network_id: NotRequired[
        "capo_networkmanager.types.core_network_id.CoreNetworkId"
    ]
    """<p>The ID of the core network associated with the prefix list.</p>"""
    prefix_list_arn: NotRequired[
        "capo_networkmanager.types.prefix_list_arn.PrefixListArn"
    ]
    """<p>The ARN of the prefix list that was associated with the core network.</p>"""
    prefix_list_alias: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The alias of the prefix list association, if provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCoreNetworkPrefixListAssociationResponse) -> dict:
    out: dict = {}
    if "core_network_id" in value:
        out["CoreNetworkId"] = value["core_network_id"]
    if "prefix_list_arn" in value:
        out["PrefixListArn"] = value["prefix_list_arn"]
    if "prefix_list_alias" in value:
        out["PrefixListAlias"] = value["prefix_list_alias"]
    return out


def deserialize_json(data: dict) -> CreateCoreNetworkPrefixListAssociationResponse:
    out: CreateCoreNetworkPrefixListAssociationResponse = {}  # type: ignore[typeddict-item]
    if "CoreNetworkId" in data:
        out["core_network_id"] = data["CoreNetworkId"]
    if "PrefixListArn" in data:
        out["prefix_list_arn"] = data["PrefixListArn"]
    if "PrefixListAlias" in data:
        out["prefix_list_alias"] = data["PrefixListAlias"]
    return out
