"""Generated from Smithy shape ``com.amazonaws.fsx#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.resource_arn
    import capo_fsx.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: NotRequired["capo_fsx.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the Amazon FSx resource that you want to tag.</p>"""
    tags: NotRequired["capo_fsx.types.tags.Tags"]
    """<p>A list of tags for the resource. If a tag with a given key already exists, the value is replaced by the one specified in this parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "tags" in value:
        import capo_fsx.types.tags

        out["Tags"] = capo_fsx.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    if "Tags" in data:
        import capo_fsx.types.tags

        out["tags"] = capo_fsx.types.tags.deserialize_aws_json_1_1(data["Tags"])
    return out
