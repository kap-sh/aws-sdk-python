"""Generated from Smithy shape ``com.amazonaws.drs#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_drs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_drs.types.arn
    import capo_drs.types.tags_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_drs.types.arn.ARN"
    """<p>ARN of the resource for which tags are to be added or updated.</p>"""
    tags: "capo_drs.types.tags_map.TagsMap"
    """<p>Array of tags to be added or updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_drs.types.tags_map

    out["tags"] = capo_drs.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
