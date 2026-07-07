"""Generated from Smithy shape ``com.amazonaws.cloud9#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloud9.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_cloud9.types.tag_list.TagList"]
    """<p>The list of tags associated with the Cloud9 development environment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_cloud9.types.tag_list

        out["Tags"] = aws_sdk_cloud9.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_cloud9.types.tag_list

        out["tags"] = aws_sdk_cloud9.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
