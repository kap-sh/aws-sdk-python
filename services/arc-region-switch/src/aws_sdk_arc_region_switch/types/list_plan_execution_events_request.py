"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ListPlanExecutionEventsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.execution_id
    import aws_sdk_arc_region_switch.types.list_execution_events_max_results
    import aws_sdk_arc_region_switch.types.plan_arn
    import aws_sdk_arc_region_switch.types.step_name


class ListPlanExecutionEventsRequest(TypedDict):
    plan_arn: "aws_sdk_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the plan.</p>"""
    execution_id: "aws_sdk_arc_region_switch.types.execution_id.ExecutionId"
    """<p>The execution identifier of a plan execution.</p>"""
    max_results: "aws_sdk_arc_region_switch.types.list_execution_events_max_results.ListExecutionEventsMaxResults"
    """<p>The number of objects that you want to return with this call.</p>"""
    next_token: NotRequired["str"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>"""
    name: NotRequired["aws_sdk_arc_region_switch.types.step_name.StepName"]
    """<p>The name of the plan execution event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListPlanExecutionEventsRequest) -> dict:
    out: dict = {}
    out["planArn"] = value["plan_arn"]
    out["executionId"] = value["execution_id"]
    out["maxResults"] = value.get("max_results", 100)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListPlanExecutionEventsRequest:
    out: ListPlanExecutionEventsRequest = {}  # type: ignore[typeddict-item]
    if "planArn" in data:
        out["plan_arn"] = data["planArn"]
    else:
        raise DeserializationError("ListPlanExecutionEventsRequest.plan_arn required")
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    else:
        raise DeserializationError(
            "ListPlanExecutionEventsRequest.execution_id required"
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 100
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "name" in data:
        out["name"] = data["name"]
    return out
