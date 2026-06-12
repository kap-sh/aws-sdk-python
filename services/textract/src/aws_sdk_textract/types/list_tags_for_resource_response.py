"""Generated from Smithy shape ``com.amazonaws.textract#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.tag_map


class ListTagsForResourceResponse(TypedDict):
    tags: NotRequired["aws_sdk_textract.types.tag_map.TagMap"]
    """<p>A set of tags (key-value pairs) that are part of the requested resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_textract.types.tag_map

        out["Tags"] = aws_sdk_textract.types.tag_map.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_textract.types.tag_map

        out["tags"] = aws_sdk_textract.types.tag_map.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
