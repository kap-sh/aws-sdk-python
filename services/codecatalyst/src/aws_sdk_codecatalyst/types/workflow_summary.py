"""Generated from Smithy shape ``com.amazonaws.codecatalyst#WorkflowSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.source_repository_branch_string
    import aws_sdk_codecatalyst.types.source_repository_name_string
    import aws_sdk_codecatalyst.types.timestamp
    import aws_sdk_codecatalyst.types.uuid
    import aws_sdk_codecatalyst.types.workflow_definition_summary
    import aws_sdk_codecatalyst.types.workflow_run_mode
    import aws_sdk_codecatalyst.types.workflow_status


class WorkflowSummary(TypedDict):
    id: "aws_sdk_codecatalyst.types.uuid.Uuid"
    """<p>The system-generated unique ID of a workflow.</p>"""
    name: "str"
    """<p>The name of the workflow.</p>"""
    source_repository_name: "aws_sdk_codecatalyst.types.source_repository_name_string.SourceRepositoryNameString"
    """<p>The name of the source repository where the workflow definition file is stored.</p>"""
    source_branch_name: "aws_sdk_codecatalyst.types.source_repository_branch_string.SourceRepositoryBranchString"
    """<p>The name of the branch of the source repository where the workflow definition file is stored.</p>"""
    definition: "aws_sdk_codecatalyst.types.workflow_definition_summary.WorkflowDefinitionSummary"
    """<p>Information about the workflow definition file.</p>"""
    created_time: "aws_sdk_codecatalyst.types.timestamp.Timestamp"
    """<p>The date and time the workflow was created, in coordinated universal time (UTC) timestamp format as specified in <a href=\"https://www.rfc-editor.org/rfc/rfc3339#section-5.6\">RFC 3339</a> </p>"""
    last_updated_time: "aws_sdk_codecatalyst.types.timestamp.Timestamp"
    """<p>The date and time the workflow was last updated, in coordinated universal time (UTC) timestamp format as specified in <a href=\"https://www.rfc-editor.org/rfc/rfc3339#section-5.6\">RFC 3339</a> </p>"""
    run_mode: "aws_sdk_codecatalyst.types.workflow_run_mode.WorkflowRunMode"
    """<p>The run mode of the workflow.</p>"""
    status: "aws_sdk_codecatalyst.types.workflow_status.WorkflowStatus"
    """<p>The status of the workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["sourceRepositoryName"] = value["source_repository_name"]
    out["sourceBranchName"] = value["source_branch_name"]
    import aws_sdk_codecatalyst.types.workflow_definition_summary

    out["definition"] = (
        aws_sdk_codecatalyst.types.workflow_definition_summary.serialize_json(
            value["definition"]
        )
    )
    import aws_sdk_codecatalyst.types.timestamp

    out["createdTime"] = aws_sdk_codecatalyst.types.timestamp.serialize_json(
        value["created_time"]
    )
    import aws_sdk_codecatalyst.types.timestamp

    out["lastUpdatedTime"] = aws_sdk_codecatalyst.types.timestamp.serialize_json(
        value["last_updated_time"]
    )
    out["runMode"] = value["run_mode"]
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> WorkflowSummary:
    out: WorkflowSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("WorkflowSummary.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("WorkflowSummary.name required")
    if "sourceRepositoryName" in data:
        out["source_repository_name"] = data["sourceRepositoryName"]
    else:
        raise DeserializationError("WorkflowSummary.source_repository_name required")
    if "sourceBranchName" in data:
        out["source_branch_name"] = data["sourceBranchName"]
    else:
        raise DeserializationError("WorkflowSummary.source_branch_name required")
    if "definition" in data:
        import aws_sdk_codecatalyst.types.workflow_definition_summary

        out["definition"] = (
            aws_sdk_codecatalyst.types.workflow_definition_summary.deserialize_json(
                data["definition"]
            )
        )
    else:
        raise DeserializationError("WorkflowSummary.definition required")
    if "createdTime" in data:
        import aws_sdk_codecatalyst.types.timestamp

        out["created_time"] = aws_sdk_codecatalyst.types.timestamp.deserialize_json(
            data["createdTime"]
        )
    else:
        raise DeserializationError("WorkflowSummary.created_time required")
    if "lastUpdatedTime" in data:
        import aws_sdk_codecatalyst.types.timestamp

        out["last_updated_time"] = (
            aws_sdk_codecatalyst.types.timestamp.deserialize_json(
                data["lastUpdatedTime"]
            )
        )
    else:
        raise DeserializationError("WorkflowSummary.last_updated_time required")
    if "runMode" in data:
        out["run_mode"] = data["runMode"]
    else:
        raise DeserializationError("WorkflowSummary.run_mode required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("WorkflowSummary.status required")
    return out
