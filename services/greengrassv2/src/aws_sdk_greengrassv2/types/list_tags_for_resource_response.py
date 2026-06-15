"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.tag_map


class ListTagsForResourceResponse(TypedDict):
    tags: NotRequired["aws_sdk_greengrassv2.types.tag_map.TagMap"]
    r"""<p>A list of key-value pairs that contain metadata for the resource. For more information, see <a href=\"https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html\">Tag your resources</a> in the <i>IoT Greengrass V2 Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_greengrassv2.types.tag_map

        out["tags"] = aws_sdk_greengrassv2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_greengrassv2.types.tag_map

        out["tags"] = aws_sdk_greengrassv2.types.tag_map.deserialize_json(data["tags"])
    return out
