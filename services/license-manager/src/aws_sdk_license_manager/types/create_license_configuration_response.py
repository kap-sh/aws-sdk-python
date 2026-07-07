"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateLicenseConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.string


class CreateLicenseConfigurationResponse(TypedDict, closed=True):
    license_configuration_arn: NotRequired[
        "aws_sdk_license_manager.types.string.String"
    ]
    """<p>Amazon Resource Name (ARN) of the license configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLicenseConfigurationResponse) -> dict:
    out: dict = {}
    if "license_configuration_arn" in value:
        out["LicenseConfigurationArn"] = value["license_configuration_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLicenseConfigurationResponse:
    out: CreateLicenseConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "LicenseConfigurationArn" in data:
        out["license_configuration_arn"] = data["LicenseConfigurationArn"]
    return out
