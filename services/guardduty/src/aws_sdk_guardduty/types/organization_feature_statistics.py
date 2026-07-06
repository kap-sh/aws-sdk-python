"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationFeatureStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.integer
    import aws_sdk_guardduty.types.org_feature
    import aws_sdk_guardduty.types.organization_feature_statistics_additional_configurations


class OrganizationFeatureStatistics(TypedDict, closed=True):
    name: NotRequired["aws_sdk_guardduty.types.org_feature.OrgFeature"]
    """<p>Name of the feature.</p>"""
    enabled_accounts_count: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>Total number of accounts that have enabled a specific feature.</p>"""
    additional_configuration: NotRequired[
        "aws_sdk_guardduty.types.organization_feature_statistics_additional_configurations.OrganizationFeatureStatisticsAdditionalConfigurations"
    ]
    """<p>Name of the additional configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationFeatureStatistics) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_guardduty.types.org_feature

        out["name"] = aws_sdk_guardduty.types.org_feature.serialize_json(value["name"])
    if "enabled_accounts_count" in value:
        out["enabledAccountsCount"] = value["enabled_accounts_count"]
    if "additional_configuration" in value:
        import aws_sdk_guardduty.types.organization_feature_statistics_additional_configurations

        out["additionalConfiguration"] = (
            aws_sdk_guardduty.types.organization_feature_statistics_additional_configurations.serialize_json(
                value["additional_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> OrganizationFeatureStatistics:
    out: OrganizationFeatureStatistics = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_guardduty.types.org_feature

        out["name"] = aws_sdk_guardduty.types.org_feature.deserialize_json(data["name"])
    if "enabledAccountsCount" in data:
        out["enabled_accounts_count"] = data["enabledAccountsCount"]
    if "additionalConfiguration" in data:
        import aws_sdk_guardduty.types.organization_feature_statistics_additional_configurations

        out["additional_configuration"] = (
            aws_sdk_guardduty.types.organization_feature_statistics_additional_configurations.deserialize_json(
                data["additionalConfiguration"]
            )
        )
    return out
