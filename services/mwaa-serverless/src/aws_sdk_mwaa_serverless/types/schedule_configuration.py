"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#ScheduleConfiguration``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ScheduleConfiguration(TypedDict):
    cron_expression: NotRequired["str"]
    """<p>A cron expression that defines when the workflow is automatically executed. Uses standard cron syntax.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduleConfiguration) -> dict:
    out: dict = {}
    if "cron_expression" in value:
        out["CronExpression"] = value["cron_expression"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ScheduleConfiguration:
    out: ScheduleConfiguration = {}  # type: ignore[typeddict-item]
    if "CronExpression" in data:
        out["cron_expression"] = data["CronExpression"]
    return out
