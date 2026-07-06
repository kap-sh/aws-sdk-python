"""Generated from Smithy shape ``com.amazonaws.dax#TagResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dax.types.tag_list


class TagResourceResponse(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_dax.types.tag_list.TagList"]
    """<p>The list of tags that are associated with the DAX resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_dax.types.tag_list

        out["Tags"] = aws_sdk_dax.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceResponse:
    out: TagResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_dax.types.tag_list

        out["tags"] = aws_sdk_dax.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
