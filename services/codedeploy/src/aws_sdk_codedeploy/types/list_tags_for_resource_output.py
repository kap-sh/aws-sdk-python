"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.next_token
    import aws_sdk_codedeploy.types.tag_list


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_codedeploy.types.tag_list.TagList"]
    """<p> A list of tags returned by <code>ListTagsForResource</code>. The tags are associated with the resource identified by the input <code>ResourceArn</code> parameter. </p>"""
    next_token: NotRequired["aws_sdk_codedeploy.types.next_token.NextToken"]
    """<p>If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list application revisions call to return the next set of application revisions in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_codedeploy.types.tag_list

        out["Tags"] = aws_sdk_codedeploy.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_codedeploy.types.tag_list

        out["tags"] = aws_sdk_codedeploy.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
