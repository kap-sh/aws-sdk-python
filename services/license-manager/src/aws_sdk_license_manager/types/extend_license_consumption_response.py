"""Generated from Smithy shape ``com.amazonaws.licensemanager#ExtendLicenseConsumptionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.iso8601_date_time
    import aws_sdk_license_manager.types.string


class ExtendLicenseConsumptionResponse(TypedDict):
    license_consumption_token: NotRequired[
        "aws_sdk_license_manager.types.string.String"
    ]
    """<p>License consumption token.</p>"""
    expiration: NotRequired[
        "aws_sdk_license_manager.types.iso8601_date_time.ISO8601DateTime"
    ]
    """<p>Date and time at which the license consumption expires.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtendLicenseConsumptionResponse) -> dict:
    out: dict = {}
    if "license_consumption_token" in value:
        out["LicenseConsumptionToken"] = value["license_consumption_token"]
    if "expiration" in value:
        out["Expiration"] = value["expiration"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExtendLicenseConsumptionResponse:
    out: ExtendLicenseConsumptionResponse = {}  # type: ignore[typeddict-item]
    if "LicenseConsumptionToken" in data:
        out["license_consumption_token"] = data["LicenseConsumptionToken"]
    if "Expiration" in data:
        out["expiration"] = data["Expiration"]
    return out
