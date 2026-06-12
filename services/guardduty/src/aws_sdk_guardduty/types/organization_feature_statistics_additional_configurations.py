"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationFeatureStatisticsAdditionalConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.organization_feature_statistics_additional_configuration

OrganizationFeatureStatisticsAdditionalConfigurations: TypeAlias = list[
    "aws_sdk_guardduty.types.organization_feature_statistics_additional_configuration.OrganizationFeatureStatisticsAdditionalConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: OrganizationFeatureStatisticsAdditionalConfigurations,
) -> list:
    import aws_sdk_guardduty.types.organization_feature_statistics_additional_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_guardduty.types.organization_feature_statistics_additional_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> OrganizationFeatureStatisticsAdditionalConfigurations:
    import aws_sdk_guardduty.types.organization_feature_statistics_additional_configuration

    out: OrganizationFeatureStatisticsAdditionalConfigurations = []
    for item in data:
        out.append(
            aws_sdk_guardduty.types.organization_feature_statistics_additional_configuration.deserialize_json(
                item
            )
        )
    return out
