"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListLicenseConfigurationsForOrganizationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.license_configurations
    import aws_sdk_license_manager.types.string


class ListLicenseConfigurationsForOrganizationResponse(TypedDict):
    license_configurations: NotRequired[
        "aws_sdk_license_manager.types.license_configurations.LicenseConfigurations"
    ]
    """<p>License configurations.</p>"""
    next_token: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListLicenseConfigurationsForOrganizationResponse,
) -> dict:
    out: dict = {}
    if "license_configurations" in value:
        import aws_sdk_license_manager.types.license_configurations

        out["LicenseConfigurations"] = (
            aws_sdk_license_manager.types.license_configurations.serialize_aws_json_1_1(
                value["license_configurations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListLicenseConfigurationsForOrganizationResponse:
    out: ListLicenseConfigurationsForOrganizationResponse = {}  # type: ignore[typeddict-item]
    if "LicenseConfigurations" in data:
        import aws_sdk_license_manager.types.license_configurations

        out["license_configurations"] = (
            aws_sdk_license_manager.types.license_configurations.deserialize_aws_json_1_1(
                data["LicenseConfigurations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
