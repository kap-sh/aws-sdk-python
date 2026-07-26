"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationAdditionalConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.organization_additional_configuration

OrganizationAdditionalConfigurations: TypeAlias = list[
    "capo_guardduty.types.organization_additional_configuration.OrganizationAdditionalConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationAdditionalConfigurations) -> list:
    import capo_guardduty.types.organization_additional_configuration

    out: list = []
    for item in value:
        out.append(
            capo_guardduty.types.organization_additional_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> OrganizationAdditionalConfigurations:
    import capo_guardduty.types.organization_additional_configuration

    out: OrganizationAdditionalConfigurations = []
    for item in data:
        out.append(
            capo_guardduty.types.organization_additional_configuration.deserialize_json(
                item
            )
        )
    return out
