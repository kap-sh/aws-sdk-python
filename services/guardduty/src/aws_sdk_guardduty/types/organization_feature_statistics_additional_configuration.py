"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationFeatureStatisticsAdditionalConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.integer
    import aws_sdk_guardduty.types.org_feature_additional_configuration


class OrganizationFeatureStatisticsAdditionalConfiguration(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_guardduty.types.org_feature_additional_configuration.OrgFeatureAdditionalConfiguration"
    ]
    """<p>Name of the additional configuration within a feature.</p>"""
    enabled_accounts_count: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>Total number of accounts that have enabled the additional configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationFeatureStatisticsAdditionalConfiguration) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_guardduty.types.org_feature_additional_configuration

        out["name"] = (
            aws_sdk_guardduty.types.org_feature_additional_configuration.serialize_json(
                value["name"]
            )
        )
    if "enabled_accounts_count" in value:
        out["enabledAccountsCount"] = value["enabled_accounts_count"]
    return out


def deserialize_json(
    data: dict,
) -> OrganizationFeatureStatisticsAdditionalConfiguration:
    out: OrganizationFeatureStatisticsAdditionalConfiguration = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_guardduty.types.org_feature_additional_configuration

        out["name"] = (
            aws_sdk_guardduty.types.org_feature_additional_configuration.deserialize_json(
                data["name"]
            )
        )
    if "enabledAccountsCount" in data:
        out["enabled_accounts_count"] = data["enabledAccountsCount"]
    return out
