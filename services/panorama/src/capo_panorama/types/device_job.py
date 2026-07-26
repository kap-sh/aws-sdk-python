"""Generated from Smithy shape ``com.amazonaws.panorama#DeviceJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.created_time
    import capo_panorama.types.device_id
    import capo_panorama.types.device_name
    import capo_panorama.types.job_id
    import capo_panorama.types.job_type


class DeviceJob(TypedDict, closed=True):
    device_name: NotRequired["capo_panorama.types.device_name.DeviceName"]
    """<p>The name of the target device</p>"""
    device_id: NotRequired["capo_panorama.types.device_id.DeviceId"]
    """<p>The ID of the target device.</p>"""
    job_id: NotRequired["capo_panorama.types.job_id.JobId"]
    """<p>The job's ID.</p>"""
    created_time: NotRequired["capo_panorama.types.created_time.CreatedTime"]
    """<p>When the job was created.</p>"""
    job_type: NotRequired["capo_panorama.types.job_type.JobType"]
    """<p>The job's type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeviceJob) -> dict:
    out: dict = {}
    if "device_name" in value:
        out["DeviceName"] = value["device_name"]
    if "device_id" in value:
        out["DeviceId"] = value["device_id"]
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "created_time" in value:
        import capo_panorama.types.created_time

        out["CreatedTime"] = capo_panorama.types.created_time.serialize_json(
            value["created_time"]
        )
    if "job_type" in value:
        out["JobType"] = value["job_type"]
    return out


def deserialize_json(data: dict) -> DeviceJob:
    out: DeviceJob = {}  # type: ignore[typeddict-item]
    if "DeviceName" in data:
        out["device_name"] = data["DeviceName"]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "CreatedTime" in data:
        import capo_panorama.types.created_time

        out["created_time"] = capo_panorama.types.created_time.deserialize_json(
            data["CreatedTime"]
        )
    if "JobType" in data:
        out["job_type"] = data["JobType"]
    return out
