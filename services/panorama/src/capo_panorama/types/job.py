"""Generated from Smithy shape ``com.amazonaws.panorama#Job``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.device_id
    import capo_panorama.types.job_id


class Job(TypedDict, closed=True):
    job_id: NotRequired["capo_panorama.types.job_id.JobId"]
    """<p>The job's ID.</p>"""
    device_id: NotRequired["capo_panorama.types.device_id.DeviceId"]
    """<p>The target device's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Job) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "device_id" in value:
        out["DeviceId"] = value["device_id"]
    return out


def deserialize_json(data: dict) -> Job:
    out: Job = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    return out
