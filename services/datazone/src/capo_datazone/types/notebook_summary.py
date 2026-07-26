"""Generated from Smithy shape ``com.amazonaws.datazone#NotebookSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.notebook_id
    import capo_datazone.types.notebook_name
    import capo_datazone.types.notebook_status
    import capo_datazone.types.project_id
    import capo_datazone.types.updated_at
    import capo_datazone.types.updated_by


class NotebookSummary(TypedDict, closed=True):
    id: "capo_datazone.types.notebook_id.NotebookId"
    """<p>The identifier of the notebook.</p>"""
    name: "capo_datazone.types.notebook_name.NotebookName"
    """<p>The name of the notebook.</p>"""
    owning_project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that owns the notebook.</p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain.</p>"""
    status: "capo_datazone.types.notebook_status.NotebookStatus"
    """<p>The status of the notebook.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the notebook.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the notebook was created.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The identifier of the user who created the notebook.</p>"""
    updated_at: NotRequired["capo_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp of when the notebook was last updated.</p>"""
    updated_by: NotRequired["capo_datazone.types.updated_by.UpdatedBy"]
    """<p>The identifier of the user who last updated the notebook.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotebookSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["owningProjectId"] = value["owning_project_id"]
    out["domainId"] = value["domain_id"]
    import capo_datazone.types.notebook_status

    out["status"] = capo_datazone.types.notebook_status.serialize_json(value["status"])
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import capo_datazone.types.updated_at

        out["updatedAt"] = capo_datazone.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    return out


def deserialize_json(data: dict) -> NotebookSummary:
    out: NotebookSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("NotebookSummary.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("NotebookSummary.name required")
    if "owningProjectId" in data:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        raise DeserializationError("NotebookSummary.owning_project_id required")
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("NotebookSummary.domain_id required")
    if "status" in data:
        import capo_datazone.types.notebook_status

        out["status"] = capo_datazone.types.notebook_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("NotebookSummary.status required")
    if "description" in data:
        out["description"] = data["description"]
    if "createdAt" in data:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "updatedAt" in data:
        import capo_datazone.types.updated_at

        out["updated_at"] = capo_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    return out
