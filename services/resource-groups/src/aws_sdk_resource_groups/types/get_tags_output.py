"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GetTagsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.group_arn_v2
    import aws_sdk_resource_groups.types.tags


class GetTagsOutput(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_resource_groups.types.group_arn_v2.GroupArnV2"]
    """<p>TheAmazon resource name (ARN) of the tagged resource group.</p>"""
    tags: NotRequired["aws_sdk_resource_groups.types.tags.Tags"]
    """<p>The tags associated with the specified resource group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTagsOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "tags" in value:
        import aws_sdk_resource_groups.types.tags

        out["Tags"] = aws_sdk_resource_groups.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetTagsOutput:
    out: GetTagsOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Tags" in data:
        import aws_sdk_resource_groups.types.tags

        out["tags"] = aws_sdk_resource_groups.types.tags.deserialize_json(data["Tags"])
    return out
