"""Generated from Smithy shape ``com.amazonaws.datazone#StartNotebookRunOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_datazone.types.cell_order
    import aws_sdk_datazone.types.compute_config
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_config
    import aws_sdk_datazone.types.metadata
    import aws_sdk_datazone.types.network_config
    import aws_sdk_datazone.types.notebook_id
    import aws_sdk_datazone.types.notebook_run_error
    import aws_sdk_datazone.types.notebook_run_id
    import aws_sdk_datazone.types.notebook_run_status
    import aws_sdk_datazone.types.parameters
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.schedule_id
    import aws_sdk_datazone.types.storage_config
    import aws_sdk_datazone.types.timeout_config
    import aws_sdk_datazone.types.trigger_source
    import aws_sdk_datazone.types.updated_at
    import aws_sdk_datazone.types.updated_by


class StartNotebookRunOutput(TypedDict):
    id: "aws_sdk_datazone.types.notebook_run_id.NotebookRunId"
    """<p>The identifier of the notebook run.</p>"""
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain.</p>"""
    owning_project_id: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that owns the notebook run.</p>"""
    notebook_id: "aws_sdk_datazone.types.notebook_id.NotebookId"
    """<p>The identifier of the notebook.</p>"""
    schedule_id: NotRequired["aws_sdk_datazone.types.schedule_id.ScheduleId"]
    """<p>The identifier of the schedule associated with the notebook run.</p>"""
    status: "aws_sdk_datazone.types.notebook_run_status.NotebookRunStatus"
    """<p>The status of the notebook run.</p>"""
    cell_order: NotRequired["aws_sdk_datazone.types.cell_order.CellOrder"]
    """<p>The ordered list of cells in the notebook run.</p>"""
    metadata: NotRequired["aws_sdk_datazone.types.metadata.Metadata"]
    """<p>The metadata of the notebook run.</p>"""
    parameters: NotRequired["aws_sdk_datazone.types.parameters.Parameters"]
    """<p>The sensitive parameters of the notebook run.</p>"""
    compute_configuration: NotRequired[
        "aws_sdk_datazone.types.compute_config.ComputeConfig"
    ]
    """<p>The compute configuration of the notebook run.</p>"""
    network_configuration: NotRequired[
        "aws_sdk_datazone.types.network_config.NetworkConfig"
    ]
    """<p>The network configuration of the notebook run.</p>"""
    timeout_configuration: NotRequired[
        "aws_sdk_datazone.types.timeout_config.TimeoutConfig"
    ]
    """<p>The timeout configuration of the notebook run.</p>"""
    environment_configuration: NotRequired[
        "aws_sdk_datazone.types.environment_config.EnvironmentConfig"
    ]
    """<p>The environment configuration of the notebook run, including image version and package settings.</p>"""
    storage_configuration: NotRequired[
        "aws_sdk_datazone.types.storage_config.StorageConfig"
    ]
    """<p>The storage configuration of the notebook run, including the Amazon Simple Storage Service path and KMS key ARN.</p>"""
    trigger_source: NotRequired["aws_sdk_datazone.types.trigger_source.TriggerSource"]
    """<p>The source that triggered the notebook run.</p>"""
    error: NotRequired["aws_sdk_datazone.types.notebook_run_error.NotebookRunError"]
    """<p>The error details if the notebook run failed.</p>"""
    created_at: NotRequired["aws_sdk_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the notebook run was created.</p>"""
    created_by: NotRequired["aws_sdk_datazone.types.created_by.CreatedBy"]
    """<p>The identifier of the user who created the notebook run.</p>"""
    updated_at: NotRequired["aws_sdk_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp of when the notebook run was last updated.</p>"""
    updated_by: NotRequired["aws_sdk_datazone.types.updated_by.UpdatedBy"]
    """<p>The identifier of the user who last updated the notebook run.</p>"""
    started_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the notebook run started executing.</p>"""
    completed_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the notebook run completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNotebookRunOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["domainId"] = value["domain_id"]
    out["owningProjectId"] = value["owning_project_id"]
    out["notebookId"] = value["notebook_id"]
    if "schedule_id" in value:
        out["scheduleId"] = value["schedule_id"]
    import aws_sdk_datazone.types.notebook_run_status

    out["status"] = aws_sdk_datazone.types.notebook_run_status.serialize_json(
        value["status"]
    )
    if "cell_order" in value:
        import aws_sdk_datazone.types.cell_order

        out["cellOrder"] = aws_sdk_datazone.types.cell_order.serialize_json(
            value["cell_order"]
        )
    if "metadata" in value:
        import aws_sdk_datazone.types.metadata

        out["metadata"] = aws_sdk_datazone.types.metadata.serialize_json(
            value["metadata"]
        )
    if "parameters" in value:
        import aws_sdk_datazone.types.parameters

        out["parameters"] = aws_sdk_datazone.types.parameters.serialize_json(
            value["parameters"]
        )
    if "compute_configuration" in value:
        import aws_sdk_datazone.types.compute_config

        out["computeConfiguration"] = (
            aws_sdk_datazone.types.compute_config.serialize_json(
                value["compute_configuration"]
            )
        )
    if "network_configuration" in value:
        import aws_sdk_datazone.types.network_config

        out["networkConfiguration"] = (
            aws_sdk_datazone.types.network_config.serialize_json(
                value["network_configuration"]
            )
        )
    if "timeout_configuration" in value:
        import aws_sdk_datazone.types.timeout_config

        out["timeoutConfiguration"] = (
            aws_sdk_datazone.types.timeout_config.serialize_json(
                value["timeout_configuration"]
            )
        )
    if "environment_configuration" in value:
        import aws_sdk_datazone.types.environment_config

        out["environmentConfiguration"] = (
            aws_sdk_datazone.types.environment_config.serialize_json(
                value["environment_configuration"]
            )
        )
    if "storage_configuration" in value:
        import aws_sdk_datazone.types.storage_config

        out["storageConfiguration"] = (
            aws_sdk_datazone.types.storage_config.serialize_json(
                value["storage_configuration"]
            )
        )
    if "trigger_source" in value:
        import aws_sdk_datazone.types.trigger_source

        out["triggerSource"] = aws_sdk_datazone.types.trigger_source.serialize_json(
            value["trigger_source"]
        )
    if "error" in value:
        import aws_sdk_datazone.types.notebook_run_error

        out["error"] = aws_sdk_datazone.types.notebook_run_error.serialize_json(
            value["error"]
        )
    if "created_at" in value:
        import aws_sdk_datazone.types.created_at

        out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import aws_sdk_datazone.types.updated_at

        out["updatedAt"] = aws_sdk_datazone.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "started_at" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["startedAt"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["started_at"]
        )
    if "completed_at" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["completedAt"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["completed_at"]
        )
    return out


def deserialize_json(data: dict) -> StartNotebookRunOutput:
    out: StartNotebookRunOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("StartNotebookRunOutput.id required")
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("StartNotebookRunOutput.domain_id required")
    if "owningProjectId" in data:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        raise DeserializationError("StartNotebookRunOutput.owning_project_id required")
    if "notebookId" in data:
        out["notebook_id"] = data["notebookId"]
    else:
        raise DeserializationError("StartNotebookRunOutput.notebook_id required")
    if "scheduleId" in data:
        out["schedule_id"] = data["scheduleId"]
    if "status" in data:
        import aws_sdk_datazone.types.notebook_run_status

        out["status"] = aws_sdk_datazone.types.notebook_run_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("StartNotebookRunOutput.status required")
    if "cellOrder" in data:
        import aws_sdk_datazone.types.cell_order

        out["cell_order"] = aws_sdk_datazone.types.cell_order.deserialize_json(
            data["cellOrder"]
        )
    if "metadata" in data:
        import aws_sdk_datazone.types.metadata

        out["metadata"] = aws_sdk_datazone.types.metadata.deserialize_json(
            data["metadata"]
        )
    if "parameters" in data:
        import aws_sdk_datazone.types.parameters

        out["parameters"] = aws_sdk_datazone.types.parameters.deserialize_json(
            data["parameters"]
        )
    if "computeConfiguration" in data:
        import aws_sdk_datazone.types.compute_config

        out["compute_configuration"] = (
            aws_sdk_datazone.types.compute_config.deserialize_json(
                data["computeConfiguration"]
            )
        )
    if "networkConfiguration" in data:
        import aws_sdk_datazone.types.network_config

        out["network_configuration"] = (
            aws_sdk_datazone.types.network_config.deserialize_json(
                data["networkConfiguration"]
            )
        )
    if "timeoutConfiguration" in data:
        import aws_sdk_datazone.types.timeout_config

        out["timeout_configuration"] = (
            aws_sdk_datazone.types.timeout_config.deserialize_json(
                data["timeoutConfiguration"]
            )
        )
    if "environmentConfiguration" in data:
        import aws_sdk_datazone.types.environment_config

        out["environment_configuration"] = (
            aws_sdk_datazone.types.environment_config.deserialize_json(
                data["environmentConfiguration"]
            )
        )
    if "storageConfiguration" in data:
        import aws_sdk_datazone.types.storage_config

        out["storage_configuration"] = (
            aws_sdk_datazone.types.storage_config.deserialize_json(
                data["storageConfiguration"]
            )
        )
    if "triggerSource" in data:
        import aws_sdk_datazone.types.trigger_source

        out["trigger_source"] = aws_sdk_datazone.types.trigger_source.deserialize_json(
            data["triggerSource"]
        )
    if "error" in data:
        import aws_sdk_datazone.types.notebook_run_error

        out["error"] = aws_sdk_datazone.types.notebook_run_error.deserialize_json(
            data["error"]
        )
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "updatedAt" in data:
        import aws_sdk_datazone.types.updated_at

        out["updated_at"] = aws_sdk_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "startedAt" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["started_at"] = aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
            data["startedAt"]
        )
    if "completedAt" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["completed_at"] = (
            aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
                data["completedAt"]
            )
        )
    return out
