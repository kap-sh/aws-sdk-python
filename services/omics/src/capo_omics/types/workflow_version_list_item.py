"""Generated from Smithy shape ``com.amazonaws.omics#WorkflowVersionListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.workflow_digest
    import capo_omics.types.workflow_id
    import capo_omics.types.workflow_metadata
    import capo_omics.types.workflow_status
    import capo_omics.types.workflow_timestamp
    import capo_omics.types.workflow_type
    import capo_omics.types.workflow_version_arn
    import capo_omics.types.workflow_version_description
    import capo_omics.types.workflow_version_name


class WorkflowVersionListItem(TypedDict, closed=True):
    arn: NotRequired["capo_omics.types.workflow_version_arn.WorkflowVersionArn"]
    """<p>ARN of the workflow version.</p>"""
    workflow_id: NotRequired["capo_omics.types.workflow_id.WorkflowId"]
    """<p>The workflow's ID.</p>"""
    version_name: NotRequired[
        "capo_omics.types.workflow_version_name.WorkflowVersionName"
    ]
    """<p>The name of the workflow version.</p>"""
    description: NotRequired[
        "capo_omics.types.workflow_version_description.WorkflowVersionDescription"
    ]
    """<p>The description of the workflow version.</p>"""
    status: NotRequired["capo_omics.types.workflow_status.WorkflowStatus"]
    """<p>The status of the workflow version.</p>"""
    type: NotRequired["capo_omics.types.workflow_type.WorkflowType"]
    """<p>The type of the workflow version.</p>"""
    digest: NotRequired["capo_omics.types.workflow_digest.WorkflowDigest"]
    """<p>The digist of the workflow version.</p>"""
    creation_time: NotRequired["capo_omics.types.workflow_timestamp.WorkflowTimestamp"]
    """<p>The creation time of the workflow version.</p>"""
    metadata: NotRequired["capo_omics.types.workflow_metadata.WorkflowMetadata"]
    """<p>Metadata for the workflow version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowVersionListItem) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "workflow_id" in value:
        out["workflowId"] = value["workflow_id"]
    if "version_name" in value:
        out["versionName"] = value["version_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        out["status"] = value["status"]
    if "type" in value:
        out["type"] = value["type"]
    if "digest" in value:
        out["digest"] = value["digest"]
    if "creation_time" in value:
        import capo_omics.types.workflow_timestamp

        out["creationTime"] = capo_omics.types.workflow_timestamp.serialize_json(
            value["creation_time"]
        )
    if "metadata" in value:
        import capo_omics.types.workflow_metadata

        out["metadata"] = capo_omics.types.workflow_metadata.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> WorkflowVersionListItem:
    out: WorkflowVersionListItem = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "workflowId" in data:
        out["workflow_id"] = data["workflowId"]
    if "versionName" in data:
        out["version_name"] = data["versionName"]
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        out["status"] = data["status"]
    if "type" in data:
        out["type"] = data["type"]
    if "digest" in data:
        out["digest"] = data["digest"]
    if "creationTime" in data:
        import capo_omics.types.workflow_timestamp

        out["creation_time"] = capo_omics.types.workflow_timestamp.deserialize_json(
            data["creationTime"]
        )
    if "metadata" in data:
        import capo_omics.types.workflow_metadata

        out["metadata"] = capo_omics.types.workflow_metadata.deserialize_json(
            data["metadata"]
        )
    return out
