"""Generated from Smithy shape ``com.amazonaws.omics#BatchListItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.batch_id
    import aws_sdk_omics.types.batch_name
    import aws_sdk_omics.types.batch_status
    import aws_sdk_omics.types.batch_timestamp
    import aws_sdk_omics.types.workflow_id


class BatchListItem(TypedDict):
    id: NotRequired["aws_sdk_omics.types.batch_id.BatchId"]
    """<p>The batch identifier.</p>"""
    name: NotRequired["aws_sdk_omics.types.batch_name.BatchName"]
    """<p>The batch name.</p>"""
    status: NotRequired["aws_sdk_omics.types.batch_status.BatchStatus"]
    """<p>The current batch status.</p>"""
    created_at: NotRequired["aws_sdk_omics.types.batch_timestamp.BatchTimestamp"]
    """<p>The timestamp when the batch was created.</p>"""
    total_runs: NotRequired["int"]
    """<p>The total number of runs in the batch.</p>"""
    workflow_id: NotRequired["aws_sdk_omics.types.workflow_id.WorkflowId"]
    """<p>The identifier of the workflow used for the batch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchListItem) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    if "created_at" in value:
        import aws_sdk_omics.types.batch_timestamp

        out["createdAt"] = aws_sdk_omics.types.batch_timestamp.serialize_json(
            value["created_at"]
        )
    if "total_runs" in value:
        out["totalRuns"] = value["total_runs"]
    if "workflow_id" in value:
        out["workflowId"] = value["workflow_id"]
    return out


def deserialize_json(data: dict) -> BatchListItem:
    out: BatchListItem = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        out["status"] = data["status"]
    if "createdAt" in data:
        import aws_sdk_omics.types.batch_timestamp

        out["created_at"] = aws_sdk_omics.types.batch_timestamp.deserialize_json(
            data["createdAt"]
        )
    if "totalRuns" in data:
        out["total_runs"] = data["totalRuns"]
    if "workflowId" in data:
        out["workflow_id"] = data["workflowId"]
    return out
