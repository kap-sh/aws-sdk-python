"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkNetworkFunctionGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.external_region_code_list
    import capo_networkmanager.types.service_insertion_segments


class CoreNetworkNetworkFunctionGroup(TypedDict, closed=True):
    name: NotRequired["capo_networkmanager.types.constrained_string.ConstrainedString"]
    """<p>The name of the network function group.</p>"""
    edge_locations: NotRequired[
        "capo_networkmanager.types.external_region_code_list.ExternalRegionCodeList"
    ]
    """<p>The core network edge locations.</p>"""
    segments: NotRequired[
        "capo_networkmanager.types.service_insertion_segments.ServiceInsertionSegments"
    ]
    """<p>The segments associated with the network function group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkNetworkFunctionGroup) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "edge_locations" in value:
        import capo_networkmanager.types.external_region_code_list

        out["EdgeLocations"] = (
            capo_networkmanager.types.external_region_code_list.serialize_json(
                value["edge_locations"]
            )
        )
    if "segments" in value:
        import capo_networkmanager.types.service_insertion_segments

        out["Segments"] = (
            capo_networkmanager.types.service_insertion_segments.serialize_json(
                value["segments"]
            )
        )
    return out


def deserialize_json(data: dict) -> CoreNetworkNetworkFunctionGroup:
    out: CoreNetworkNetworkFunctionGroup = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "EdgeLocations" in data:
        import capo_networkmanager.types.external_region_code_list

        out["edge_locations"] = (
            capo_networkmanager.types.external_region_code_list.deserialize_json(
                data["EdgeLocations"]
            )
        )
    if "Segments" in data:
        import capo_networkmanager.types.service_insertion_segments

        out["segments"] = (
            capo_networkmanager.types.service_insertion_segments.deserialize_json(
                data["Segments"]
            )
        )
    return out
