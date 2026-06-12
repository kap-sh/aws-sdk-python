"""Generated from Smithy shape ``com.amazonaws.licensemanager#GetLicenseConversionTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.license_conversion_task_id


class GetLicenseConversionTaskRequest(TypedDict):
    license_conversion_task_id: "aws_sdk_license_manager.types.license_conversion_task_id.LicenseConversionTaskId"
    """<p>ID of the license type conversion task to retrieve information on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLicenseConversionTaskRequest) -> dict:
    out: dict = {}
    out["LicenseConversionTaskId"] = value["license_conversion_task_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLicenseConversionTaskRequest:
    out: GetLicenseConversionTaskRequest = {}  # type: ignore[typeddict-item]
    if "LicenseConversionTaskId" in data:
        out["license_conversion_task_id"] = data["LicenseConversionTaskId"]
    else:
        raise DeserializationError(
            "GetLicenseConversionTaskRequest.license_conversion_task_id required"
        )
    return out
