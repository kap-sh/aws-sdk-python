"""Generated from Smithy shape ``com.amazonaws.datazone#GetNotebookExportOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.completed_at
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.export_id
    import aws_sdk_datazone.types.file_format
    import aws_sdk_datazone.types.notebook_export_error
    import aws_sdk_datazone.types.notebook_export_status
    import aws_sdk_datazone.types.notebook_id
    import aws_sdk_datazone.types.output_location
    import aws_sdk_datazone.types.project_id


class GetNotebookExportOutput(TypedDict, closed=True):
    id: "aws_sdk_datazone.types.export_id.ExportId"
    """<p>The identifier of the notebook export.</p>"""
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain.</p>"""
    owning_project_id: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that owns the notebook.</p>"""
    notebook_id: "aws_sdk_datazone.types.notebook_id.NotebookId"
    """<p>The identifier of the notebook.</p>"""
    file_format: "aws_sdk_datazone.types.file_format.FileFormat"
    """<p>The file format of the notebook export.</p>"""
    status: "aws_sdk_datazone.types.notebook_export_status.NotebookExportStatus"
    """<p>The status of the notebook export.</p>"""
    output_location: NotRequired[
        "aws_sdk_datazone.types.output_location.OutputLocation"
    ]
    """<p>The output location of the exported notebook in Amazon Simple Storage Service.</p>"""
    error: NotRequired[
        "aws_sdk_datazone.types.notebook_export_error.NotebookExportError"
    ]
    """<p>The error details if the notebook export failed.</p>"""
    completed_at: NotRequired["aws_sdk_datazone.types.completed_at.CompletedAt"]
    """<p>The timestamp of when the notebook export completed.</p>"""
    created_at: NotRequired["aws_sdk_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the notebook export was started.</p>"""
    created_by: NotRequired["aws_sdk_datazone.types.created_by.CreatedBy"]
    """<p>The identifier of the user who started the notebook export.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNotebookExportOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["domainId"] = value["domain_id"]
    out["owningProjectId"] = value["owning_project_id"]
    out["notebookId"] = value["notebook_id"]
    import aws_sdk_datazone.types.file_format

    out["fileFormat"] = aws_sdk_datazone.types.file_format.serialize_json(
        value["file_format"]
    )
    import aws_sdk_datazone.types.notebook_export_status

    out["status"] = aws_sdk_datazone.types.notebook_export_status.serialize_json(
        value["status"]
    )
    if "output_location" in value:
        import aws_sdk_datazone.types.output_location

        out["outputLocation"] = aws_sdk_datazone.types.output_location.serialize_json(
            value["output_location"]
        )
    if "error" in value:
        import aws_sdk_datazone.types.notebook_export_error

        out["error"] = aws_sdk_datazone.types.notebook_export_error.serialize_json(
            value["error"]
        )
    if "completed_at" in value:
        import aws_sdk_datazone.types.completed_at

        out["completedAt"] = aws_sdk_datazone.types.completed_at.serialize_json(
            value["completed_at"]
        )
    if "created_at" in value:
        import aws_sdk_datazone.types.created_at

        out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    return out


def deserialize_json(data: dict) -> GetNotebookExportOutput:
    out: GetNotebookExportOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetNotebookExportOutput.id required")
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("GetNotebookExportOutput.domain_id required")
    if "owningProjectId" in data:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        raise DeserializationError("GetNotebookExportOutput.owning_project_id required")
    if "notebookId" in data:
        out["notebook_id"] = data["notebookId"]
    else:
        raise DeserializationError("GetNotebookExportOutput.notebook_id required")
    if "fileFormat" in data:
        import aws_sdk_datazone.types.file_format

        out["file_format"] = aws_sdk_datazone.types.file_format.deserialize_json(
            data["fileFormat"]
        )
    else:
        raise DeserializationError("GetNotebookExportOutput.file_format required")
    if "status" in data:
        import aws_sdk_datazone.types.notebook_export_status

        out["status"] = aws_sdk_datazone.types.notebook_export_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetNotebookExportOutput.status required")
    if "outputLocation" in data:
        import aws_sdk_datazone.types.output_location

        out["output_location"] = (
            aws_sdk_datazone.types.output_location.deserialize_json(
                data["outputLocation"]
            )
        )
    if "error" in data:
        import aws_sdk_datazone.types.notebook_export_error

        out["error"] = aws_sdk_datazone.types.notebook_export_error.deserialize_json(
            data["error"]
        )
    if "completedAt" in data:
        import aws_sdk_datazone.types.completed_at

        out["completed_at"] = aws_sdk_datazone.types.completed_at.deserialize_json(
            data["completedAt"]
        )
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    return out
