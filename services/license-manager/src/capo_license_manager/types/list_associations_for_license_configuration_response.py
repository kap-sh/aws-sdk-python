"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListAssociationsForLicenseConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.license_configuration_associations
    import capo_license_manager.types.string


class ListAssociationsForLicenseConfigurationResponse(TypedDict, closed=True):
    license_configuration_associations: NotRequired[
        "capo_license_manager.types.license_configuration_associations.LicenseConfigurationAssociations"
    ]
    """<p>Information about the associations for the license configuration.</p>"""
    next_token: NotRequired["capo_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListAssociationsForLicenseConfigurationResponse,
) -> dict:
    out: dict = {}
    if "license_configuration_associations" in value:
        import capo_license_manager.types.license_configuration_associations

        out["LicenseConfigurationAssociations"] = (
            capo_license_manager.types.license_configuration_associations.serialize_aws_json_1_1(
                value["license_configuration_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListAssociationsForLicenseConfigurationResponse:
    out: ListAssociationsForLicenseConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "LicenseConfigurationAssociations" in data:
        import capo_license_manager.types.license_configuration_associations

        out["license_configuration_associations"] = (
            capo_license_manager.types.license_configuration_associations.deserialize_aws_json_1_1(
                data["LicenseConfigurationAssociations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
