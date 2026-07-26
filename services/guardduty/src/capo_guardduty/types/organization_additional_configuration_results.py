"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationAdditionalConfigurationResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.organization_additional_configuration_result

OrganizationAdditionalConfigurationResults: TypeAlias = list[
    "capo_guardduty.types.organization_additional_configuration_result.OrganizationAdditionalConfigurationResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationAdditionalConfigurationResults) -> list:
    import capo_guardduty.types.organization_additional_configuration_result

    out: list = []
    for item in value:
        out.append(
            capo_guardduty.types.organization_additional_configuration_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> OrganizationAdditionalConfigurationResults:
    import capo_guardduty.types.organization_additional_configuration_result

    out: OrganizationAdditionalConfigurationResults = []
    for item in data:
        out.append(
            capo_guardduty.types.organization_additional_configuration_result.deserialize_json(
                item
            )
        )
    return out
