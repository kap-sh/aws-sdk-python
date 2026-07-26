"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationFeaturesConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.organization_feature_configuration

OrganizationFeaturesConfigurations: TypeAlias = list[
    "capo_guardduty.types.organization_feature_configuration.OrganizationFeatureConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationFeaturesConfigurations) -> list:
    import capo_guardduty.types.organization_feature_configuration

    out: list = []
    for item in value:
        out.append(
            capo_guardduty.types.organization_feature_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> OrganizationFeaturesConfigurations:
    import capo_guardduty.types.organization_feature_configuration

    out: OrganizationFeaturesConfigurations = []
    for item in data:
        out.append(
            capo_guardduty.types.organization_feature_configuration.deserialize_json(
                item
            )
        )
    return out
