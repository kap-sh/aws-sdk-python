"""Generated from Smithy shape ``com.amazonaws.datazone#StartNotebookExportInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.file_format
    import aws_sdk_datazone.types.notebook_id
    import aws_sdk_datazone.types.project_id


class StartNotebookExportInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain in which to export the notebook.</p>"""
    notebook_identifier: "aws_sdk_datazone.types.notebook_id.NotebookId"
    """<p>The identifier of the notebook to export.</p>"""
    owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that owns the notebook.</p>"""
    file_format: "aws_sdk_datazone.types.file_format.FileFormat"
    """<p>The file format for the notebook export. Valid values are <code>PDF</code> and <code>IPYNB</code>.</p>"""
    client_token: NotRequired["aws_sdk_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNotebookExportInput) -> dict:
    out: dict = {}
    out["notebookIdentifier"] = value["notebook_identifier"]
    out["owningProjectIdentifier"] = value["owning_project_identifier"]
    import aws_sdk_datazone.types.file_format

    out["fileFormat"] = aws_sdk_datazone.types.file_format.serialize_json(
        value["file_format"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartNotebookExportInput:
    out: StartNotebookExportInput = {}  # type: ignore[typeddict-item]
    if "notebookIdentifier" in data:
        out["notebook_identifier"] = data["notebookIdentifier"]
    else:
        raise DeserializationError(
            "StartNotebookExportInput.notebook_identifier required"
        )
    if "owningProjectIdentifier" in data:
        out["owning_project_identifier"] = data["owningProjectIdentifier"]
    else:
        raise DeserializationError(
            "StartNotebookExportInput.owning_project_identifier required"
        )
    if "fileFormat" in data:
        import aws_sdk_datazone.types.file_format

        out["file_format"] = aws_sdk_datazone.types.file_format.deserialize_json(
            data["fileFormat"]
        )
    else:
        raise DeserializationError("StartNotebookExportInput.file_format required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
