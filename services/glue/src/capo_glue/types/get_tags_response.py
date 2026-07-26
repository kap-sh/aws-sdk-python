"""Generated from Smithy shape ``com.amazonaws.glue#GetTagsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.tags_map


class GetTagsResponse(TypedDict, closed=True):
    tags: NotRequired["capo_glue.types.tags_map.TagsMap"]
    """<p>The requested tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTagsResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_glue.types.tags_map

        out["Tags"] = capo_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTagsResponse:
    out: GetTagsResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_glue.types.tags_map

        out["tags"] = capo_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    return out
