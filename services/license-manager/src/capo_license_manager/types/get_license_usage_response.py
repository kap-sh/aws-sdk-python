"""Generated from Smithy shape ``com.amazonaws.licensemanager#GetLicenseUsageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.license_usage


class GetLicenseUsageResponse(TypedDict, closed=True):
    license_usage: NotRequired["capo_license_manager.types.license_usage.LicenseUsage"]
    """<p>License usage details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLicenseUsageResponse) -> dict:
    out: dict = {}
    if "license_usage" in value:
        import capo_license_manager.types.license_usage

        out["LicenseUsage"] = (
            capo_license_manager.types.license_usage.serialize_aws_json_1_1(
                value["license_usage"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLicenseUsageResponse:
    out: GetLicenseUsageResponse = {}  # type: ignore[typeddict-item]
    if "LicenseUsage" in data:
        import capo_license_manager.types.license_usage

        out["license_usage"] = (
            capo_license_manager.types.license_usage.deserialize_aws_json_1_1(
                data["LicenseUsage"]
            )
        )
    return out
