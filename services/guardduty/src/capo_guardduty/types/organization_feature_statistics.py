"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationFeatureStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.integer
    import capo_guardduty.types.org_feature
    import capo_guardduty.types.organization_feature_statistics_additional_configurations


class OrganizationFeatureStatistics(TypedDict, closed=True):
    name: NotRequired["capo_guardduty.types.org_feature.OrgFeature"]
    """<p>Name of the feature.</p>"""
    enabled_accounts_count: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>Total number of accounts that have enabled a specific feature.</p>"""
    additional_configuration: NotRequired[
        "capo_guardduty.types.organization_feature_statistics_additional_configurations.OrganizationFeatureStatisticsAdditionalConfigurations"
    ]
    """<p>Name of the additional configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationFeatureStatistics) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_guardduty.types.org_feature

        out["name"] = capo_guardduty.types.org_feature.serialize_json(value["name"])
    if "enabled_accounts_count" in value:
        out["enabledAccountsCount"] = value["enabled_accounts_count"]
    if "additional_configuration" in value:
        import capo_guardduty.types.organization_feature_statistics_additional_configurations

        out["additionalConfiguration"] = (
            capo_guardduty.types.organization_feature_statistics_additional_configurations.serialize_json(
                value["additional_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> OrganizationFeatureStatistics:
    out: OrganizationFeatureStatistics = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import capo_guardduty.types.org_feature

        out["name"] = capo_guardduty.types.org_feature.deserialize_json(data["name"])
    if "enabledAccountsCount" in data:
        out["enabled_accounts_count"] = data["enabledAccountsCount"]
    if "additionalConfiguration" in data:
        import capo_guardduty.types.organization_feature_statistics_additional_configurations

        out["additional_configuration"] = (
            capo_guardduty.types.organization_feature_statistics_additional_configurations.deserialize_json(
                data["additionalConfiguration"]
            )
        )
    return out
