"""Generated from Smithy shape ``com.amazonaws.pinpoint#TagsModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.map_of__string


class TagsModel(TypedDict, closed=True):
    tags: NotRequired["capo_pinpoint.types.map_of__string.MapOf__string"]
    """<p>A string-to-string map of key-value pairs that defines the tags for an application, campaign, message template, or segment. Each of these resources can have a maximum of 50 tags.</p> <p>Each tag consists of a required tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagsModel) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_pinpoint.types.map_of__string

        out["tags"] = capo_pinpoint.types.map_of__string.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagsModel:
    out: TagsModel = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_pinpoint.types.map_of__string

        out["tags"] = capo_pinpoint.types.map_of__string.deserialize_json(data["tags"])
    return out
