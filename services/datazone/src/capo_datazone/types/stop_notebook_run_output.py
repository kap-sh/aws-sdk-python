"""Generated from Smithy shape ``com.amazonaws.datazone#StopNotebookRunOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.notebook_run_id
    import capo_datazone.types.notebook_run_status
    import capo_datazone.types.project_id


class StopNotebookRunOutput(TypedDict, closed=True):
    id: "capo_datazone.types.notebook_run_id.NotebookRunId"
    """<p>The identifier of the notebook run.</p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain.</p>"""
    owning_project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that owns the notebook run.</p>"""
    status: "capo_datazone.types.notebook_run_status.NotebookRunStatus"
    """<p>The status of the notebook run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopNotebookRunOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["domainId"] = value["domain_id"]
    out["owningProjectId"] = value["owning_project_id"]
    import capo_datazone.types.notebook_run_status

    out["status"] = capo_datazone.types.notebook_run_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> StopNotebookRunOutput:
    out: StopNotebookRunOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("StopNotebookRunOutput.id required")
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("StopNotebookRunOutput.domain_id required")
    if "owningProjectId" in data:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        raise DeserializationError("StopNotebookRunOutput.owning_project_id required")
    if "status" in data:
        import capo_datazone.types.notebook_run_status

        out["status"] = capo_datazone.types.notebook_run_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("StopNotebookRunOutput.status required")
    return out
