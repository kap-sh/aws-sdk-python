"""Generated from Smithy shape ``com.amazonaws.iot#ListDetectMitigationActionsExecutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.device_defender_thing_name
    import capo_iot.types.max_results
    import capo_iot.types.mitigation_actions_task_id
    import capo_iot.types.next_token
    import capo_iot.types.timestamp
    import capo_iot.types.violation_id


class ListDetectMitigationActionsExecutionsRequest(TypedDict, closed=True):
    task_id: NotRequired[
        "capo_iot.types.mitigation_actions_task_id.MitigationActionsTaskId"
    ]
    """<p> The unique identifier of the task. </p>"""
    violation_id: NotRequired["capo_iot.types.violation_id.ViolationId"]
    """<p> The unique identifier of the violation. </p>"""
    thing_name: NotRequired[
        "capo_iot.types.device_defender_thing_name.DeviceDefenderThingName"
    ]
    """<p> The name of the thing whose mitigation actions are listed. </p>"""
    start_time: NotRequired["capo_iot.types.timestamp.Timestamp"]
    """<p> A filter to limit results to those found after the specified time. You must specify either the startTime and endTime or the taskId, but not both. </p>"""
    end_time: NotRequired["capo_iot.types.timestamp.Timestamp"]
    """<p> The end of the time period for which ML Detect mitigation actions executions are returned. </p>"""
    max_results: NotRequired["capo_iot.types.max_results.MaxResults"]
    """<p> The maximum number of results to return at one time. The default is 25. </p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p> The token for the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDetectMitigationActionsExecutionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDetectMitigationActionsExecutionsRequest:
    out: ListDetectMitigationActionsExecutionsRequest = {}  # type: ignore[typeddict-item]
    return out
