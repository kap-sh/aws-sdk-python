"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseConfigurationAssociations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_license_manager.types.license_configuration_association

LicenseConfigurationAssociations: TypeAlias = list[
    "capo_license_manager.types.license_configuration_association.LicenseConfigurationAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseConfigurationAssociations) -> list:
    import capo_license_manager.types.license_configuration_association

    out: list = []
    for item in value:
        out.append(
            capo_license_manager.types.license_configuration_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LicenseConfigurationAssociations:
    import capo_license_manager.types.license_configuration_association

    out: LicenseConfigurationAssociations = []
    for item in data:
        out.append(
            capo_license_manager.types.license_configuration_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out
