"""Generated from Smithy shape ``com.amazonaws.mgn#LifeCycleLastTestInitiated``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.iso8601_datetime_string
    import aws_sdk_mgn.types.job_id


class LifeCycleLastTestInitiated(TypedDict, closed=True):
    api_call_date_time: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Lifecycle last Test initiated API call date and time.</p>"""
    job_id: NotRequired["aws_sdk_mgn.types.job_id.JobID"]
    """<p>Lifecycle last Test initiated Job ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifeCycleLastTestInitiated) -> dict:
    out: dict = {}
    if "api_call_date_time" in value:
        out["apiCallDateTime"] = value["api_call_date_time"]
    if "job_id" in value:
        out["jobID"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> LifeCycleLastTestInitiated:
    out: LifeCycleLastTestInitiated = {}  # type: ignore[typeddict-item]
    if "apiCallDateTime" in data:
        out["api_call_date_time"] = data["apiCallDateTime"]
    if "jobID" in data:
        out["job_id"] = data["jobID"]
    return out
