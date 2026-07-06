"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#UpdatePlanExecutionStepRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.execution_comment
    import aws_sdk_arc_region_switch.types.execution_id
    import aws_sdk_arc_region_switch.types.plan_arn
    import aws_sdk_arc_region_switch.types.update_plan_execution_step_action


class UpdatePlanExecutionStepRequest(TypedDict, closed=True):
    plan_arn: "aws_sdk_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the plan containing the execution step to update.</p>"""
    execution_id: "aws_sdk_arc_region_switch.types.execution_id.ExecutionId"
    """<p>The unique identifier of the plan execution containing the step to update.</p>"""
    comment: "aws_sdk_arc_region_switch.types.execution_comment.ExecutionComment"
    """<p>An optional comment about the plan execution.</p>"""
    step_name: "str"
    """<p>The name of the execution step to update.</p>"""
    action_to_take: "aws_sdk_arc_region_switch.types.update_plan_execution_step_action.UpdatePlanExecutionStepAction"
    """<p>The updated action to take for the step. This can be used to skip or retry a step.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdatePlanExecutionStepRequest) -> dict:
    out: dict = {}
    out["planArn"] = value["plan_arn"]
    out["executionId"] = value["execution_id"]
    out["comment"] = value["comment"]
    out["stepName"] = value["step_name"]
    import aws_sdk_arc_region_switch.types.update_plan_execution_step_action

    out["actionToTake"] = (
        aws_sdk_arc_region_switch.types.update_plan_execution_step_action.serialize_aws_json_1_0(
            value["action_to_take"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdatePlanExecutionStepRequest:
    out: UpdatePlanExecutionStepRequest = {}  # type: ignore[typeddict-item]
    if "planArn" in data:
        out["plan_arn"] = data["planArn"]
    else:
        raise DeserializationError("UpdatePlanExecutionStepRequest.plan_arn required")
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    else:
        raise DeserializationError(
            "UpdatePlanExecutionStepRequest.execution_id required"
        )
    if "comment" in data:
        out["comment"] = data["comment"]
    else:
        raise DeserializationError("UpdatePlanExecutionStepRequest.comment required")
    if "stepName" in data:
        out["step_name"] = data["stepName"]
    else:
        raise DeserializationError("UpdatePlanExecutionStepRequest.step_name required")
    if "actionToTake" in data:
        import aws_sdk_arc_region_switch.types.update_plan_execution_step_action

        out["action_to_take"] = (
            aws_sdk_arc_region_switch.types.update_plan_execution_step_action.deserialize_aws_json_1_0(
                data["actionToTake"]
            )
        )
    else:
        raise DeserializationError(
            "UpdatePlanExecutionStepRequest.action_to_take required"
        )
    return out
