"""Generated from Smithy shape ``com.amazonaws.omics#CreateWorkflowResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.tag_map
    import aws_sdk_omics.types.workflow_arn
    import aws_sdk_omics.types.workflow_id
    import aws_sdk_omics.types.workflow_status
    import aws_sdk_omics.types.workflow_uuid


class CreateWorkflowResponse(TypedDict):
    arn: NotRequired["aws_sdk_omics.types.workflow_arn.WorkflowArn"]
    """<p>The workflow's ARN.</p>"""
    id: NotRequired["aws_sdk_omics.types.workflow_id.WorkflowId"]
    """<p>The workflow's ID.</p>"""
    status: NotRequired["aws_sdk_omics.types.workflow_status.WorkflowStatus"]
    """<p>The workflow's status.</p>"""
    tags: NotRequired["aws_sdk_omics.types.tag_map.TagMap"]
    """<p>The workflow's tags.</p>"""
    uuid: NotRequired["aws_sdk_omics.types.workflow_uuid.WorkflowUuid"]
    """<p>The universally unique identifier (UUID) value for this workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkflowResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "status" in value:
        out["status"] = value["status"]
    if "tags" in value:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.serialize_json(value["tags"])
    if "uuid" in value:
        out["uuid"] = value["uuid"]
    return out


def deserialize_json(data: dict) -> CreateWorkflowResponse:
    out: CreateWorkflowResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    if "status" in data:
        out["status"] = data["status"]
    if "tags" in data:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.deserialize_json(data["tags"])
    if "uuid" in data:
        out["uuid"] = data["uuid"]
    return out
