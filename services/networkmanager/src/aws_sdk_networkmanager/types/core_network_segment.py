"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkSegment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.constrained_string_list
    import aws_sdk_networkmanager.types.external_region_code_list


class CoreNetworkSegment(TypedDict):
    name: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The name of a core network segment.</p>"""
    edge_locations: NotRequired[
        "aws_sdk_networkmanager.types.external_region_code_list.ExternalRegionCodeList"
    ]
    """<p>The Regions where the edges are located.</p>"""
    shared_segments: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>The shared segments of a core network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkSegment) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "edge_locations" in value:
        import aws_sdk_networkmanager.types.external_region_code_list

        out["EdgeLocations"] = (
            aws_sdk_networkmanager.types.external_region_code_list.serialize_json(
                value["edge_locations"]
            )
        )
    if "shared_segments" in value:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["SharedSegments"] = (
            aws_sdk_networkmanager.types.constrained_string_list.serialize_json(
                value["shared_segments"]
            )
        )
    return out


def deserialize_json(data: dict) -> CoreNetworkSegment:
    out: CoreNetworkSegment = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "EdgeLocations" in data:
        import aws_sdk_networkmanager.types.external_region_code_list

        out["edge_locations"] = (
            aws_sdk_networkmanager.types.external_region_code_list.deserialize_json(
                data["EdgeLocations"]
            )
        )
    if "SharedSegments" in data:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["shared_segments"] = (
            aws_sdk_networkmanager.types.constrained_string_list.deserialize_json(
                data["SharedSegments"]
            )
        )
    return out
