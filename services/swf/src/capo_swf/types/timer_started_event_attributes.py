"""Generated from Smithy shape ``com.amazonaws.swf#TimerStartedEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.data
    import capo_swf.types.duration_in_seconds
    import capo_swf.types.event_id
    import capo_swf.types.timer_id


class TimerStartedEventAttributes(TypedDict, closed=True):
    timer_id: "capo_swf.types.timer_id.TimerId"
    """<p>The unique ID of the timer that was started.</p>"""
    control: NotRequired["capo_swf.types.data.Data"]
    """<p>Data attached to the event that can be used by the decider in subsequent workflow tasks.</p>"""
    start_to_fire_timeout: "capo_swf.types.duration_in_seconds.DurationInSeconds"
    """<p>The duration of time after which the timer fires.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>.</p>"""
    decision_task_completed_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>DecisionTaskCompleted</code> event corresponding to the decision task that resulted in the <code>StartTimer</code> decision for this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimerStartedEventAttributes) -> dict:
    out: dict = {}
    out["timerId"] = value["timer_id"]
    if "control" in value:
        out["control"] = value["control"]
    out["startToFireTimeout"] = value["start_to_fire_timeout"]
    out["decisionTaskCompletedEventId"] = value.get(
        "decision_task_completed_event_id", 0
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TimerStartedEventAttributes:
    out: TimerStartedEventAttributes = {}  # type: ignore[typeddict-item]
    if "timerId" in data:
        out["timer_id"] = data["timerId"]
    else:
        raise DeserializationError("TimerStartedEventAttributes.timer_id required")
    if "control" in data:
        out["control"] = data["control"]
    if "startToFireTimeout" in data:
        out["start_to_fire_timeout"] = data["startToFireTimeout"]
    else:
        raise DeserializationError(
            "TimerStartedEventAttributes.start_to_fire_timeout required"
        )
    if "decisionTaskCompletedEventId" in data:
        out["decision_task_completed_event_id"] = data["decisionTaskCompletedEventId"]
    else:
        out["decision_task_completed_event_id"] = 0
    return out
