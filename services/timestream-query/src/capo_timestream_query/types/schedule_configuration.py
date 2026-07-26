"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ScheduleConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import capo_timestream_query.types.schedule_expression


class ScheduleConfiguration(TypedDict, closed=True):
    schedule_expression: (
        "capo_timestream_query.types.schedule_expression.ScheduleExpression"
    )
    """<p>An expression that denotes when to trigger the scheduled query run. This can be a cron expression or a rate expression. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduleConfiguration) -> dict:
    out: dict = {}
    out["ScheduleExpression"] = value["schedule_expression"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ScheduleConfiguration:
    out: ScheduleConfiguration = {}  # type: ignore[typeddict-item]
    if "ScheduleExpression" in data:
        out["schedule_expression"] = data["ScheduleExpression"]
    else:
        raise DeserializationError("ScheduleConfiguration.schedule_expression required")
    return out
