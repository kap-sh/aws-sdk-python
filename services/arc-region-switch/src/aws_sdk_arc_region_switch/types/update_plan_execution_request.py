"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#UpdatePlanExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.execution_comment
    import aws_sdk_arc_region_switch.types.execution_id
    import aws_sdk_arc_region_switch.types.plan_arn
    import aws_sdk_arc_region_switch.types.update_plan_execution_action


class UpdatePlanExecutionRequest(TypedDict, closed=True):
    plan_arn: "aws_sdk_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the plan with the execution to update.</p>"""
    execution_id: "aws_sdk_arc_region_switch.types.execution_id.ExecutionId"
    """<p>The execution identifier of a plan execution.</p>"""
    action: "aws_sdk_arc_region_switch.types.update_plan_execution_action.UpdatePlanExecutionAction"
    """<p>The action specified for a plan execution, for example, Switch to Graceful or Pause.</p>"""
    comment: NotRequired[
        "aws_sdk_arc_region_switch.types.execution_comment.ExecutionComment"
    ]
    """<p>An optional comment about the plan execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdatePlanExecutionRequest) -> dict:
    out: dict = {}
    out["planArn"] = value["plan_arn"]
    out["executionId"] = value["execution_id"]
    import aws_sdk_arc_region_switch.types.update_plan_execution_action

    out["action"] = (
        aws_sdk_arc_region_switch.types.update_plan_execution_action.serialize_aws_json_1_0(
            value["action"]
        )
    )
    if "comment" in value:
        out["comment"] = value["comment"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdatePlanExecutionRequest:
    out: UpdatePlanExecutionRequest = {}  # type: ignore[typeddict-item]
    if "planArn" in data:
        out["plan_arn"] = data["planArn"]
    else:
        raise DeserializationError("UpdatePlanExecutionRequest.plan_arn required")
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    else:
        raise DeserializationError("UpdatePlanExecutionRequest.execution_id required")
    if "action" in data:
        import aws_sdk_arc_region_switch.types.update_plan_execution_action

        out["action"] = (
            aws_sdk_arc_region_switch.types.update_plan_execution_action.deserialize_aws_json_1_0(
                data["action"]
            )
        )
    else:
        raise DeserializationError("UpdatePlanExecutionRequest.action required")
    if "comment" in data:
        out["comment"] = data["comment"]
    return out
