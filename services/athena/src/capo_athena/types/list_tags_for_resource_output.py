"""Generated from Smithy shape ``com.amazonaws.athena#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.tag_list
    import capo_athena.types.token


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: NotRequired["capo_athena.types.tag_list.TagList"]
    """<p>The list of tags associated with the specified resource.</p>"""
    next_token: NotRequired["capo_athena.types.token.Token"]
    """<p>A token to be used by the next request if this request is truncated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_athena.types.tag_list

        out["Tags"] = capo_athena.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_athena.types.tag_list

        out["tags"] = capo_athena.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
