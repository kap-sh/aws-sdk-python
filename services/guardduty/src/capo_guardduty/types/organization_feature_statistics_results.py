"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationFeatureStatisticsResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.organization_feature_statistics

OrganizationFeatureStatisticsResults: TypeAlias = list[
    "capo_guardduty.types.organization_feature_statistics.OrganizationFeatureStatistics"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationFeatureStatisticsResults) -> list:
    import capo_guardduty.types.organization_feature_statistics

    out: list = []
    for item in value:
        out.append(
            capo_guardduty.types.organization_feature_statistics.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> OrganizationFeatureStatisticsResults:
    import capo_guardduty.types.organization_feature_statistics

    out: OrganizationFeatureStatisticsResults = []
    for item in data:
        out.append(
            capo_guardduty.types.organization_feature_statistics.deserialize_json(item)
        )
    return out
