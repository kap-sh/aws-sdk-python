"""Generated from Smithy shape ``com.amazonaws.panorama#DescribeDeviceJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.device_arn
    import capo_panorama.types.device_id
    import capo_panorama.types.device_name
    import capo_panorama.types.device_type
    import capo_panorama.types.image_version
    import capo_panorama.types.job_id
    import capo_panorama.types.job_type
    import capo_panorama.types.update_created_time
    import capo_panorama.types.update_progress


class DescribeDeviceJobResponse(TypedDict, closed=True):
    job_id: NotRequired["capo_panorama.types.job_id.JobId"]
    """<p>The job's ID.</p>"""
    device_id: NotRequired["capo_panorama.types.device_id.DeviceId"]
    """<p>The device's ID.</p>"""
    device_arn: NotRequired["capo_panorama.types.device_arn.DeviceArn"]
    """<p>The device's ARN.</p>"""
    device_name: NotRequired["capo_panorama.types.device_name.DeviceName"]
    """<p>The device's name.</p>"""
    device_type: NotRequired["capo_panorama.types.device_type.DeviceType"]
    """<p>The device's type.</p>"""
    image_version: NotRequired["capo_panorama.types.image_version.ImageVersion"]
    """<p>For an OTA job, the target version of the device software.</p>"""
    status: NotRequired["capo_panorama.types.update_progress.UpdateProgress"]
    """<p>The job's status.</p>"""
    created_time: NotRequired[
        "capo_panorama.types.update_created_time.UpdateCreatedTime"
    ]
    """<p>When the job was created.</p>"""
    job_type: NotRequired["capo_panorama.types.job_type.JobType"]
    """<p>The job's type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDeviceJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "device_id" in value:
        out["DeviceId"] = value["device_id"]
    if "device_arn" in value:
        out["DeviceArn"] = value["device_arn"]
    if "device_name" in value:
        out["DeviceName"] = value["device_name"]
    if "device_type" in value:
        out["DeviceType"] = value["device_type"]
    if "image_version" in value:
        out["ImageVersion"] = value["image_version"]
    if "status" in value:
        out["Status"] = value["status"]
    if "created_time" in value:
        import capo_panorama.types.update_created_time

        out["CreatedTime"] = capo_panorama.types.update_created_time.serialize_json(
            value["created_time"]
        )
    if "job_type" in value:
        out["JobType"] = value["job_type"]
    return out


def deserialize_json(data: dict) -> DescribeDeviceJobResponse:
    out: DescribeDeviceJobResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    if "DeviceArn" in data:
        out["device_arn"] = data["DeviceArn"]
    if "DeviceName" in data:
        out["device_name"] = data["DeviceName"]
    if "DeviceType" in data:
        out["device_type"] = data["DeviceType"]
    if "ImageVersion" in data:
        out["image_version"] = data["ImageVersion"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "CreatedTime" in data:
        import capo_panorama.types.update_created_time

        out["created_time"] = capo_panorama.types.update_created_time.deserialize_json(
            data["CreatedTime"]
        )
    if "JobType" in data:
        out["job_type"] = data["JobType"]
    return out
