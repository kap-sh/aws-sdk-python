"""Generated from Smithy shape ``com.amazonaws.memorydb#TagResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.tag_list


class TagResourceResponse(TypedDict, closed=True):
    tag_list: NotRequired["aws_sdk_memorydb.types.tag_list.TagList"]
    """<p>A list of tags as key-value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceResponse) -> dict:
    out: dict = {}
    if "tag_list" in value:
        import aws_sdk_memorydb.types.tag_list

        out["TagList"] = aws_sdk_memorydb.types.tag_list.serialize_aws_json_1_1(
            value["tag_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceResponse:
    out: TagResourceResponse = {}  # type: ignore[typeddict-item]
    if "TagList" in data:
        import aws_sdk_memorydb.types.tag_list

        out["tag_list"] = aws_sdk_memorydb.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    return out
