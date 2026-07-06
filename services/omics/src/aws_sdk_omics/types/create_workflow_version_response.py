"""Generated from Smithy shape ``com.amazonaws.omics#CreateWorkflowVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.tag_map
    import aws_sdk_omics.types.workflow_id
    import aws_sdk_omics.types.workflow_status
    import aws_sdk_omics.types.workflow_uuid
    import aws_sdk_omics.types.workflow_version_arn
    import aws_sdk_omics.types.workflow_version_name


class CreateWorkflowVersionResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_omics.types.workflow_version_arn.WorkflowVersionArn"]
    """<p>ARN of the workflow version.</p>"""
    workflow_id: NotRequired["aws_sdk_omics.types.workflow_id.WorkflowId"]
    """<p>The workflow's ID.</p>"""
    version_name: NotRequired[
        "aws_sdk_omics.types.workflow_version_name.WorkflowVersionName"
    ]
    """<p>The workflow version name.</p>"""
    status: NotRequired["aws_sdk_omics.types.workflow_status.WorkflowStatus"]
    """<p>The workflow version status.</p>"""
    tags: NotRequired["aws_sdk_omics.types.tag_map.TagMap"]
    """<p>The workflow version's tags.</p>"""
    uuid: NotRequired["aws_sdk_omics.types.workflow_uuid.WorkflowUuid"]
    """<p>The universally unique identifier (UUID) value for this workflow version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkflowVersionResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "workflow_id" in value:
        out["workflowId"] = value["workflow_id"]
    if "version_name" in value:
        out["versionName"] = value["version_name"]
    if "status" in value:
        out["status"] = value["status"]
    if "tags" in value:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.serialize_json(value["tags"])
    if "uuid" in value:
        out["uuid"] = value["uuid"]
    return out


def deserialize_json(data: dict) -> CreateWorkflowVersionResponse:
    out: CreateWorkflowVersionResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "workflowId" in data:
        out["workflow_id"] = data["workflowId"]
    if "versionName" in data:
        out["version_name"] = data["versionName"]
    if "status" in data:
        out["status"] = data["status"]
    if "tags" in data:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.deserialize_json(data["tags"])
    if "uuid" in data:
        out["uuid"] = data["uuid"]
    return out
