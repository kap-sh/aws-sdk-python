"""Generated from Smithy shape ``com.amazonaws.dax#UntagResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dax.types.tag_list


class UntagResourceResponse(TypedDict):
    tags: NotRequired["aws_sdk_dax.types.tag_list.TagList"]
    """<p>The tag keys that have been removed from the cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_dax.types.tag_list

        out["Tags"] = aws_sdk_dax.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceResponse:
    out: UntagResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_dax.types.tag_list

        out["tags"] = aws_sdk_dax.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
