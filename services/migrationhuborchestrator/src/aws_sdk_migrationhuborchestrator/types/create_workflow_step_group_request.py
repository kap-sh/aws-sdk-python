"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#CreateWorkflowStepGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_migrationhuborchestrator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_id
    import aws_sdk_migrationhuborchestrator.types.step_group_description
    import aws_sdk_migrationhuborchestrator.types.step_group_name
    import aws_sdk_migrationhuborchestrator.types.string_list


class CreateWorkflowStepGroupRequest(TypedDict):
    workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    """<p>The ID of the migration workflow that will contain the step group.</p>"""
    name: "aws_sdk_migrationhuborchestrator.types.step_group_name.StepGroupName"
    """<p>The name of the step group.</p>"""
    description: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.step_group_description.StepGroupDescription"
    ]
    """<p>The description of the step group.</p>"""
    next: NotRequired["aws_sdk_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The next step group.</p>"""
    previous: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
    ]
    """<p>The previous step group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkflowStepGroupRequest) -> dict:
    out: dict = {}
    out["workflowId"] = value["workflow_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "next" in value:
        import aws_sdk_migrationhuborchestrator.types.string_list

        out["next"] = aws_sdk_migrationhuborchestrator.types.string_list.serialize_json(
            value["next"]
        )
    if "previous" in value:
        import aws_sdk_migrationhuborchestrator.types.string_list

        out["previous"] = (
            aws_sdk_migrationhuborchestrator.types.string_list.serialize_json(
                value["previous"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateWorkflowStepGroupRequest:
    out: CreateWorkflowStepGroupRequest = {}  # type: ignore[typeddict-item]
    if "workflowId" in data:
        out["workflow_id"] = data["workflowId"]
    else:
        raise DeserializationError(
            "CreateWorkflowStepGroupRequest.workflow_id required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateWorkflowStepGroupRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "next" in data:
        import aws_sdk_migrationhuborchestrator.types.string_list

        out["next"] = (
            aws_sdk_migrationhuborchestrator.types.string_list.deserialize_json(
                data["next"]
            )
        )
    if "previous" in data:
        import aws_sdk_migrationhuborchestrator.types.string_list

        out["previous"] = (
            aws_sdk_migrationhuborchestrator.types.string_list.deserialize_json(
                data["previous"]
            )
        )
    return out
