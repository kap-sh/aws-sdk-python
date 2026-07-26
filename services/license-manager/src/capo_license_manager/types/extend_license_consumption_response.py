"""Generated from Smithy shape ``com.amazonaws.licensemanager#ExtendLicenseConsumptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.iso8601_date_time
    import capo_license_manager.types.string


class ExtendLicenseConsumptionResponse(TypedDict, closed=True):
    license_consumption_token: NotRequired["capo_license_manager.types.string.String"]
    """<p>License consumption token.</p>"""
    expiration: NotRequired[
        "capo_license_manager.types.iso8601_date_time.ISO8601DateTime"
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
