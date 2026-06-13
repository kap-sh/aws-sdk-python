"""Generated from Smithy shape ``com.amazonaws.location#JobsFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_location.types.job_status


class JobsFilter(TypedDict):
    job_status: NotRequired["aws_sdk_location.types.job_status.JobStatus"]
    """<p>Filter by job status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobsFilter) -> dict:
    out: dict = {}
    if "job_status" in value:
        out["JobStatus"] = value["job_status"]
    return out


def deserialize_json(data: dict) -> JobsFilter:
    out: JobsFilter = {}  # type: ignore[typeddict-item]
    if "JobStatus" in data:
        out["job_status"] = data["JobStatus"]
    return out
