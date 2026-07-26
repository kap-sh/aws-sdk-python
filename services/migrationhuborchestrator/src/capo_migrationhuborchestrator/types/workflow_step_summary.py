"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#WorkflowStepSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.owner
    import capo_migrationhuborchestrator.types.step_action_type
    import capo_migrationhuborchestrator.types.step_status
    import capo_migrationhuborchestrator.types.string_list


class WorkflowStepSummary(TypedDict, closed=True):
    step_id: NotRequired["str"]
    """<p>The ID of the step.</p>"""
    name: NotRequired["str"]
    """<p>The name of the step.</p>"""
    step_action_type: NotRequired[
        "capo_migrationhuborchestrator.types.step_action_type.StepActionType"
    ]
    """<p>The action type of the step. You must run and update the status of a manual step for the workflow to continue after the completion of the step.</p>"""
    owner: NotRequired["capo_migrationhuborchestrator.types.owner.Owner"]
    """<p>The owner of the step.</p>"""
    previous: NotRequired["capo_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The previous step.</p>"""
    next: NotRequired["capo_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The next step.</p>"""
    status: NotRequired["capo_migrationhuborchestrator.types.step_status.StepStatus"]
    """<p>The status of the step.</p>"""
    status_message: NotRequired["str"]
    """<p>The status message of the migration workflow.</p>"""
    no_of_srv_completed: NotRequired["int"]
    """<p>The number of servers that have been migrated.</p>"""
    no_of_srv_failed: NotRequired["int"]
    """<p>The number of servers that have failed to migrate.</p>"""
    total_no_of_srv: NotRequired["int"]
    """<p>The total number of servers that have been migrated.</p>"""
    description: NotRequired["str"]
    """<p>The description of the step.</p>"""
    script_location: NotRequired["str"]
    """<p>The location of the script.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowStepSummary) -> dict:
    out: dict = {}
    if "step_id" in value:
        out["stepId"] = value["step_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "step_action_type" in value:
        out["stepActionType"] = value["step_action_type"]
    if "owner" in value:
        out["owner"] = value["owner"]
    if "previous" in value:
        import capo_migrationhuborchestrator.types.string_list

        out["previous"] = (
            capo_migrationhuborchestrator.types.string_list.serialize_json(
                value["previous"]
            )
        )
    if "next" in value:
        import capo_migrationhuborchestrator.types.string_list

        out["next"] = capo_migrationhuborchestrator.types.string_list.serialize_json(
            value["next"]
        )
    if "status" in value:
        out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "no_of_srv_completed" in value:
        out["noOfSrvCompleted"] = value["no_of_srv_completed"]
    if "no_of_srv_failed" in value:
        out["noOfSrvFailed"] = value["no_of_srv_failed"]
    if "total_no_of_srv" in value:
        out["totalNoOfSrv"] = value["total_no_of_srv"]
    if "description" in value:
        out["description"] = value["description"]
    if "script_location" in value:
        out["scriptLocation"] = value["script_location"]
    return out


def deserialize_json(data: dict) -> WorkflowStepSummary:
    out: WorkflowStepSummary = {}  # type: ignore[typeddict-item]
    if "stepId" in data:
        out["step_id"] = data["stepId"]
    if "name" in data:
        out["name"] = data["name"]
    if "stepActionType" in data:
        out["step_action_type"] = data["stepActionType"]
    if "owner" in data:
        out["owner"] = data["owner"]
    if "previous" in data:
        import capo_migrationhuborchestrator.types.string_list

        out["previous"] = (
            capo_migrationhuborchestrator.types.string_list.deserialize_json(
                data["previous"]
            )
        )
    if "next" in data:
        import capo_migrationhuborchestrator.types.string_list

        out["next"] = capo_migrationhuborchestrator.types.string_list.deserialize_json(
            data["next"]
        )
    if "status" in data:
        out["status"] = data["status"]
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "noOfSrvCompleted" in data:
        out["no_of_srv_completed"] = data["noOfSrvCompleted"]
    if "noOfSrvFailed" in data:
        out["no_of_srv_failed"] = data["noOfSrvFailed"]
    if "totalNoOfSrv" in data:
        out["total_no_of_srv"] = data["totalNoOfSrv"]
    if "description" in data:
        out["description"] = data["description"]
    if "scriptLocation" in data:
        out["script_location"] = data["scriptLocation"]
    return out
