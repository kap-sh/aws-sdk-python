"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#Resource``."""

from typing_extensions import NotRequired, TypedDict


class Resource(TypedDict, closed=True):
    id: NotRequired["str"]
    """<p>The <code>scanName</code> of the scan that was run on the resource.</p>"""
    sub_resource_id: NotRequired["str"]
    """<p>The identifier for a section of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "sub_resource_id" in value:
        out["subResourceId"] = value["sub_resource_id"]
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "subResourceId" in data:
        out["sub_resource_id"] = data["subResourceId"]
    return out
