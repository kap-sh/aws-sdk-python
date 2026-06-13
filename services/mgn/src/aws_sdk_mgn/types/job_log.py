"""Generated from Smithy shape ``com.amazonaws.mgn#JobLog``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.iso8601_datetime_string
    import aws_sdk_mgn.types.job_log_event
    import aws_sdk_mgn.types.job_log_event_data


class JobLog(TypedDict):
    log_date_time: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Job log event date and time.</p>"""
    event: NotRequired["aws_sdk_mgn.types.job_log_event.JobLogEvent"]
    """<p>Job log event.</p>"""
    event_data: NotRequired["aws_sdk_mgn.types.job_log_event_data.JobLogEventData"]
    """<p>Job event data</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobLog) -> dict:
    out: dict = {}
    if "log_date_time" in value:
        out["logDateTime"] = value["log_date_time"]
    if "event" in value:
        out["event"] = value["event"]
    if "event_data" in value:
        import aws_sdk_mgn.types.job_log_event_data

        out["eventData"] = aws_sdk_mgn.types.job_log_event_data.serialize_json(
            value["event_data"]
        )
    return out


def deserialize_json(data: dict) -> JobLog:
    out: JobLog = {}  # type: ignore[typeddict-item]
    if "logDateTime" in data:
        out["log_date_time"] = data["logDateTime"]
    if "event" in data:
        out["event"] = data["event"]
    if "eventData" in data:
        import aws_sdk_mgn.types.job_log_event_data

        out["event_data"] = aws_sdk_mgn.types.job_log_event_data.deserialize_json(
            data["eventData"]
        )
    return out
