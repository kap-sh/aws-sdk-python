"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateLicenseConversionTaskForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.license_conversion_task_id


class CreateLicenseConversionTaskForResourceResponse(TypedDict, closed=True):
    license_conversion_task_id: NotRequired[
        "capo_license_manager.types.license_conversion_task_id.LicenseConversionTaskId"
    ]
    """<p>The ID of the created license type conversion task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: CreateLicenseConversionTaskForResourceResponse,
) -> dict:
    out: dict = {}
    if "license_conversion_task_id" in value:
        out["LicenseConversionTaskId"] = value["license_conversion_task_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> CreateLicenseConversionTaskForResourceResponse:
    out: CreateLicenseConversionTaskForResourceResponse = {}  # type: ignore[typeddict-item]
    if "LicenseConversionTaskId" in data:
        out["license_conversion_task_id"] = data["LicenseConversionTaskId"]
    return out
