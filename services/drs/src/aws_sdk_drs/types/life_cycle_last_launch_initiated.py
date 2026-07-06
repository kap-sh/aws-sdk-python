"""Generated from Smithy shape ``com.amazonaws.drs#LifeCycleLastLaunchInitiated``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_drs.types.iso8601_datetime_string
    import aws_sdk_drs.types.job_id
    import aws_sdk_drs.types.last_launch_type


class LifeCycleLastLaunchInitiated(TypedDict, closed=True):
    api_call_date_time: NotRequired[
        "aws_sdk_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>The date and time the last Source Server launch was initiated.</p>"""
    job_id: NotRequired["aws_sdk_drs.types.job_id.JobID"]
    """<p>The ID of the Job that was used to last launch the Source Server.</p>"""
    type: NotRequired["aws_sdk_drs.types.last_launch_type.LastLaunchType"]
    """<p>The Job type that was used to last launch the Source Server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifeCycleLastLaunchInitiated) -> dict:
    out: dict = {}
    if "api_call_date_time" in value:
        out["apiCallDateTime"] = value["api_call_date_time"]
    if "job_id" in value:
        out["jobID"] = value["job_id"]
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> LifeCycleLastLaunchInitiated:
    out: LifeCycleLastLaunchInitiated = {}  # type: ignore[typeddict-item]
    if "apiCallDateTime" in data:
        out["api_call_date_time"] = data["apiCallDateTime"]
    if "jobID" in data:
        out["job_id"] = data["jobID"]
    if "type" in data:
        out["type"] = data["type"]
    return out
