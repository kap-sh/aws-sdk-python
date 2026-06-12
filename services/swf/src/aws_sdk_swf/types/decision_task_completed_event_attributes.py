"""Generated from Smithy shape ``com.amazonaws.swf#DecisionTaskCompletedEventAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_swf.types.data
    import aws_sdk_swf.types.duration_in_seconds_optional
    import aws_sdk_swf.types.event_id
    import aws_sdk_swf.types.task_list


class DecisionTaskCompletedEventAttributes(TypedDict):
    execution_context: NotRequired["aws_sdk_swf.types.data.Data"]
    """<p>User defined context for the workflow execution.</p>"""
    scheduled_event_id: "aws_sdk_swf.types.event_id.EventId"
    """<p>The ID of the <code>DecisionTaskScheduled</code> event that was recorded when this decision task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""
    started_event_id: "aws_sdk_swf.types.event_id.EventId"
    """<p>The ID of the <code>DecisionTaskStarted</code> event recorded when this decision task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""
    task_list: NotRequired["aws_sdk_swf.types.task_list.TaskList"]
    task_list_schedule_to_start_timeout: NotRequired[
        "aws_sdk_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>The maximum amount of time the decision task can wait to be assigned to a worker.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DecisionTaskCompletedEventAttributes) -> dict:
    out: dict = {}
    if "execution_context" in value:
        out["executionContext"] = value["execution_context"]
    out["scheduledEventId"] = value.get("scheduled_event_id", 0)
    out["startedEventId"] = value.get("started_event_id", 0)
    if "task_list" in value:
        import aws_sdk_swf.types.task_list

        out["taskList"] = aws_sdk_swf.types.task_list.serialize_aws_json_1_0(
            value["task_list"]
        )
    if "task_list_schedule_to_start_timeout" in value:
        out["taskListScheduleToStartTimeout"] = value[
            "task_list_schedule_to_start_timeout"
        ]
    return out


def deserialize_aws_json_1_0(data: dict) -> DecisionTaskCompletedEventAttributes:
    out: DecisionTaskCompletedEventAttributes = {}  # type: ignore[typeddict-item]
    if "executionContext" in data:
        out["execution_context"] = data["executionContext"]
    if "scheduledEventId" in data:
        out["scheduled_event_id"] = data["scheduledEventId"]
    else:
        out["scheduled_event_id"] = 0
    if "startedEventId" in data:
        out["started_event_id"] = data["startedEventId"]
    else:
        out["started_event_id"] = 0
    if "taskList" in data:
        import aws_sdk_swf.types.task_list

        out["task_list"] = aws_sdk_swf.types.task_list.deserialize_aws_json_1_0(
            data["taskList"]
        )
    if "taskListScheduleToStartTimeout" in data:
        out["task_list_schedule_to_start_timeout"] = data[
            "taskListScheduleToStartTimeout"
        ]
    return out
