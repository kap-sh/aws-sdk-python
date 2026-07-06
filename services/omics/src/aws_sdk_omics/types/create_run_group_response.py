"""Generated from Smithy shape ``com.amazonaws.omics#CreateRunGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.run_group_arn
    import aws_sdk_omics.types.run_group_id
    import aws_sdk_omics.types.tag_map


class CreateRunGroupResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_omics.types.run_group_arn.RunGroupArn"]
    """<p>The group's ARN.</p>"""
    id: NotRequired["aws_sdk_omics.types.run_group_id.RunGroupId"]
    """<p>The group's ID.</p>"""
    tags: NotRequired["aws_sdk_omics.types.tag_map.TagMap"]
    """<p>Tags for the run group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRunGroupResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "tags" in value:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRunGroupResponse:
    out: CreateRunGroupResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    if "tags" in data:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.deserialize_json(data["tags"])
    return out
