"""Generated from Smithy shape ``com.amazonaws.licensemanager#DeleteLicenseRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.arn
    import aws_sdk_license_manager.types.string


class DeleteLicenseRequest(TypedDict):
    license_arn: "aws_sdk_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the license.</p>"""
    source_version: "aws_sdk_license_manager.types.string.String"
    """<p>Current version of the license.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLicenseRequest) -> dict:
    out: dict = {}
    out["LicenseArn"] = value["license_arn"]
    out["SourceVersion"] = value["source_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLicenseRequest:
    out: DeleteLicenseRequest = {}  # type: ignore[typeddict-item]
    if "LicenseArn" in data:
        out["license_arn"] = data["LicenseArn"]
    else:
        raise DeserializationError("DeleteLicenseRequest.license_arn required")
    if "SourceVersion" in data:
        out["source_version"] = data["SourceVersion"]
    else:
        raise DeserializationError("DeleteLicenseRequest.source_version required")
    return out
