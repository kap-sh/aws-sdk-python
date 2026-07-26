"""Generated from Smithy shape ``com.amazonaws.appflow#DescribeFlowExecutionRecordsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.flow_execution_list
    import capo_appflow.types.next_token


class DescribeFlowExecutionRecordsResponse(TypedDict, closed=True):
    flow_executions: NotRequired[
        "capo_appflow.types.flow_execution_list.FlowExecutionList"
    ]
    """<p> Returns a list of all instances when this flow was run. </p>"""
    next_token: NotRequired["capo_appflow.types.next_token.NextToken"]
    """<p> The pagination token for the next page of data. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFlowExecutionRecordsResponse) -> dict:
    out: dict = {}
    if "flow_executions" in value:
        import capo_appflow.types.flow_execution_list

        out["flowExecutions"] = capo_appflow.types.flow_execution_list.serialize_json(
            value["flow_executions"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeFlowExecutionRecordsResponse:
    out: DescribeFlowExecutionRecordsResponse = {}  # type: ignore[typeddict-item]
    if "flowExecutions" in data:
        import capo_appflow.types.flow_execution_list

        out["flow_executions"] = (
            capo_appflow.types.flow_execution_list.deserialize_json(
                data["flowExecutions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
