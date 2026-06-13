"""Generated from Smithy shape ``com.amazonaws.mgn#LifeCycleLastCutoverInitiated``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.iso8601_datetime_string
    import aws_sdk_mgn.types.job_id


class LifeCycleLastCutoverInitiated(TypedDict):
    api_call_date_time: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p/>"""
    job_id: NotRequired["aws_sdk_mgn.types.job_id.JobID"]
    """<p>Lifecycle last Cutover initiated by Job ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifeCycleLastCutoverInitiated) -> dict:
    out: dict = {}
    if "api_call_date_time" in value:
        out["apiCallDateTime"] = value["api_call_date_time"]
    if "job_id" in value:
        out["jobID"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> LifeCycleLastCutoverInitiated:
    out: LifeCycleLastCutoverInitiated = {}  # type: ignore[typeddict-item]
    if "apiCallDateTime" in data:
        out["api_call_date_time"] = data["apiCallDateTime"]
    if "jobID" in data:
        out["job_id"] = data["jobID"]
    return out
