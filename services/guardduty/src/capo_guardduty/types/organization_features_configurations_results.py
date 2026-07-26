"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationFeaturesConfigurationsResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.organization_feature_configuration_result

OrganizationFeaturesConfigurationsResults: TypeAlias = list[
    "capo_guardduty.types.organization_feature_configuration_result.OrganizationFeatureConfigurationResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationFeaturesConfigurationsResults) -> list:
    import capo_guardduty.types.organization_feature_configuration_result

    out: list = []
    for item in value:
        out.append(
            capo_guardduty.types.organization_feature_configuration_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> OrganizationFeaturesConfigurationsResults:
    import capo_guardduty.types.organization_feature_configuration_result

    out: OrganizationFeaturesConfigurationsResults = []
    for item in data:
        out.append(
            capo_guardduty.types.organization_feature_configuration_result.deserialize_json(
                item
            )
        )
    return out
