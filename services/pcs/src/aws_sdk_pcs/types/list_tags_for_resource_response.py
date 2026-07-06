"""Generated from Smithy shape ``com.amazonaws.pcs#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pcs.types.response_tag_map


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_pcs.types.response_tag_map.ResponseTagMap"]
    """<p>1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_pcs.types.response_tag_map

        out["tags"] = aws_sdk_pcs.types.response_tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_pcs.types.response_tag_map

        out["tags"] = aws_sdk_pcs.types.response_tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
