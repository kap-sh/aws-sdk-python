"""Generated from Smithy shape ``com.amazonaws.fms#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fms.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tag_list: NotRequired["aws_sdk_fms.types.tag_list.TagList"]
    """<p>The tags associated with the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tag_list" in value:
        import aws_sdk_fms.types.tag_list

        out["TagList"] = aws_sdk_fms.types.tag_list.serialize_aws_json_1_1(
            value["tag_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "TagList" in data:
        import aws_sdk_fms.types.tag_list

        out["tag_list"] = aws_sdk_fms.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    return out
