"""Generated from Smithy shape ``com.amazonaws.greengrass#CreateSoftwareUpdateJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class CreateSoftwareUpdateJobResponse(TypedDict):
    iot_job_arn: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The IoT Job ARN corresponding to this update."""
    iot_job_id: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The IoT Job Id corresponding to this update."""
    platform_software_version: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The software version installed on the device or devices after the update."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSoftwareUpdateJobResponse) -> dict:
    out: dict = {}
    if "iot_job_arn" in value:
        out["IotJobArn"] = value["iot_job_arn"]
    if "iot_job_id" in value:
        out["IotJobId"] = value["iot_job_id"]
    if "platform_software_version" in value:
        out["PlatformSoftwareVersion"] = value["platform_software_version"]
    return out


def deserialize_json(data: dict) -> CreateSoftwareUpdateJobResponse:
    out: CreateSoftwareUpdateJobResponse = {}  # type: ignore[typeddict-item]
    if "IotJobArn" in data:
        out["iot_job_arn"] = data["IotJobArn"]
    if "IotJobId" in data:
        out["iot_job_id"] = data["IotJobId"]
    if "PlatformSoftwareVersion" in data:
        out["platform_software_version"] = data["PlatformSoftwareVersion"]
    return out
