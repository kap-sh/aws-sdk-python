"""Generated from Smithy shape ``com.amazonaws.odb#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.response_tag_map


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_odb.types.response_tag_map.ResponseTagMap"]
    """<p>The list of tags applied to the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_odb.types.response_tag_map

        out["tags"] = aws_sdk_odb.types.response_tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_odb.types.response_tag_map

        out["tags"] = aws_sdk_odb.types.response_tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
