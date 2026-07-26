"""Generated from Smithy shape ``com.amazonaws.codeconnections#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.tag_list


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: NotRequired["capo_codeconnections.types.tag_list.TagList"]
    """<p>A list of tag key and value pairs associated with the specified resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_codeconnections.types.tag_list

        out["Tags"] = capo_codeconnections.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_codeconnections.types.tag_list

        out["tags"] = capo_codeconnections.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
