"""Generated from Smithy shape ``com.amazonaws.panorama#LatestDeviceJob``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_panorama.types.image_version
    import aws_sdk_panorama.types.job_type
    import aws_sdk_panorama.types.update_progress


class LatestDeviceJob(TypedDict):
    image_version: NotRequired["aws_sdk_panorama.types.image_version.ImageVersion"]
    """<p>The target version of the device software.</p>"""
    status: NotRequired["aws_sdk_panorama.types.update_progress.UpdateProgress"]
    """<p>Status of the latest device job.</p>"""
    job_type: NotRequired["aws_sdk_panorama.types.job_type.JobType"]
    """<p>The job's type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LatestDeviceJob) -> dict:
    out: dict = {}
    if "image_version" in value:
        out["ImageVersion"] = value["image_version"]
    if "status" in value:
        out["Status"] = value["status"]
    if "job_type" in value:
        out["JobType"] = value["job_type"]
    return out


def deserialize_json(data: dict) -> LatestDeviceJob:
    out: LatestDeviceJob = {}  # type: ignore[typeddict-item]
    if "ImageVersion" in data:
        out["image_version"] = data["ImageVersion"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "JobType" in data:
        out["job_type"] = data["JobType"]
    return out
