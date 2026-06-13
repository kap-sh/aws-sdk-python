"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#UpdateWorkflowStepRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_migrationhuborchestrator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_id
    import aws_sdk_migrationhuborchestrator.types.step_action_type
    import aws_sdk_migrationhuborchestrator.types.step_description
    import aws_sdk_migrationhuborchestrator.types.step_group_id
    import aws_sdk_migrationhuborchestrator.types.step_id
    import aws_sdk_migrationhuborchestrator.types.step_name
    import aws_sdk_migrationhuborchestrator.types.step_status
    import aws_sdk_migrationhuborchestrator.types.string_list
    import aws_sdk_migrationhuborchestrator.types.workflow_step_automation_configuration
    import aws_sdk_migrationhuborchestrator.types.workflow_step_output_list


class UpdateWorkflowStepRequest(TypedDict):
    id: "aws_sdk_migrationhuborchestrator.types.step_id.StepId"
    """<p>The ID of the step.</p>"""
    step_group_id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId"
    """<p>The ID of the step group.</p>"""
    workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    """<p>The ID of the migration workflow.</p>"""
    name: NotRequired["aws_sdk_migrationhuborchestrator.types.step_name.StepName"]
    """<p>The name of the step.</p>"""
    description: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.step_description.StepDescription"
    ]
    """<p>The description of the step.</p>"""
    step_action_type: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.step_action_type.StepActionType"
    ]
    """<p>The action type of the step. You must run and update the status of a manual step for the workflow to continue after the completion of the step.</p>"""
    workflow_step_automation_configuration: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.workflow_step_automation_configuration.WorkflowStepAutomationConfiguration"
    ]
    """<p>The custom script to run tests on the source and target environments.</p>"""
    step_target: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
    ]
    """<p>The servers on which a step will be run.</p>"""
    outputs: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.workflow_step_output_list.WorkflowStepOutputList"
    ]
    """<p>The outputs of a step.</p>"""
    previous: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
    ]
    """<p>The previous step.</p>"""
    next: NotRequired["aws_sdk_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The next step.</p>"""
    status: NotRequired["aws_sdk_migrationhuborchestrator.types.step_status.StepStatus"]
    """<p>The status of the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkflowStepRequest) -> dict:
    out: dict = {}
    out["stepGroupId"] = value["step_group_id"]
    out["workflowId"] = value["workflow_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "step_action_type" in value:
        out["stepActionType"] = value["step_action_type"]
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
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> UpdateWorkflowStepRequest:
    out: UpdateWorkflowStepRequest = {}  # type: ignore[typeddict-item]
    if "stepGroupId" in data:
        out["step_group_id"] = data["stepGroupId"]
    else:
        raise DeserializationError("UpdateWorkflowStepRequest.step_group_id required")
    if "workflowId" in data:
        out["workflow_id"] = data["workflowId"]
    else:
        raise DeserializationError("UpdateWorkflowStepRequest.workflow_id required")
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "stepActionType" in data:
        out["step_action_type"] = data["stepActionType"]
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
    if "status" in data:
        out["status"] = data["status"]
    return out
