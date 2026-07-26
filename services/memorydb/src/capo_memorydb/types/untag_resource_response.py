"""Generated from Smithy shape ``com.amazonaws.memorydb#UntagResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.tag_list


class UntagResourceResponse(TypedDict, closed=True):
    tag_list: NotRequired["capo_memorydb.types.tag_list.TagList"]
    """<p>The list of tags removed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceResponse) -> dict:
    out: dict = {}
    if "tag_list" in value:
        import capo_memorydb.types.tag_list

        out["TagList"] = capo_memorydb.types.tag_list.serialize_aws_json_1_1(
            value["tag_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceResponse:
    out: UntagResourceResponse = {}  # type: ignore[typeddict-item]
    if "TagList" in data:
        import capo_memorydb.types.tag_list

        out["tag_list"] = capo_memorydb.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    return out
