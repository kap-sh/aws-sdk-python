"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#UpdateWorkflowStepGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_id
    import aws_sdk_migrationhuborchestrator.types.step_group_description
    import aws_sdk_migrationhuborchestrator.types.step_group_id
    import aws_sdk_migrationhuborchestrator.types.step_group_name
    import aws_sdk_migrationhuborchestrator.types.string_list


class UpdateWorkflowStepGroupRequest(TypedDict):
    workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    """<p>The ID of the migration workflow.</p>"""
    id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId"
    """<p>The ID of the step group.</p>"""
    name: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.step_group_name.StepGroupName"
    ]
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
def serialize_json(value: UpdateWorkflowStepGroupRequest) -> dict:
    out: dict = {}
    if "name" in value:
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


def deserialize_json(data: dict) -> UpdateWorkflowStepGroupRequest:
    out: UpdateWorkflowStepGroupRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
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
