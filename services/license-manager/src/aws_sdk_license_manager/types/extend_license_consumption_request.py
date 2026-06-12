"""Generated from Smithy shape ``com.amazonaws.licensemanager#ExtendLicenseConsumptionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.boolean
    import aws_sdk_license_manager.types.string


class ExtendLicenseConsumptionRequest(TypedDict):
    license_consumption_token: "aws_sdk_license_manager.types.string.String"
    """<p>License consumption token.</p>"""
    dry_run: "aws_sdk_license_manager.types.boolean.Boolean"
    """<p>Checks whether you have the required permissions for the action, without actually making the request. Provides an error response if you do not have the required permissions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtendLicenseConsumptionRequest) -> dict:
    out: dict = {}
    out["LicenseConsumptionToken"] = value["license_consumption_token"]
    out["DryRun"] = value.get("dry_run", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ExtendLicenseConsumptionRequest:
    out: ExtendLicenseConsumptionRequest = {}  # type: ignore[typeddict-item]
    if "LicenseConsumptionToken" in data:
        out["license_consumption_token"] = data["LicenseConsumptionToken"]
    else:
        raise DeserializationError(
            "ExtendLicenseConsumptionRequest.license_consumption_token required"
        )
    if "DryRun" in data:
        out["dry_run"] = data["DryRun"]
    else:
        out["dry_run"] = False
    return out
