"""Generated from Smithy shape ``com.amazonaws.datazone#GetNotebookOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_datazone.types.cell_order
    import aws_sdk_datazone.types.compute_id
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_config
    import aws_sdk_datazone.types.metadata
    import aws_sdk_datazone.types.notebook_error
    import aws_sdk_datazone.types.notebook_id
    import aws_sdk_datazone.types.notebook_name
    import aws_sdk_datazone.types.notebook_status
    import aws_sdk_datazone.types.parameters
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.updated_at
    import aws_sdk_datazone.types.updated_by


class GetNotebookOutput(TypedDict):
    id: "aws_sdk_datazone.types.notebook_id.NotebookId"
    """<p>The identifier of the notebook.</p>"""
    name: "aws_sdk_datazone.types.notebook_name.NotebookName"
    """<p>The name of the notebook.</p>"""
    owning_project_id: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that owns the notebook.</p>"""
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain.</p>"""
    cell_order: "aws_sdk_datazone.types.cell_order.CellOrder"
    """<p>The ordered list of cells in the notebook.</p>"""
    status: "aws_sdk_datazone.types.notebook_status.NotebookStatus"
    """<p>The status of the notebook.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the notebook.</p>"""
    created_at: NotRequired["aws_sdk_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the notebook was created.</p>"""
    created_by: NotRequired["aws_sdk_datazone.types.created_by.CreatedBy"]
    """<p>The identifier of the user who created the notebook.</p>"""
    updated_at: NotRequired["aws_sdk_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp of when the notebook was last updated.</p>"""
    updated_by: NotRequired["aws_sdk_datazone.types.updated_by.UpdatedBy"]
    """<p>The identifier of the user who last updated the notebook.</p>"""
    locked_by: NotRequired["str"]
    """<p>The identifier of the user who locked the notebook.</p>"""
    locked_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the notebook was locked.</p>"""
    lock_expires_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the notebook lock expires.</p>"""
    compute_id: NotRequired["aws_sdk_datazone.types.compute_id.ComputeId"]
    """<p>The identifier of the compute associated with the notebook.</p>"""
    metadata: NotRequired["aws_sdk_datazone.types.metadata.Metadata"]
    """<p>The metadata of the notebook.</p>"""
    parameters: NotRequired["aws_sdk_datazone.types.parameters.Parameters"]
    """<p>The sensitive parameters of the notebook.</p>"""
    environment_configuration: NotRequired[
        "aws_sdk_datazone.types.environment_config.EnvironmentConfig"
    ]
    """<p>The environment configuration of the notebook.</p>"""
    error: NotRequired["aws_sdk_datazone.types.notebook_error.NotebookError"]
    """<p>The error details if the notebook is in a failed state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNotebookOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["owningProjectId"] = value["owning_project_id"]
    out["domainId"] = value["domain_id"]
    import aws_sdk_datazone.types.cell_order

    out["cellOrder"] = aws_sdk_datazone.types.cell_order.serialize_json(
        value["cell_order"]
    )
    import aws_sdk_datazone.types.notebook_status

    out["status"] = aws_sdk_datazone.types.notebook_status.serialize_json(
        value["status"]
    )
    if "description" in value:
        out["description"] = value["description"]
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
    if "locked_by" in value:
        out["lockedBy"] = value["locked_by"]
    if "locked_at" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["lockedAt"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["locked_at"]
        )
    if "lock_expires_at" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["lockExpiresAt"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["lock_expires_at"]
        )
    if "compute_id" in value:
        out["computeId"] = value["compute_id"]
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
    if "environment_configuration" in value:
        import aws_sdk_datazone.types.environment_config

        out["environmentConfiguration"] = (
            aws_sdk_datazone.types.environment_config.serialize_json(
                value["environment_configuration"]
            )
        )
    if "error" in value:
        import aws_sdk_datazone.types.notebook_error

        out["error"] = aws_sdk_datazone.types.notebook_error.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> GetNotebookOutput:
    out: GetNotebookOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetNotebookOutput.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetNotebookOutput.name required")
    if "owningProjectId" in data:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        raise DeserializationError("GetNotebookOutput.owning_project_id required")
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("GetNotebookOutput.domain_id required")
    if "cellOrder" in data:
        import aws_sdk_datazone.types.cell_order

        out["cell_order"] = aws_sdk_datazone.types.cell_order.deserialize_json(
            data["cellOrder"]
        )
    else:
        raise DeserializationError("GetNotebookOutput.cell_order required")
    if "status" in data:
        import aws_sdk_datazone.types.notebook_status

        out["status"] = aws_sdk_datazone.types.notebook_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetNotebookOutput.status required")
    if "description" in data:
        out["description"] = data["description"]
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
    if "lockedBy" in data:
        out["locked_by"] = data["lockedBy"]
    if "lockedAt" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["locked_at"] = aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
            data["lockedAt"]
        )
    if "lockExpiresAt" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["lock_expires_at"] = (
            aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
                data["lockExpiresAt"]
            )
        )
    if "computeId" in data:
        out["compute_id"] = data["computeId"]
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
    if "environmentConfiguration" in data:
        import aws_sdk_datazone.types.environment_config

        out["environment_configuration"] = (
            aws_sdk_datazone.types.environment_config.deserialize_json(
                data["environmentConfiguration"]
            )
        )
    if "error" in data:
        import aws_sdk_datazone.types.notebook_error

        out["error"] = aws_sdk_datazone.types.notebook_error.deserialize_json(
            data["error"]
        )
    return out
