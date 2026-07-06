"""Generated from Smithy shape ``com.amazonaws.sfn#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sfn.types.tag_list


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_sfn.types.tag_list.TagList"]
    """<p>An array of tags associated with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_sfn.types.tag_list

        out["tags"] = aws_sdk_sfn.types.tag_list.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_sfn.types.tag_list

        out["tags"] = aws_sdk_sfn.types.tag_list.deserialize_aws_json_1_0(data["tags"])
    return out
