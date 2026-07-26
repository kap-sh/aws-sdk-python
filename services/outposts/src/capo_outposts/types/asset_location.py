"""Generated from Smithy shape ``com.amazonaws.outposts#AssetLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.rack_elevation


class AssetLocation(TypedDict, closed=True):
    rack_elevation: NotRequired["capo_outposts.types.rack_elevation.RackElevation"]
    """<p> The position of an asset in a rack measured in rack units. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetLocation) -> dict:
    out: dict = {}
    if "rack_elevation" in value:
        out["RackElevation"] = value["rack_elevation"]
    return out


def deserialize_json(data: dict) -> AssetLocation:
    out: AssetLocation = {}  # type: ignore[typeddict-item]
    if "RackElevation" in data:
        out["rack_elevation"] = data["RackElevation"]
    return out
