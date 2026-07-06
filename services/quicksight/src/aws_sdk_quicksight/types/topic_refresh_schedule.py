"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicRefreshSchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean
    import aws_sdk_quicksight.types.limited_string
    import aws_sdk_quicksight.types.nullable_boolean
    import aws_sdk_quicksight.types.timestamp
    import aws_sdk_quicksight.types.topic_schedule_type


class TopicRefreshSchedule(TypedDict, closed=True):
    is_enabled: "aws_sdk_quicksight.types.nullable_boolean.NullableBoolean"
    """<p>A Boolean value that controls whether to schedule is enabled.</p>"""
    based_on_spice_schedule: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>A Boolean value that controls whether to schedule runs at the same schedule that is specified in SPICE dataset.</p>"""
    starting_at: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The starting date and time for the refresh schedule.</p>"""
    timezone: NotRequired["aws_sdk_quicksight.types.limited_string.LimitedString"]
    """<p>The timezone that you want the refresh schedule to use.</p>"""
    repeat_at: NotRequired["aws_sdk_quicksight.types.limited_string.LimitedString"]
    """<p>The time of day when the refresh should run, for example, Monday-Sunday.</p>"""
    topic_schedule_type: NotRequired[
        "aws_sdk_quicksight.types.topic_schedule_type.TopicScheduleType"
    ]
    """<p>The type of refresh schedule. Valid values for this structure are <code>HOURLY</code>, <code>DAILY</code>, <code>WEEKLY</code>, and <code>MONTHLY</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicRefreshSchedule) -> dict:
    out: dict = {}
    out["IsEnabled"] = value["is_enabled"]
    out["BasedOnSpiceSchedule"] = value.get("based_on_spice_schedule", False)
    if "starting_at" in value:
        import aws_sdk_quicksight.types.timestamp

        out["StartingAt"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["starting_at"]
        )
    if "timezone" in value:
        out["Timezone"] = value["timezone"]
    if "repeat_at" in value:
        out["RepeatAt"] = value["repeat_at"]
    if "topic_schedule_type" in value:
        import aws_sdk_quicksight.types.topic_schedule_type

        out["TopicScheduleType"] = (
            aws_sdk_quicksight.types.topic_schedule_type.serialize_json(
                value["topic_schedule_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> TopicRefreshSchedule:
    out: TopicRefreshSchedule = {}  # type: ignore[typeddict-item]
    if "IsEnabled" in data:
        out["is_enabled"] = data["IsEnabled"]
    else:
        raise DeserializationError("TopicRefreshSchedule.is_enabled required")
    if "BasedOnSpiceSchedule" in data:
        out["based_on_spice_schedule"] = data["BasedOnSpiceSchedule"]
    else:
        out["based_on_spice_schedule"] = False
    if "StartingAt" in data:
        import aws_sdk_quicksight.types.timestamp

        out["starting_at"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["StartingAt"]
        )
    if "Timezone" in data:
        out["timezone"] = data["Timezone"]
    if "RepeatAt" in data:
        out["repeat_at"] = data["RepeatAt"]
    if "TopicScheduleType" in data:
        import aws_sdk_quicksight.types.topic_schedule_type

        out["topic_schedule_type"] = (
            aws_sdk_quicksight.types.topic_schedule_type.deserialize_json(
                data["TopicScheduleType"]
            )
        )
    return out
