"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListTagsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.tag_list


class ListTagsOutput(TypedDict, closed=True):
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>An array of <code>Tag</code> objects, each with a tag key and a value.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p> If response is truncated, SageMaker includes a token in the response. You can use this token in your subsequent request to fetch next set of tokens. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsOutput:
    out: ListTagsOutput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
