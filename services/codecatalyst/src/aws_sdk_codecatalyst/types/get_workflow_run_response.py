"""Generated from Smithy shape ``com.amazonaws.codecatalyst#GetWorkflowRunResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.name_string
    import aws_sdk_codecatalyst.types.timestamp
    import aws_sdk_codecatalyst.types.uuid
    import aws_sdk_codecatalyst.types.workflow_run_status
    import aws_sdk_codecatalyst.types.workflow_run_status_reasons


class GetWorkflowRunResponse(TypedDict):
    space_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    id: "aws_sdk_codecatalyst.types.uuid.Uuid"
    """<p>The ID of the workflow run.</p>"""
    workflow_id: "aws_sdk_codecatalyst.types.uuid.Uuid"
    """<p>The ID of the workflow.</p>"""
    status: "aws_sdk_codecatalyst.types.workflow_run_status.WorkflowRunStatus"
    """<p>The status of the workflow run.</p>"""
    status_reasons: NotRequired[
        "aws_sdk_codecatalyst.types.workflow_run_status_reasons.WorkflowRunStatusReasons"
    ]
    """<p>Information about the reasons for the status of the workflow run.</p>"""
    start_time: "aws_sdk_codecatalyst.types.timestamp.Timestamp"
    """<p>The date and time the workflow run began, in coordinated universal time (UTC) timestamp format as specified in <a href=\"https://www.rfc-editor.org/rfc/rfc3339#section-5.6\">RFC 3339</a> </p>"""
    end_time: NotRequired["aws_sdk_codecatalyst.types.timestamp.Timestamp"]
    """<p>The date and time the workflow run ended, in coordinated universal time (UTC) timestamp format as specified in <a href=\"https://www.rfc-editor.org/rfc/rfc3339#section-5.6\">RFC 3339</a>.</p>"""
    last_updated_time: "aws_sdk_codecatalyst.types.timestamp.Timestamp"
    """<p>The date and time the workflow run status was last updated, in coordinated universal time (UTC) timestamp format as specified in <a href=\"https://www.rfc-editor.org/rfc/rfc3339#section-5.6\">RFC 3339</a> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowRunResponse) -> dict:
    out: dict = {}
    out["spaceName"] = value["space_name"]
    out["projectName"] = value["project_name"]
    out["id"] = value["id"]
    out["workflowId"] = value["workflow_id"]
    out["status"] = value["status"]
    if "status_reasons" in value:
        import aws_sdk_codecatalyst.types.workflow_run_status_reasons

        out["statusReasons"] = (
            aws_sdk_codecatalyst.types.workflow_run_status_reasons.serialize_json(
                value["status_reasons"]
            )
        )
    import aws_sdk_codecatalyst.types.timestamp

    out["startTime"] = aws_sdk_codecatalyst.types.timestamp.serialize_json(
        value["start_time"]
    )
    if "end_time" in value:
        import aws_sdk_codecatalyst.types.timestamp

        out["endTime"] = aws_sdk_codecatalyst.types.timestamp.serialize_json(
            value["end_time"]
        )
    import aws_sdk_codecatalyst.types.timestamp

    out["lastUpdatedTime"] = aws_sdk_codecatalyst.types.timestamp.serialize_json(
        value["last_updated_time"]
    )
    return out


def deserialize_json(data: dict) -> GetWorkflowRunResponse:
    out: GetWorkflowRunResponse = {}  # type: ignore[typeddict-item]
    if "spaceName" in data:
        out["space_name"] = data["spaceName"]
    else:
        raise DeserializationError("GetWorkflowRunResponse.space_name required")
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError("GetWorkflowRunResponse.project_name required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetWorkflowRunResponse.id required")
    if "workflowId" in data:
        out["workflow_id"] = data["workflowId"]
    else:
        raise DeserializationError("GetWorkflowRunResponse.workflow_id required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetWorkflowRunResponse.status required")
    if "statusReasons" in data:
        import aws_sdk_codecatalyst.types.workflow_run_status_reasons

        out["status_reasons"] = (
            aws_sdk_codecatalyst.types.workflow_run_status_reasons.deserialize_json(
                data["statusReasons"]
            )
        )
    if "startTime" in data:
        import aws_sdk_codecatalyst.types.timestamp

        out["start_time"] = aws_sdk_codecatalyst.types.timestamp.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("GetWorkflowRunResponse.start_time required")
    if "endTime" in data:
        import aws_sdk_codecatalyst.types.timestamp

        out["end_time"] = aws_sdk_codecatalyst.types.timestamp.deserialize_json(
            data["endTime"]
        )
    if "lastUpdatedTime" in data:
        import aws_sdk_codecatalyst.types.timestamp

        out["last_updated_time"] = (
            aws_sdk_codecatalyst.types.timestamp.deserialize_json(
                data["lastUpdatedTime"]
            )
        )
    else:
        raise DeserializationError("GetWorkflowRunResponse.last_updated_time required")
    return out
