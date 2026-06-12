"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetPropertyPathSegment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.name


class AssetPropertyPathSegment(TypedDict):
    id: NotRequired["aws_sdk_iotsitewise.types.id.ID"]
    """<p>The ID of the path segment.</p>"""
    name: NotRequired["aws_sdk_iotsitewise.types.name.Name"]
    """<p>The name of the path segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetPropertyPathSegment) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AssetPropertyPathSegment:
    out: AssetPropertyPathSegment = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    return out
