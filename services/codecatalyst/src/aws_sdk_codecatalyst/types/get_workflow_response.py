"""Generated from Smithy shape ``com.amazonaws.codecatalyst#GetWorkflowResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.name_string
    import aws_sdk_codecatalyst.types.source_repository_branch_string
    import aws_sdk_codecatalyst.types.source_repository_name_string
    import aws_sdk_codecatalyst.types.timestamp
    import aws_sdk_codecatalyst.types.uuid
    import aws_sdk_codecatalyst.types.workflow_definition
    import aws_sdk_codecatalyst.types.workflow_run_mode
    import aws_sdk_codecatalyst.types.workflow_status


class GetWorkflowResponse(TypedDict):
    space_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    id: "aws_sdk_codecatalyst.types.uuid.Uuid"
    """<p>The ID of the workflow.</p>"""
    name: "str"
    """<p>The name of the workflow.</p>"""
    source_repository_name: NotRequired[
        "aws_sdk_codecatalyst.types.source_repository_name_string.SourceRepositoryNameString"
    ]
    """<p>The name of the source repository where the workflow YAML is stored.</p>"""
    source_branch_name: NotRequired[
        "aws_sdk_codecatalyst.types.source_repository_branch_string.SourceRepositoryBranchString"
    ]
    """<p>The name of the branch that contains the workflow YAML.</p>"""
    definition: "aws_sdk_codecatalyst.types.workflow_definition.WorkflowDefinition"
    """<p>Information about the workflow definition file for the workflow.</p>"""
    created_time: "aws_sdk_codecatalyst.types.timestamp.Timestamp"
    r"""<p>The date and time the workflow was created, in coordinated universal time (UTC) timestamp format as specified in <a href=\"https://www.rfc-editor.org/rfc/rfc3339#section-5.6\">RFC 3339</a> </p>"""
    last_updated_time: "aws_sdk_codecatalyst.types.timestamp.Timestamp"
    r"""<p>The date and time the workflow was last updated, in coordinated universal time (UTC) timestamp format as specified in <a href=\"https://www.rfc-editor.org/rfc/rfc3339#section-5.6\">RFC 3339</a> </p>"""
    run_mode: "aws_sdk_codecatalyst.types.workflow_run_mode.WorkflowRunMode"
    r"""<p>The behavior to use when multiple workflows occur at the same time. For more information, see <a href=\"https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-configure-runs.html\">https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-configure-runs.html</a> in the Amazon CodeCatalyst User Guide.</p>"""
    status: "aws_sdk_codecatalyst.types.workflow_status.WorkflowStatus"
    """<p>The status of the workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowResponse) -> dict:
    out: dict = {}
    out["spaceName"] = value["space_name"]
    out["projectName"] = value["project_name"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "source_repository_name" in value:
        out["sourceRepositoryName"] = value["source_repository_name"]
    if "source_branch_name" in value:
        out["sourceBranchName"] = value["source_branch_name"]
    import aws_sdk_codecatalyst.types.workflow_definition

    out["definition"] = aws_sdk_codecatalyst.types.workflow_definition.serialize_json(
        value["definition"]
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


def deserialize_json(data: dict) -> GetWorkflowResponse:
    out: GetWorkflowResponse = {}  # type: ignore[typeddict-item]
    if "spaceName" in data:
        out["space_name"] = data["spaceName"]
    else:
        raise DeserializationError("GetWorkflowResponse.space_name required")
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError("GetWorkflowResponse.project_name required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetWorkflowResponse.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetWorkflowResponse.name required")
    if "sourceRepositoryName" in data:
        out["source_repository_name"] = data["sourceRepositoryName"]
    if "sourceBranchName" in data:
        out["source_branch_name"] = data["sourceBranchName"]
    if "definition" in data:
        import aws_sdk_codecatalyst.types.workflow_definition

        out["definition"] = (
            aws_sdk_codecatalyst.types.workflow_definition.deserialize_json(
                data["definition"]
            )
        )
    else:
        raise DeserializationError("GetWorkflowResponse.definition required")
    if "createdTime" in data:
        import aws_sdk_codecatalyst.types.timestamp

        out["created_time"] = aws_sdk_codecatalyst.types.timestamp.deserialize_json(
            data["createdTime"]
        )
    else:
        raise DeserializationError("GetWorkflowResponse.created_time required")
    if "lastUpdatedTime" in data:
        import aws_sdk_codecatalyst.types.timestamp

        out["last_updated_time"] = (
            aws_sdk_codecatalyst.types.timestamp.deserialize_json(
                data["lastUpdatedTime"]
            )
        )
    else:
        raise DeserializationError("GetWorkflowResponse.last_updated_time required")
    if "runMode" in data:
        out["run_mode"] = data["runMode"]
    else:
        raise DeserializationError("GetWorkflowResponse.run_mode required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetWorkflowResponse.status required")
    return out
