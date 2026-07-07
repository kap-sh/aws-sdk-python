"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelPropertyPathSegment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.name


class AssetModelPropertyPathSegment(TypedDict, closed=True):
    id: NotRequired["aws_sdk_iotsitewise.types.id.ID"]
    """<p>The ID of the path segment.</p>"""
    name: NotRequired["aws_sdk_iotsitewise.types.name.Name"]
    """<p>The name of the path segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelPropertyPathSegment) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AssetModelPropertyPathSegment:
    out: AssetModelPropertyPathSegment = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    return out
