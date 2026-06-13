"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#GetWorkflowStepResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_migrationhuborchestrator.types.owner
    import aws_sdk_migrationhuborchestrator.types.step_action_type
    import aws_sdk_migrationhuborchestrator.types.step_status
    import aws_sdk_migrationhuborchestrator.types.string_list
    import aws_sdk_migrationhuborchestrator.types.workflow_step_automation_configuration
    import aws_sdk_migrationhuborchestrator.types.workflow_step_output_list


class GetWorkflowStepResponse(TypedDict):
    name: NotRequired["str"]
    """<p>The name of the step.</p>"""
    step_group_id: NotRequired["str"]
    """<p>The ID of the step group.</p>"""
    workflow_id: NotRequired["str"]
    """<p>The ID of the migration workflow.</p>"""
    step_id: NotRequired["str"]
    """<p>The ID of the step.</p>"""
    description: NotRequired["str"]
    """<p>The description of the step.</p>"""
    step_action_type: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.step_action_type.StepActionType"
    ]
    """<p>The action type of the step. You must run and update the status of a manual step for the workflow to continue after the completion of the step.</p>"""
    owner: NotRequired["aws_sdk_migrationhuborchestrator.types.owner.Owner"]
    """<p>The owner of the step.</p>"""
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
    """<p>The outputs of the step.</p>"""
    previous: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
    ]
    """<p>The previous step.</p>"""
    next: NotRequired["aws_sdk_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The next step.</p>"""
    status: NotRequired["aws_sdk_migrationhuborchestrator.types.step_status.StepStatus"]
    """<p>The status of the step.</p>"""
    status_message: NotRequired["str"]
    """<p>The status message of the migration workflow.</p>"""
    script_output_location: NotRequired["str"]
    """<p>The output location of the script.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>The time at which the step was created.</p>"""
    last_start_time: NotRequired["datetime.datetime"]
    """<p>The time at which the workflow was last started.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The time at which the step ended.</p>"""
    no_of_srv_completed: NotRequired["int"]
    """<p>The number of servers that have been migrated.</p>"""
    no_of_srv_failed: NotRequired["int"]
    """<p>The number of servers that have failed to migrate.</p>"""
    total_no_of_srv: NotRequired["int"]
    """<p>The total number of servers that have been migrated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowStepResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "step_group_id" in value:
        out["stepGroupId"] = value["step_group_id"]
    if "workflow_id" in value:
        out["workflowId"] = value["workflow_id"]
    if "step_id" in value:
        out["stepId"] = value["step_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "step_action_type" in value:
        out["stepActionType"] = value["step_action_type"]
    if "owner" in value:
        out["owner"] = value["owner"]
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
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "script_output_location" in value:
        out["scriptOutputLocation"] = value["script_output_location"]
    if "creation_time" in value:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["creationTime"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "last_start_time" in value:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["lastStartTime"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["last_start_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["endTime"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["end_time"]
            )
        )
    if "no_of_srv_completed" in value:
        out["noOfSrvCompleted"] = value["no_of_srv_completed"]
    if "no_of_srv_failed" in value:
        out["noOfSrvFailed"] = value["no_of_srv_failed"]
    if "total_no_of_srv" in value:
        out["totalNoOfSrv"] = value["total_no_of_srv"]
    return out


def deserialize_json(data: dict) -> GetWorkflowStepResponse:
    out: GetWorkflowStepResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "stepGroupId" in data:
        out["step_group_id"] = data["stepGroupId"]
    if "workflowId" in data:
        out["workflow_id"] = data["workflowId"]
    if "stepId" in data:
        out["step_id"] = data["stepId"]
    if "description" in data:
        out["description"] = data["description"]
    if "stepActionType" in data:
        out["step_action_type"] = data["stepActionType"]
    if "owner" in data:
        out["owner"] = data["owner"]
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
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "scriptOutputLocation" in data:
        out["script_output_location"] = data["scriptOutputLocation"]
    if "creationTime" in data:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["creation_time"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    if "lastStartTime" in data:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["last_start_time"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["lastStartTime"]
            )
        )
    if "endTime" in data:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    if "noOfSrvCompleted" in data:
        out["no_of_srv_completed"] = data["noOfSrvCompleted"]
    if "noOfSrvFailed" in data:
        out["no_of_srv_failed"] = data["noOfSrvFailed"]
    if "totalNoOfSrv" in data:
        out["total_no_of_srv"] = data["totalNoOfSrv"]
    return out
