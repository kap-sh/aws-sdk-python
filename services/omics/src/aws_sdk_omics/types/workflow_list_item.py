"""Generated from Smithy shape ``com.amazonaws.omics#WorkflowListItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.workflow_arn
    import aws_sdk_omics.types.workflow_digest
    import aws_sdk_omics.types.workflow_id
    import aws_sdk_omics.types.workflow_metadata
    import aws_sdk_omics.types.workflow_name
    import aws_sdk_omics.types.workflow_status
    import aws_sdk_omics.types.workflow_timestamp
    import aws_sdk_omics.types.workflow_type


class WorkflowListItem(TypedDict):
    arn: NotRequired["aws_sdk_omics.types.workflow_arn.WorkflowArn"]
    """<p>The workflow's ARN.</p>"""
    id: NotRequired["aws_sdk_omics.types.workflow_id.WorkflowId"]
    """<p>The workflow's ID.</p>"""
    name: NotRequired["aws_sdk_omics.types.workflow_name.WorkflowName"]
    """<p>The workflow's name.</p>"""
    status: NotRequired["aws_sdk_omics.types.workflow_status.WorkflowStatus"]
    """<p>The workflow's status.</p>"""
    type: NotRequired["aws_sdk_omics.types.workflow_type.WorkflowType"]
    """<p>The workflow's type.</p>"""
    digest: NotRequired["aws_sdk_omics.types.workflow_digest.WorkflowDigest"]
    """<p>The workflow's digest.</p>"""
    creation_time: NotRequired[
        "aws_sdk_omics.types.workflow_timestamp.WorkflowTimestamp"
    ]
    """<p>When the workflow was created.</p>"""
    metadata: NotRequired["aws_sdk_omics.types.workflow_metadata.WorkflowMetadata"]
    """<p> Any metadata available for workflow. The information listed may vary depending on the workflow, and there may also be no metadata to return. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowListItem) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    if "type" in value:
        out["type"] = value["type"]
    if "digest" in value:
        out["digest"] = value["digest"]
    if "creation_time" in value:
        import aws_sdk_omics.types.workflow_timestamp

        out["creationTime"] = aws_sdk_omics.types.workflow_timestamp.serialize_json(
            value["creation_time"]
        )
    if "metadata" in value:
        import aws_sdk_omics.types.workflow_metadata

        out["metadata"] = aws_sdk_omics.types.workflow_metadata.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> WorkflowListItem:
    out: WorkflowListItem = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        out["status"] = data["status"]
    if "type" in data:
        out["type"] = data["type"]
    if "digest" in data:
        out["digest"] = data["digest"]
    if "creationTime" in data:
        import aws_sdk_omics.types.workflow_timestamp

        out["creation_time"] = aws_sdk_omics.types.workflow_timestamp.deserialize_json(
            data["creationTime"]
        )
    if "metadata" in data:
        import aws_sdk_omics.types.workflow_metadata

        out["metadata"] = aws_sdk_omics.types.workflow_metadata.deserialize_json(
            data["metadata"]
        )
    return out
