"""Generated from Smithy shape ``com.amazonaws.iot#ListDetectMitigationActionsExecutionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.device_defender_thing_name
    import aws_sdk_iot.types.max_results
    import aws_sdk_iot.types.mitigation_actions_task_id
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.timestamp
    import aws_sdk_iot.types.violation_id


class ListDetectMitigationActionsExecutionsRequest(TypedDict):
    task_id: NotRequired[
        "aws_sdk_iot.types.mitigation_actions_task_id.MitigationActionsTaskId"
    ]
    """<p> The unique identifier of the task. </p>"""
    violation_id: NotRequired["aws_sdk_iot.types.violation_id.ViolationId"]
    """<p> The unique identifier of the violation. </p>"""
    thing_name: NotRequired[
        "aws_sdk_iot.types.device_defender_thing_name.DeviceDefenderThingName"
    ]
    """<p> The name of the thing whose mitigation actions are listed. </p>"""
    start_time: NotRequired["aws_sdk_iot.types.timestamp.Timestamp"]
    """<p> A filter to limit results to those found after the specified time. You must specify either the startTime and endTime or the taskId, but not both. </p>"""
    end_time: NotRequired["aws_sdk_iot.types.timestamp.Timestamp"]
    """<p> The end of the time period for which ML Detect mitigation actions executions are returned. </p>"""
    max_results: NotRequired["aws_sdk_iot.types.max_results.MaxResults"]
    """<p> The maximum number of results to return at one time. The default is 25. </p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p> The token for the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDetectMitigationActionsExecutionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDetectMitigationActionsExecutionsRequest:
    out: ListDetectMitigationActionsExecutionsRequest = {}  # type: ignore[typeddict-item]
    return out
