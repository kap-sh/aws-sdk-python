"""Generated from Smithy shape ``com.amazonaws.swf#DecisionTaskTimedOutEventAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.decision_task_timeout_type
    import aws_sdk_swf.types.event_id


class DecisionTaskTimedOutEventAttributes(TypedDict):
    timeout_type: "aws_sdk_swf.types.decision_task_timeout_type.DecisionTaskTimeoutType"
    """<p>The type of timeout that expired before the decision task could be completed.</p>"""
    scheduled_event_id: "aws_sdk_swf.types.event_id.EventId"
    """<p>The ID of the <code>DecisionTaskScheduled</code> event that was recorded when this decision task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""
    started_event_id: "aws_sdk_swf.types.event_id.EventId"
    """<p>The ID of the <code>DecisionTaskStarted</code> event recorded when this decision task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DecisionTaskTimedOutEventAttributes) -> dict:
    out: dict = {}
    import aws_sdk_swf.types.decision_task_timeout_type

    out["timeoutType"] = (
        aws_sdk_swf.types.decision_task_timeout_type.serialize_aws_json_1_0(
            value["timeout_type"]
        )
    )
    out["scheduledEventId"] = value.get("scheduled_event_id", 0)
    out["startedEventId"] = value.get("started_event_id", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> DecisionTaskTimedOutEventAttributes:
    out: DecisionTaskTimedOutEventAttributes = {}  # type: ignore[typeddict-item]
    if "timeoutType" in data:
        import aws_sdk_swf.types.decision_task_timeout_type

        out["timeout_type"] = (
            aws_sdk_swf.types.decision_task_timeout_type.deserialize_aws_json_1_0(
                data["timeoutType"]
            )
        )
    else:
        raise DeserializationError(
            "DecisionTaskTimedOutEventAttributes.timeout_type required"
        )
    if "scheduledEventId" in data:
        out["scheduled_event_id"] = data["scheduledEventId"]
    else:
        out["scheduled_event_id"] = 0
    if "startedEventId" in data:
        out["started_event_id"] = data["startedEventId"]
    else:
        out["started_event_id"] = 0
    return out
