"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateLicenseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.arn
    import aws_sdk_license_manager.types.license_status
    import aws_sdk_license_manager.types.string


class CreateLicenseResponse(TypedDict, closed=True):
    license_arn: NotRequired["aws_sdk_license_manager.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of the license.</p>"""
    status: NotRequired["aws_sdk_license_manager.types.license_status.LicenseStatus"]
    """<p>License status.</p>"""
    version: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>License version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLicenseResponse) -> dict:
    out: dict = {}
    if "license_arn" in value:
        out["LicenseArn"] = value["license_arn"]
    if "status" in value:
        import aws_sdk_license_manager.types.license_status

        out["Status"] = (
            aws_sdk_license_manager.types.license_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLicenseResponse:
    out: CreateLicenseResponse = {}  # type: ignore[typeddict-item]
    if "LicenseArn" in data:
        out["license_arn"] = data["LicenseArn"]
    if "Status" in data:
        import aws_sdk_license_manager.types.license_status

        out["status"] = (
            aws_sdk_license_manager.types.license_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "Version" in data:
        out["version"] = data["Version"]
    return out
