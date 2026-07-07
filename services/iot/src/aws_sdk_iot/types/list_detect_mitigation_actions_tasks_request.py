"""Generated from Smithy shape ``com.amazonaws.iot#ListDetectMitigationActionsTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.max_results
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.timestamp


class ListDetectMitigationActionsTasksRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_iot.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at one time. The default is 25.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p> The token for the next set of results. </p>"""
    start_time: "aws_sdk_iot.types.timestamp.Timestamp"
    """<p> A filter to limit results to those found after the specified time. You must specify either the startTime and endTime or the taskId, but not both. </p>"""
    end_time: "aws_sdk_iot.types.timestamp.Timestamp"
    """<p> The end of the time period for which ML Detect mitigation actions tasks are returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDetectMitigationActionsTasksRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDetectMitigationActionsTasksRequest:
    out: ListDetectMitigationActionsTasksRequest = {}  # type: ignore[typeddict-item]
    return out
