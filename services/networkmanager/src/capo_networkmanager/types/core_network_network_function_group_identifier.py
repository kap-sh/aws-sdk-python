"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkNetworkFunctionGroupIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.external_region_code


class CoreNetworkNetworkFunctionGroupIdentifier(TypedDict, closed=True):
    core_network_id: NotRequired[
        "capo_networkmanager.types.core_network_id.CoreNetworkId"
    ]
    """<p>The ID of the core network.</p>"""
    network_function_group_name: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The network function group name.</p>"""
    edge_location: NotRequired[
        "capo_networkmanager.types.external_region_code.ExternalRegionCode"
    ]
    """<p>The location for the core network edge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkNetworkFunctionGroupIdentifier) -> dict:
    out: dict = {}
    if "core_network_id" in value:
        out["CoreNetworkId"] = value["core_network_id"]
    if "network_function_group_name" in value:
        out["NetworkFunctionGroupName"] = value["network_function_group_name"]
    if "edge_location" in value:
        out["EdgeLocation"] = value["edge_location"]
    return out


def deserialize_json(data: dict) -> CoreNetworkNetworkFunctionGroupIdentifier:
    out: CoreNetworkNetworkFunctionGroupIdentifier = {}  # type: ignore[typeddict-item]
    if "CoreNetworkId" in data:
        out["core_network_id"] = data["CoreNetworkId"]
    if "NetworkFunctionGroupName" in data:
        out["network_function_group_name"] = data["NetworkFunctionGroupName"]
    if "EdgeLocation" in data:
        out["edge_location"] = data["EdgeLocation"]
    return out
