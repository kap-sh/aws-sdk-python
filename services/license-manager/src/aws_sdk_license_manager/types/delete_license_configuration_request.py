"""Generated from Smithy shape ``com.amazonaws.licensemanager#DeleteLicenseConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.string


class DeleteLicenseConfigurationRequest(TypedDict, closed=True):
    license_configuration_arn: "aws_sdk_license_manager.types.string.String"
    """<p>ID of the license configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLicenseConfigurationRequest) -> dict:
    out: dict = {}
    out["LicenseConfigurationArn"] = value["license_configuration_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLicenseConfigurationRequest:
    out: DeleteLicenseConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "LicenseConfigurationArn" in data:
        out["license_configuration_arn"] = data["LicenseConfigurationArn"]
    else:
        raise DeserializationError(
            "DeleteLicenseConfigurationRequest.license_configuration_arn required"
        )
    return out
