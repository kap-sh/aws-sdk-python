"""Generated from Smithy shape ``com.amazonaws.interconnect#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_interconnect.types.tag_map


class ListTagsForResourceResponse(TypedDict):
    tags: NotRequired["aws_sdk_interconnect.types.tag_map.TagMap"]
    """<p>The tags on the specified ARN.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_interconnect.types.tag_map

        out["tags"] = aws_sdk_interconnect.types.tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_interconnect.types.tag_map

        out["tags"] = aws_sdk_interconnect.types.tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
