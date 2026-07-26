"""Generated from Smithy shape ``com.amazonaws.drs#JobLog``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.iso8601_datetime_string
    import capo_drs.types.job_log_event
    import capo_drs.types.job_log_event_data


class JobLog(TypedDict, closed=True):
    log_date_time: NotRequired[
        "capo_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>The date and time the log was taken.</p>"""
    event: NotRequired["capo_drs.types.job_log_event.JobLogEvent"]
    """<p>The event represents the type of a log.</p>"""
    event_data: NotRequired["capo_drs.types.job_log_event_data.JobLogEventData"]
    """<p>Metadata associated with a Job log.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobLog) -> dict:
    out: dict = {}
    if "log_date_time" in value:
        out["logDateTime"] = value["log_date_time"]
    if "event" in value:
        out["event"] = value["event"]
    if "event_data" in value:
        import capo_drs.types.job_log_event_data

        out["eventData"] = capo_drs.types.job_log_event_data.serialize_json(
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
        import capo_drs.types.job_log_event_data

        out["event_data"] = capo_drs.types.job_log_event_data.deserialize_json(
            data["eventData"]
        )
    return out
