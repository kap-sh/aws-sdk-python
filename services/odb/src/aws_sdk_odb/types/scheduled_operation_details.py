"""Generated from Smithy shape ``com.amazonaws.odb#ScheduledOperationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.day_of_week


class ScheduledOperationDetails(TypedDict):
    day_of_week: "aws_sdk_odb.types.day_of_week.DayOfWeek"
    """<p>The day of the week on which the scheduled operation occurs.</p>"""
    scheduled_start_time: NotRequired["str"]
    """<p>The scheduled start time for the Autonomous Database, in UTC.</p>"""
    scheduled_stop_time: NotRequired["str"]
    """<p>The scheduled stop time for the Autonomous Database, in UTC.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduledOperationDetails) -> dict:
    out: dict = {}
    import aws_sdk_odb.types.day_of_week

    out["dayOfWeek"] = aws_sdk_odb.types.day_of_week.serialize_aws_json_1_0(
        value["day_of_week"]
    )
    if "scheduled_start_time" in value:
        out["scheduledStartTime"] = value["scheduled_start_time"]
    if "scheduled_stop_time" in value:
        out["scheduledStopTime"] = value["scheduled_stop_time"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ScheduledOperationDetails:
    out: ScheduledOperationDetails = {}  # type: ignore[typeddict-item]
    if "dayOfWeek" in data:
        import aws_sdk_odb.types.day_of_week

        out["day_of_week"] = aws_sdk_odb.types.day_of_week.deserialize_aws_json_1_0(
            data["dayOfWeek"]
        )
    else:
        raise DeserializationError("ScheduledOperationDetails.day_of_week required")
    if "scheduledStartTime" in data:
        out["scheduled_start_time"] = data["scheduledStartTime"]
    if "scheduledStopTime" in data:
        out["scheduled_stop_time"] = data["scheduledStopTime"]
    return out
