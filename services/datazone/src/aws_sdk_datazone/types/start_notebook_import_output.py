"""Generated from Smithy shape ``com.amazonaws.datazone#StartNotebookImportOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.notebook_id
    import aws_sdk_datazone.types.notebook_name
    import aws_sdk_datazone.types.notebook_status
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.source_location


class StartNotebookImportOutput(TypedDict, closed=True):
    notebook_id: NotRequired["aws_sdk_datazone.types.notebook_id.NotebookId"]
    """<p>The identifier of the imported notebook.</p>"""
    status: NotRequired["aws_sdk_datazone.types.notebook_status.NotebookStatus"]
    """<p>The status of the notebook import.</p>"""
    domain_id: NotRequired["aws_sdk_datazone.types.domain_id.DomainId"]
    """<p>The identifier of the Amazon SageMaker Unified Studio domain.</p>"""
    owning_project_id: NotRequired["aws_sdk_datazone.types.project_id.ProjectId"]
    """<p>The identifier of the project that owns the imported notebook.</p>"""
    name: NotRequired["aws_sdk_datazone.types.notebook_name.NotebookName"]
    """<p>The name of the imported notebook.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the imported notebook.</p>"""
    source_location: NotRequired[
        "aws_sdk_datazone.types.source_location.SourceLocation"
    ]
    """<p>The source location from which the notebook was imported.</p>"""
    created_at: NotRequired["aws_sdk_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the notebook import was started.</p>"""
    created_by: NotRequired["aws_sdk_datazone.types.created_by.CreatedBy"]
    """<p>The identifier of the user who started the notebook import.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNotebookImportOutput) -> dict:
    out: dict = {}
    if "notebook_id" in value:
        out["notebookId"] = value["notebook_id"]
    if "status" in value:
        import aws_sdk_datazone.types.notebook_status

        out["status"] = aws_sdk_datazone.types.notebook_status.serialize_json(
            value["status"]
        )
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    if "owning_project_id" in value:
        out["owningProjectId"] = value["owning_project_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "source_location" in value:
        import aws_sdk_datazone.types.source_location

        out["sourceLocation"] = aws_sdk_datazone.types.source_location.serialize_json(
            value["source_location"]
        )
    if "created_at" in value:
        import aws_sdk_datazone.types.created_at

        out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    return out


def deserialize_json(data: dict) -> StartNotebookImportOutput:
    out: StartNotebookImportOutput = {}  # type: ignore[typeddict-item]
    if "notebookId" in data:
        out["notebook_id"] = data["notebookId"]
    if "status" in data:
        import aws_sdk_datazone.types.notebook_status

        out["status"] = aws_sdk_datazone.types.notebook_status.deserialize_json(
            data["status"]
        )
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    if "owningProjectId" in data:
        out["owning_project_id"] = data["owningProjectId"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "sourceLocation" in data:
        import aws_sdk_datazone.types.source_location

        out["source_location"] = (
            aws_sdk_datazone.types.source_location.deserialize_json(
                data["sourceLocation"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    return out
