"""Generated from Smithy shape ``com.amazonaws.licensemanager#GetLicenseConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager.types.string


class GetLicenseConfigurationRequest(TypedDict, closed=True):
    license_configuration_arn: "capo_license_manager.types.string.String"
    """<p>Amazon Resource Name (ARN) of the license configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLicenseConfigurationRequest) -> dict:
    out: dict = {}
    out["LicenseConfigurationArn"] = value["license_configuration_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLicenseConfigurationRequest:
    out: GetLicenseConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "LicenseConfigurationArn" in data:
        out["license_configuration_arn"] = data["LicenseConfigurationArn"]
    else:
        raise DeserializationError(
            "GetLicenseConfigurationRequest.license_configuration_arn required"
        )
    return out
