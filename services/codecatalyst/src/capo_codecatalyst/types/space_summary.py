"""Generated from Smithy shape ``com.amazonaws.codecatalyst#SpaceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecatalyst.types.name_string
    import capo_codecatalyst.types.region_string


class SpaceSummary(TypedDict, closed=True):
    name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    region_name: "capo_codecatalyst.types.region_string.RegionString"
    """<p>The Amazon Web Services Region where the space exists.</p>"""
    display_name: NotRequired["str"]
    """<p>The friendly name of the space displayed to users.</p>"""
    description: NotRequired["str"]
    """<p>The description of the space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpaceSummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["regionName"] = value["region_name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> SpaceSummary:
    out: SpaceSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SpaceSummary.name required")
    if "regionName" in data:
        out["region_name"] = data["regionName"]
    else:
        raise DeserializationError("SpaceSummary.region_name required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "description" in data:
        out["description"] = data["description"]
    return out
