"""Generated from Smithy shape ``com.amazonaws.panorama#CreateJobForDevicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.device_id_list
    import aws_sdk_panorama.types.device_job_config
    import aws_sdk_panorama.types.job_type


class CreateJobForDevicesRequest(TypedDict, closed=True):
    device_ids: "aws_sdk_panorama.types.device_id_list.DeviceIdList"
    """<p>ID of target device.</p>"""
    device_job_config: NotRequired[
        "aws_sdk_panorama.types.device_job_config.DeviceJobConfig"
    ]
    """<p>Configuration settings for a software update job.</p>"""
    job_type: "aws_sdk_panorama.types.job_type.JobType"
    """<p>The type of job to run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobForDevicesRequest) -> dict:
    out: dict = {}
    import aws_sdk_panorama.types.device_id_list

    out["DeviceIds"] = aws_sdk_panorama.types.device_id_list.serialize_json(
        value["device_ids"]
    )
    if "device_job_config" in value:
        import aws_sdk_panorama.types.device_job_config

        out["DeviceJobConfig"] = (
            aws_sdk_panorama.types.device_job_config.serialize_json(
                value["device_job_config"]
            )
        )
    out["JobType"] = value["job_type"]
    return out


def deserialize_json(data: dict) -> CreateJobForDevicesRequest:
    out: CreateJobForDevicesRequest = {}  # type: ignore[typeddict-item]
    if "DeviceIds" in data:
        import aws_sdk_panorama.types.device_id_list

        out["device_ids"] = aws_sdk_panorama.types.device_id_list.deserialize_json(
            data["DeviceIds"]
        )
    else:
        raise DeserializationError("CreateJobForDevicesRequest.device_ids required")
    if "DeviceJobConfig" in data:
        import aws_sdk_panorama.types.device_job_config

        out["device_job_config"] = (
            aws_sdk_panorama.types.device_job_config.deserialize_json(
                data["DeviceJobConfig"]
            )
        )
    if "JobType" in data:
        out["job_type"] = data["JobType"]
    else:
        raise DeserializationError("CreateJobForDevicesRequest.job_type required")
    return out
