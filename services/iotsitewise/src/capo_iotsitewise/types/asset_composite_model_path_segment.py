"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetCompositeModelPathSegment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name


class AssetCompositeModelPathSegment(TypedDict, closed=True):
    id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the path segment.</p>"""
    name: NotRequired["capo_iotsitewise.types.name.Name"]
    """<p>The name of the path segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetCompositeModelPathSegment) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AssetCompositeModelPathSegment:
    out: AssetCompositeModelPathSegment = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    return out
