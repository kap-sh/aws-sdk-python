"""Generated from Smithy shape ``com.amazonaws.quicksight#ListFlowsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.flow_summary_list
    import capo_quicksight.types.status_code


class ListFlowsOutput(TypedDict, closed=True):
    flow_summary_list: NotRequired[
        "capo_quicksight.types.flow_summary_list.FlowSummaryList"
    ]
    """<p>A structure that contains all of the flows in your Amazon Web Services account. This structure provides basic information about the flows.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFlowsOutput) -> dict:
    out: dict = {}
    if "flow_summary_list" in value:
        import capo_quicksight.types.flow_summary_list

        out["FlowSummaryList"] = capo_quicksight.types.flow_summary_list.serialize_json(
            value["flow_summary_list"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListFlowsOutput:
    out: ListFlowsOutput = {}  # type: ignore[typeddict-item]
    if "FlowSummaryList" in data:
        import capo_quicksight.types.flow_summary_list

        out["flow_summary_list"] = (
            capo_quicksight.types.flow_summary_list.deserialize_json(
                data["FlowSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
