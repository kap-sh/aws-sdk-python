"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateLicenseVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.arn
    import capo_license_manager.types.license_status
    import capo_license_manager.types.string


class CreateLicenseVersionResponse(TypedDict, closed=True):
    license_arn: NotRequired["capo_license_manager.types.arn.Arn"]
    """<p>License ARN.</p>"""
    version: NotRequired["capo_license_manager.types.string.String"]
    """<p>New version of the license.</p>"""
    status: NotRequired["capo_license_manager.types.license_status.LicenseStatus"]
    """<p>License status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLicenseVersionResponse) -> dict:
    out: dict = {}
    if "license_arn" in value:
        out["LicenseArn"] = value["license_arn"]
    if "version" in value:
        out["Version"] = value["version"]
    if "status" in value:
        import capo_license_manager.types.license_status

        out["Status"] = (
            capo_license_manager.types.license_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLicenseVersionResponse:
    out: CreateLicenseVersionResponse = {}  # type: ignore[typeddict-item]
    if "LicenseArn" in data:
        out["license_arn"] = data["LicenseArn"]
    if "Version" in data:
        out["version"] = data["Version"]
    if "Status" in data:
        import capo_license_manager.types.license_status

        out["status"] = (
            capo_license_manager.types.license_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out
