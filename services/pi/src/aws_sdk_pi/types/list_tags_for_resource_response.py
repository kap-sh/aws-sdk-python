"""Generated from Smithy shape ``com.amazonaws.pi#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pi.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_pi.types.tag_list.TagList"]
    """<p>The metadata assigned to an Amazon RDS resource consisting of a key-value pair.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_pi.types.tag_list

        out["Tags"] = aws_sdk_pi.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_pi.types.tag_list

        out["tags"] = aws_sdk_pi.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
