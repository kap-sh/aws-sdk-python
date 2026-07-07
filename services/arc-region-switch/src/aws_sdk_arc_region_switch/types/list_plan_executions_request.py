"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ListPlanExecutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.execution_state
    import aws_sdk_arc_region_switch.types.list_executions_max_results
    import aws_sdk_arc_region_switch.types.plan_arn


class ListPlanExecutionsRequest(TypedDict, closed=True):
    plan_arn: "aws_sdk_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The ARN for the plan.</p>"""
    max_results: "aws_sdk_arc_region_switch.types.list_executions_max_results.ListExecutionsMaxResults"
    """<p>The number of objects that you want to return with this call.</p>"""
    next_token: NotRequired["str"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>"""
    state: NotRequired["aws_sdk_arc_region_switch.types.execution_state.ExecutionState"]
    """<p>The state of the plan execution. For example, the plan execution might be In Progress.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListPlanExecutionsRequest) -> dict:
    out: dict = {}
    out["planArn"] = value["plan_arn"]
    out["maxResults"] = value.get("max_results", 100)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "state" in value:
        import aws_sdk_arc_region_switch.types.execution_state

        out["state"] = (
            aws_sdk_arc_region_switch.types.execution_state.serialize_aws_json_1_0(
                value["state"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListPlanExecutionsRequest:
    out: ListPlanExecutionsRequest = {}  # type: ignore[typeddict-item]
    if "planArn" in data:
        out["plan_arn"] = data["planArn"]
    else:
        raise DeserializationError("ListPlanExecutionsRequest.plan_arn required")
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 100
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "state" in data:
        import aws_sdk_arc_region_switch.types.execution_state

        out["state"] = (
            aws_sdk_arc_region_switch.types.execution_state.deserialize_aws_json_1_0(
                data["state"]
            )
        )
    return out
