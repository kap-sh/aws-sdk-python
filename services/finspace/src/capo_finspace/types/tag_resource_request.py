"""Generated from Smithy shape ``com.amazonaws.finspace#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_finspace.errors import DeserializationError

if TYPE_CHECKING:
    import capo_finspace.types.fin_space_taggable_arn
    import capo_finspace.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_finspace.types.fin_space_taggable_arn.FinSpaceTaggableArn"
    """<p>The Amazon Resource Name (ARN) for the resource.</p>"""
    tags: "capo_finspace.types.tag_map.TagMap"
    """<p>One or more tags to be assigned to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_finspace.types.tag_map

    out["tags"] = capo_finspace.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_finspace.types.tag_map

        out["tags"] = capo_finspace.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
