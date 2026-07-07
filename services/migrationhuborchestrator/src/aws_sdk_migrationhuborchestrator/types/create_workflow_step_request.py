"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#CreateWorkflowStepRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_migrationhuborchestrator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_description
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_id
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_name
    import aws_sdk_migrationhuborchestrator.types.step_action_type
    import aws_sdk_migrationhuborchestrator.types.step_group_id
    import aws_sdk_migrationhuborchestrator.types.string_list
    import aws_sdk_migrationhuborchestrator.types.workflow_step_automation_configuration
    import aws_sdk_migrationhuborchestrator.types.workflow_step_output_list


class CreateWorkflowStepRequest(TypedDict, closed=True):
    name: "aws_sdk_migrationhuborchestrator.types.migration_workflow_name.MigrationWorkflowName"
    """<p>The name of the step.</p>"""
    step_group_id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId"
    """<p>The ID of the step group.</p>"""
    workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    """<p>The ID of the migration workflow.</p>"""
    step_action_type: (
        "aws_sdk_migrationhuborchestrator.types.step_action_type.StepActionType"
    )
    """<p>The action type of the step. You must run and update the status of a manual step for the workflow to continue after the completion of the step.</p>"""
    description: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.migration_workflow_description.MigrationWorkflowDescription"
    ]
    """<p>The description of the step.</p>"""
    workflow_step_automation_configuration: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.workflow_step_automation_configuration.WorkflowStepAutomationConfiguration"
    ]
    """<p>The custom script to run tests on source or target environments.</p>"""
    step_target: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
    ]
    """<p>The servers on which a step will be run.</p>"""
    outputs: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.workflow_step_output_list.WorkflowStepOutputList"
    ]
    """<p>The key value pairs added for the expected output.</p>"""
    previous: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
    ]
    """<p>The previous step.</p>"""
    next: NotRequired["aws_sdk_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The next step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkflowStepRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["stepGroupId"] = value["step_group_id"]
    out["workflowId"] = value["workflow_id"]
    out["stepActionType"] = value["step_action_type"]
    if "description" in value:
        out["description"] = value["description"]
    if "workflow_step_automation_configuration" in value:
        import aws_sdk_migrationhuborchestrator.types.workflow_step_automation_configuration

        out["workflowStepAutomationConfiguration"] = (
            aws_sdk_migrationhuborchestrator.types.workflow_step_automation_configuration.serialize_json(
                value["workflow_step_automation_configuration"]
            )
        )
    if "step_target" in value:
        import aws_sdk_migrationhuborchestrator.types.string_list

        out["stepTarget"] = (
            aws_sdk_migrationhuborchestrator.types.string_list.serialize_json(
                value["step_target"]
            )
        )
    if "outputs" in value:
        import aws_sdk_migrationhuborchestrator.types.workflow_step_output_list

        out["outputs"] = (
            aws_sdk_migrationhuborchestrator.types.workflow_step_output_list.serialize_json(
                value["outputs"]
            )
        )
    if "previous" in value:
        import aws_sdk_migrationhuborchestrator.types.string_list

        out["previous"] = (
            aws_sdk_migrationhuborchestrator.types.string_list.serialize_json(
                value["previous"]
            )
        )
    if "next" in value:
        import aws_sdk_migrationhuborchestrator.types.string_list

        out["next"] = aws_sdk_migrationhuborchestrator.types.string_list.serialize_json(
            value["next"]
        )
    return out


def deserialize_json(data: dict) -> CreateWorkflowStepRequest:
    out: CreateWorkflowStepRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateWorkflowStepRequest.name required")
    if "stepGroupId" in data:
        out["step_group_id"] = data["stepGroupId"]
    else:
        raise DeserializationError("CreateWorkflowStepRequest.step_group_id required")
    if "workflowId" in data:
        out["workflow_id"] = data["workflowId"]
    else:
        raise DeserializationError("CreateWorkflowStepRequest.workflow_id required")
    if "stepActionType" in data:
        out["step_action_type"] = data["stepActionType"]
    else:
        raise DeserializationError(
            "CreateWorkflowStepRequest.step_action_type required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "workflowStepAutomationConfiguration" in data:
        import aws_sdk_migrationhuborchestrator.types.workflow_step_automation_configuration

        out["workflow_step_automation_configuration"] = (
            aws_sdk_migrationhuborchestrator.types.workflow_step_automation_configuration.deserialize_json(
                data["workflowStepAutomationConfiguration"]
            )
        )
    if "stepTarget" in data:
        import aws_sdk_migrationhuborchestrator.types.string_list

        out["step_target"] = (
            aws_sdk_migrationhuborchestrator.types.string_list.deserialize_json(
                data["stepTarget"]
            )
        )
    if "outputs" in data:
        import aws_sdk_migrationhuborchestrator.types.workflow_step_output_list

        out["outputs"] = (
            aws_sdk_migrationhuborchestrator.types.workflow_step_output_list.deserialize_json(
                data["outputs"]
            )
        )
    if "previous" in data:
        import aws_sdk_migrationhuborchestrator.types.string_list

        out["previous"] = (
            aws_sdk_migrationhuborchestrator.types.string_list.deserialize_json(
                data["previous"]
            )
        )
    if "next" in data:
        import aws_sdk_migrationhuborchestrator.types.string_list

        out["next"] = (
            aws_sdk_migrationhuborchestrator.types.string_list.deserialize_json(
                data["next"]
            )
        )
    return out
