"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#CancelPlanExecutionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.execution_comment
    import aws_sdk_arc_region_switch.types.execution_id
    import aws_sdk_arc_region_switch.types.plan_arn


class CancelPlanExecutionRequest(TypedDict):
    plan_arn: "aws_sdk_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the plan.</p>"""
    execution_id: "aws_sdk_arc_region_switch.types.execution_id.ExecutionId"
    """<p>The execution identifier of a plan execution.</p>"""
    comment: NotRequired[
        "aws_sdk_arc_region_switch.types.execution_comment.ExecutionComment"
    ]
    """<p>A comment that you can enter about canceling a plan execution step.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelPlanExecutionRequest) -> dict:
    out: dict = {}
    out["planArn"] = value["plan_arn"]
    out["executionId"] = value["execution_id"]
    if "comment" in value:
        out["comment"] = value["comment"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelPlanExecutionRequest:
    out: CancelPlanExecutionRequest = {}  # type: ignore[typeddict-item]
    if "planArn" in data:
        out["plan_arn"] = data["planArn"]
    else:
        raise DeserializationError("CancelPlanExecutionRequest.plan_arn required")
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    else:
        raise DeserializationError("CancelPlanExecutionRequest.execution_id required")
    if "comment" in data:
        out["comment"] = data["comment"]
    return out
