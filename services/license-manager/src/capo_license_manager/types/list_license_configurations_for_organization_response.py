"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListLicenseConfigurationsForOrganizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.license_configurations
    import capo_license_manager.types.string


class ListLicenseConfigurationsForOrganizationResponse(TypedDict, closed=True):
    license_configurations: NotRequired[
        "capo_license_manager.types.license_configurations.LicenseConfigurations"
    ]
    """<p>License configurations.</p>"""
    next_token: NotRequired["capo_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListLicenseConfigurationsForOrganizationResponse,
) -> dict:
    out: dict = {}
    if "license_configurations" in value:
        import capo_license_manager.types.license_configurations

        out["LicenseConfigurations"] = (
            capo_license_manager.types.license_configurations.serialize_aws_json_1_1(
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
        import capo_license_manager.types.license_configurations

        out["license_configurations"] = (
            capo_license_manager.types.license_configurations.deserialize_aws_json_1_1(
                data["LicenseConfigurations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
