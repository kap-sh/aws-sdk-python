"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_timestream_write.types.tag_list.TagList"]
    """<p> The tags currently associated with the Timestream resource. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_timestream_write.types.tag_list

        out["Tags"] = aws_sdk_timestream_write.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_timestream_write.types.tag_list

        out["tags"] = aws_sdk_timestream_write.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
