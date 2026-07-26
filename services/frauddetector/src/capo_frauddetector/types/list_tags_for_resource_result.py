"""Generated from Smithy shape ``com.amazonaws.frauddetector#ListTagsForResourceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.string
    import capo_frauddetector.types.tag_list


class ListTagsForResourceResult(TypedDict, closed=True):
    tags: NotRequired["capo_frauddetector.types.tag_list.tagList"]
    """<p>A collection of key and value pairs.</p>"""
    next_token: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The next token for subsequent requests. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResult) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResult:
    out: ListTagsForResourceResult = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
