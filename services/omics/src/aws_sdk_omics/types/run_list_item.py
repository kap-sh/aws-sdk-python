"""Generated from Smithy shape ``com.amazonaws.omics#RunListItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.batch_id
    import aws_sdk_omics.types.run_arn
    import aws_sdk_omics.types.run_id
    import aws_sdk_omics.types.run_name
    import aws_sdk_omics.types.run_status
    import aws_sdk_omics.types.run_timestamp
    import aws_sdk_omics.types.storage_type
    import aws_sdk_omics.types.workflow_id
    import aws_sdk_omics.types.workflow_name
    import aws_sdk_omics.types.workflow_version_name


class RunListItem(TypedDict):
    arn: NotRequired["aws_sdk_omics.types.run_arn.RunArn"]
    """<p>The run's ARN.</p>"""
    id: NotRequired["aws_sdk_omics.types.run_id.RunId"]
    """<p>The run's ID.</p>"""
    status: NotRequired["aws_sdk_omics.types.run_status.RunStatus"]
    """<p>The run's status.</p>"""
    workflow_id: NotRequired["aws_sdk_omics.types.workflow_id.WorkflowId"]
    """<p>The run's workflow ID.</p>"""
    batch_id: NotRequired["aws_sdk_omics.types.batch_id.BatchId"]
    """<p>The run's batch ID.</p>"""
    name: NotRequired["aws_sdk_omics.types.run_name.RunName"]
    """<p>The run's name.</p>"""
    priority: NotRequired["int"]
    """<p>The run's priority.</p>"""
    storage_capacity: NotRequired["int"]
    """<p>The run's storage capacity in gibibytes. For dynamic storage, after the run has completed, this value is the maximum amount of storage used during the run.</p>"""
    creation_time: NotRequired["aws_sdk_omics.types.run_timestamp.RunTimestamp"]
    """<p>When the run was created.</p>"""
    start_time: NotRequired["aws_sdk_omics.types.run_timestamp.RunTimestamp"]
    """<p>When the run started.</p>"""
    stop_time: NotRequired["aws_sdk_omics.types.run_timestamp.RunTimestamp"]
    """<p>When the run stopped.</p>"""
    storage_type: NotRequired["aws_sdk_omics.types.storage_type.StorageType"]
    """<p>The run's storage type.</p>"""
    workflow_version_name: NotRequired[
        "aws_sdk_omics.types.workflow_version_name.WorkflowVersionName"
    ]
    """<p>The name of the workflow version.</p>"""
    workflow_name: NotRequired["aws_sdk_omics.types.workflow_name.WorkflowName"]
    """<p>The name of the workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RunListItem) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "status" in value:
        out["status"] = value["status"]
    if "workflow_id" in value:
        out["workflowId"] = value["workflow_id"]
    if "batch_id" in value:
        out["batchId"] = value["batch_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "priority" in value:
        out["priority"] = value["priority"]
    if "storage_capacity" in value:
        out["storageCapacity"] = value["storage_capacity"]
    if "creation_time" in value:
        import aws_sdk_omics.types.run_timestamp

        out["creationTime"] = aws_sdk_omics.types.run_timestamp.serialize_json(
            value["creation_time"]
        )
    if "start_time" in value:
        import aws_sdk_omics.types.run_timestamp

        out["startTime"] = aws_sdk_omics.types.run_timestamp.serialize_json(
            value["start_time"]
        )
    if "stop_time" in value:
        import aws_sdk_omics.types.run_timestamp

        out["stopTime"] = aws_sdk_omics.types.run_timestamp.serialize_json(
            value["stop_time"]
        )
    if "storage_type" in value:
        out["storageType"] = value["storage_type"]
    if "workflow_version_name" in value:
        out["workflowVersionName"] = value["workflow_version_name"]
    if "workflow_name" in value:
        out["workflowName"] = value["workflow_name"]
    return out


def deserialize_json(data: dict) -> RunListItem:
    out: RunListItem = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    if "status" in data:
        out["status"] = data["status"]
    if "workflowId" in data:
        out["workflow_id"] = data["workflowId"]
    if "batchId" in data:
        out["batch_id"] = data["batchId"]
    if "name" in data:
        out["name"] = data["name"]
    if "priority" in data:
        out["priority"] = data["priority"]
    if "storageCapacity" in data:
        out["storage_capacity"] = data["storageCapacity"]
    if "creationTime" in data:
        import aws_sdk_omics.types.run_timestamp

        out["creation_time"] = aws_sdk_omics.types.run_timestamp.deserialize_json(
            data["creationTime"]
        )
    if "startTime" in data:
        import aws_sdk_omics.types.run_timestamp

        out["start_time"] = aws_sdk_omics.types.run_timestamp.deserialize_json(
            data["startTime"]
        )
    if "stopTime" in data:
        import aws_sdk_omics.types.run_timestamp

        out["stop_time"] = aws_sdk_omics.types.run_timestamp.deserialize_json(
            data["stopTime"]
        )
    if "storageType" in data:
        out["storage_type"] = data["storageType"]
    if "workflowVersionName" in data:
        out["workflow_version_name"] = data["workflowVersionName"]
    if "workflowName" in data:
        out["workflow_name"] = data["workflowName"]
    return out
