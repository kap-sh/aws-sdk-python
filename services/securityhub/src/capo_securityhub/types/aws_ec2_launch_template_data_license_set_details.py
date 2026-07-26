"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataLicenseSetDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsEc2LaunchTemplateDataLicenseSetDetails(TypedDict, closed=True):
    license_configuration_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of the license configuration. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2LaunchTemplateDataLicenseSetDetails) -> dict:
    out: dict = {}
    if "license_configuration_arn" in value:
        out["LicenseConfigurationArn"] = value["license_configuration_arn"]
    return out


def deserialize_json(data: dict) -> AwsEc2LaunchTemplateDataLicenseSetDetails:
    out: AwsEc2LaunchTemplateDataLicenseSetDetails = {}  # type: ignore[typeddict-item]
    if "LicenseConfigurationArn" in data:
        out["license_configuration_arn"] = data["LicenseConfigurationArn"]
    return out
