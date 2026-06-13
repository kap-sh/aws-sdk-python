"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.tag_map


class ListTagsForResourceResponse(TypedDict):
    tags: "aws_sdk_cleanroomsml.types.tag_map.TagMap"
    """<p>The tags that are associated with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types.tag_map

    out["tags"] = aws_sdk_cleanroomsml.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_cleanroomsml.types.tag_map

        out["tags"] = aws_sdk_cleanroomsml.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("ListTagsForResourceResponse.tags required")
    return out
