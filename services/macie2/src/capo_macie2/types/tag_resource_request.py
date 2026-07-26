"""Generated from Smithy shape ``com.amazonaws.macie2#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string
    import capo_macie2.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_macie2.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: NotRequired["capo_macie2.types.tag_map.TagMap"]
    """<p>A map of key-value pairs that specifies the tags to associate with the resource.</p> <p>A resource can have a maximum of 50 tags. Each tag consists of a tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_macie2.types.tag_map

        out["tags"] = capo_macie2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_macie2.types.tag_map

        out["tags"] = capo_macie2.types.tag_map.deserialize_json(data["tags"])
    return out
