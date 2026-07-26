"""Generated from Smithy shape ``com.amazonaws.swf#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.resource_tag_list


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: NotRequired["capo_swf.types.resource_tag_list.ResourceTagList"]
    """<p>An array of tags associated with the domain.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_swf.types.resource_tag_list

        out["tags"] = capo_swf.types.resource_tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_swf.types.resource_tag_list

        out["tags"] = capo_swf.types.resource_tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
