"""Generated from Smithy shape ``com.amazonaws.datazone#StartNotebookExportOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.export_id
    import aws_sdk_datazone.types.file_format
    import aws_sdk_datazone.types.notebook_export_status
    import aws_sdk_datazone.types.notebook_id
    import aws_sdk_datazone.types.project_id


class StartNotebookExportOutput(TypedDict):
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
    created_at: NotRequired["aws_sdk_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the notebook export was started.</p>"""
    created_by: NotRequired["aws_sdk_datazone.types.created_by.CreatedBy"]
    """<p>The identifier of the user who started the notebook export.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNotebookExportOutput) -> dict:
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
    if "created_at" in value:
        import aws_sdk_datazone.types.created_at

        out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    return out


def deserialize_json(data: dict) -> StartNotebookExportOutput:
    out: StartNotebookExportOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("StartNotebookExportOutput.id required")
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("StartNotebookExportOutput.domain_id required")
    if "owningProjectId" in data:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        raise DeserializationError(
            "StartNotebookExportOutput.owning_project_id required"
        )
    if "notebookId" in data:
        out["notebook_id"] = data["notebookId"]
    else:
        raise DeserializationError("StartNotebookExportOutput.notebook_id required")
    if "fileFormat" in data:
        import aws_sdk_datazone.types.file_format

        out["file_format"] = aws_sdk_datazone.types.file_format.deserialize_json(
            data["fileFormat"]
        )
    else:
        raise DeserializationError("StartNotebookExportOutput.file_format required")
    if "status" in data:
        import aws_sdk_datazone.types.notebook_export_status

        out["status"] = aws_sdk_datazone.types.notebook_export_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("StartNotebookExportOutput.status required")
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    return out
