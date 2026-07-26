"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListTagsOfResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.next_token_string
    import capo_dynamodb.types.tag_list


class ListTagsOfResourceOutput(TypedDict, closed=True):
    tags: NotRequired["capo_dynamodb.types.tag_list.TagList"]
    """<p>The tags currently associated with the Amazon DynamoDB resource.</p>"""
    next_token: NotRequired["capo_dynamodb.types.next_token_string.NextTokenString"]
    """<p>If this value is returned, there are additional results to be displayed. To retrieve them, call ListTagsOfResource again, with NextToken set to this value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsOfResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_dynamodb.types.tag_list

        out["Tags"] = capo_dynamodb.types.tag_list.serialize_aws_json_1_0(value["tags"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsOfResourceOutput:
    out: ListTagsOfResourceOutput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_dynamodb.types.tag_list

        out["tags"] = capo_dynamodb.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
