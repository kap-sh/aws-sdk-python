"""Generated from Smithy shape ``com.amazonaws.ssm#ListTagsForResourceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.tag_list


class ListTagsForResourceResult(TypedDict, closed=True):
    tag_list: NotRequired["capo_ssm.types.tag_list.TagList"]
    """<p>A list of tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResult) -> dict:
    out: dict = {}
    if "tag_list" in value:
        import capo_ssm.types.tag_list

        out["TagList"] = capo_ssm.types.tag_list.serialize_aws_json_1_1(
            value["tag_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResult:
    out: ListTagsForResourceResult = {}  # type: ignore[typeddict-item]
    if "TagList" in data:
        import capo_ssm.types.tag_list

        out["tag_list"] = capo_ssm.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    return out
