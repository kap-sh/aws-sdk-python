"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchFlowsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.flow_summary_list
    import aws_sdk_quicksight.types.status_code


class SearchFlowsOutput(TypedDict, closed=True):
    flow_summary_list: "aws_sdk_quicksight.types.flow_summary_list.FlowSummaryList"
    """<p>The list of flows found against the search.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchFlowsOutput) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.flow_summary_list

    out["FlowSummaryList"] = aws_sdk_quicksight.types.flow_summary_list.serialize_json(
        value["flow_summary_list"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> SearchFlowsOutput:
    out: SearchFlowsOutput = {}  # type: ignore[typeddict-item]
    if "FlowSummaryList" in data:
        import aws_sdk_quicksight.types.flow_summary_list

        out["flow_summary_list"] = (
            aws_sdk_quicksight.types.flow_summary_list.deserialize_json(
                data["FlowSummaryList"]
            )
        )
    else:
        raise DeserializationError("SearchFlowsOutput.flow_summary_list required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
