"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdateScheduledActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.action_type
    import aws_sdk_opensearch.types.domain_name
    import aws_sdk_opensearch.types.long
    import aws_sdk_opensearch.types.schedule_at
    import aws_sdk_opensearch.types.string


class UpdateScheduledActionRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_opensearch.types.domain_name.DomainName"
    """<p>The name of the domain to reschedule an action for.</p>"""
    action_id: "aws_sdk_opensearch.types.string.String"
    r"""<p>The unique identifier of the action to reschedule. To retrieve this ID, send a <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListScheduledActions.html\">ListScheduledActions</a> request.</p>"""
    action_type: "aws_sdk_opensearch.types.action_type.ActionType"
    r"""<p>The type of action to reschedule. Can be one of <code>SERVICE_SOFTWARE_UPDATE</code>, <code>JVM_HEAP_SIZE_TUNING</code>, or <code>JVM_YOUNG_GEN_TUNING</code>. To retrieve this value, send a <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListScheduledActions.html\">ListScheduledActions</a> request.</p>"""
    schedule_at: "aws_sdk_opensearch.types.schedule_at.ScheduleAt"
    """<p>When to schedule the action.</p> <ul> <li> <p> <code>NOW</code> - Immediately schedules the update to happen in the current hour if there's capacity available.</p> </li> <li> <p> <code>TIMESTAMP</code> - Lets you specify a custom date and time to apply the update. If you specify this value, you must also provide a value for <code>DesiredStartTime</code>.</p> </li> <li> <p> <code>OFF_PEAK_WINDOW</code> - Marks the action to be picked up during an upcoming off-peak window. There's no guarantee that the change will be implemented during the next immediate window. Depending on capacity, it might happen in subsequent days.</p> </li> </ul>"""
    desired_start_time: NotRequired["aws_sdk_opensearch.types.long.Long"]
    """<p>The time to implement the change, in Coordinated Universal Time (UTC). Only specify this parameter if you set <code>ScheduleAt</code> to <code>TIMESTAMP</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateScheduledActionRequest) -> dict:
    out: dict = {}
    out["ActionID"] = value["action_id"]
    import aws_sdk_opensearch.types.action_type

    out["ActionType"] = aws_sdk_opensearch.types.action_type.serialize_json(
        value["action_type"]
    )
    import aws_sdk_opensearch.types.schedule_at

    out["ScheduleAt"] = aws_sdk_opensearch.types.schedule_at.serialize_json(
        value["schedule_at"]
    )
    if "desired_start_time" in value:
        out["DesiredStartTime"] = value["desired_start_time"]
    return out


def deserialize_json(data: dict) -> UpdateScheduledActionRequest:
    out: UpdateScheduledActionRequest = {}  # type: ignore[typeddict-item]
    if "ActionID" in data:
        out["action_id"] = data["ActionID"]
    else:
        raise DeserializationError("UpdateScheduledActionRequest.action_id required")
    if "ActionType" in data:
        import aws_sdk_opensearch.types.action_type

        out["action_type"] = aws_sdk_opensearch.types.action_type.deserialize_json(
            data["ActionType"]
        )
    else:
        raise DeserializationError("UpdateScheduledActionRequest.action_type required")
    if "ScheduleAt" in data:
        import aws_sdk_opensearch.types.schedule_at

        out["schedule_at"] = aws_sdk_opensearch.types.schedule_at.deserialize_json(
            data["ScheduleAt"]
        )
    else:
        raise DeserializationError("UpdateScheduledActionRequest.schedule_at required")
    if "DesiredStartTime" in data:
        out["desired_start_time"] = data["DesiredStartTime"]
    return out
