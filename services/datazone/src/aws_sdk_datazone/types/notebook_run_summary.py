"""Generated from Smithy shape ``com.amazonaws.datazone#NotebookRunSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.notebook_id
    import aws_sdk_datazone.types.notebook_run_id
    import aws_sdk_datazone.types.notebook_run_status
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.schedule_id
    import aws_sdk_datazone.types.trigger_source
    import aws_sdk_datazone.types.updated_at
    import aws_sdk_datazone.types.updated_by


class NotebookRunSummary(TypedDict):
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
    trigger_source: NotRequired["aws_sdk_datazone.types.trigger_source.TriggerSource"]
    """<p>The source that triggered the notebook run.</p>"""
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
def serialize_json(value: NotebookRunSummary) -> dict:
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
    if "trigger_source" in value:
        import aws_sdk_datazone.types.trigger_source

        out["triggerSource"] = aws_sdk_datazone.types.trigger_source.serialize_json(
            value["trigger_source"]
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


def deserialize_json(data: dict) -> NotebookRunSummary:
    out: NotebookRunSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("NotebookRunSummary.id required")
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("NotebookRunSummary.domain_id required")
    if "owningProjectId" in data:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        raise DeserializationError("NotebookRunSummary.owning_project_id required")
    if "notebookId" in data:
        out["notebook_id"] = data["notebookId"]
    else:
        raise DeserializationError("NotebookRunSummary.notebook_id required")
    if "scheduleId" in data:
        out["schedule_id"] = data["scheduleId"]
    if "status" in data:
        import aws_sdk_datazone.types.notebook_run_status

        out["status"] = aws_sdk_datazone.types.notebook_run_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("NotebookRunSummary.status required")
    if "triggerSource" in data:
        import aws_sdk_datazone.types.trigger_source

        out["trigger_source"] = aws_sdk_datazone.types.trigger_source.deserialize_json(
            data["triggerSource"]
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
