"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeTagsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.tag_list


class DescribeTagsResult(TypedDict):
    tag_list: NotRequired["aws_sdk_workspaces.types.tag_list.TagList"]
    """<p>The tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTagsResult) -> dict:
    out: dict = {}
    if "tag_list" in value:
        import aws_sdk_workspaces.types.tag_list

        out["TagList"] = aws_sdk_workspaces.types.tag_list.serialize_aws_json_1_1(
            value["tag_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTagsResult:
    out: DescribeTagsResult = {}  # type: ignore[typeddict-item]
    if "TagList" in data:
        import aws_sdk_workspaces.types.tag_list

        out["tag_list"] = aws_sdk_workspaces.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    return out
