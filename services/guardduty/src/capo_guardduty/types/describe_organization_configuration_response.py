"""Generated from Smithy shape ``com.amazonaws.guardduty#DescribeOrganizationConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.auto_enable_members
    import capo_guardduty.types.boolean
    import capo_guardduty.types.organization_data_source_configurations_result
    import capo_guardduty.types.organization_features_configurations_results
    import capo_guardduty.types.string


class DescribeOrganizationConfigurationResponse(TypedDict, closed=True):
    auto_enable: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>Indicates whether GuardDuty is automatically enabled for accounts added to the organization.</p> <p>Even though this is still supported, we recommend using <code>AutoEnableOrganizationMembers</code> to achieve the similar results.</p>"""
    member_account_limit_reached: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>Indicates whether the maximum number of allowed member accounts are already associated with the delegated administrator account for your organization.</p>"""
    data_sources: NotRequired[
        "capo_guardduty.types.organization_data_source_configurations_result.OrganizationDataSourceConfigurationsResult"
    ]
    """<p>Describes which data sources are enabled automatically for member accounts.</p>"""
    features: NotRequired[
        "capo_guardduty.types.organization_features_configurations_results.OrganizationFeaturesConfigurationsResults"
    ]
    """<p>A list of features that are configured for this organization.</p>"""
    next_token: NotRequired["capo_guardduty.types.string.String"]
    """<p>The pagination parameter to be used on the next list operation to retrieve more items.</p>"""
    auto_enable_organization_members: NotRequired[
        "capo_guardduty.types.auto_enable_members.AutoEnableMembers"
    ]
    """<p>Indicates the auto-enablement configuration of GuardDuty or any of the corresponding protection plans for the member accounts in the organization.</p> <ul> <li> <p> <code>NEW</code>: Indicates that when a new account joins the organization, they will have GuardDuty or any of the corresponding protection plans enabled automatically. </p> </li> <li> <p> <code>ALL</code>: Indicates that all accounts in the organization have GuardDuty and any of the corresponding protection plans enabled automatically. This includes <code>NEW</code> accounts that join the organization and accounts that may have been suspended or removed from the organization in GuardDuty.</p> </li> <li> <p> <code>NONE</code>: Indicates that GuardDuty or any of the corresponding protection plans will not be automatically enabled for any account in the organization. The administrator must manage GuardDuty for each account in the organization individually.</p> <p>When you update the auto-enable setting from <code>ALL</code> or <code>NEW</code> to <code>NONE</code>, this action doesn't disable the corresponding option for your existing accounts. This configuration will apply to the new accounts that join the organization. After you update the auto-enable settings, no new account will have the corresponding option as enabled.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeOrganizationConfigurationResponse) -> dict:
    out: dict = {}
    if "auto_enable" in value:
        out["autoEnable"] = value["auto_enable"]
    if "member_account_limit_reached" in value:
        out["memberAccountLimitReached"] = value["member_account_limit_reached"]
    if "data_sources" in value:
        import capo_guardduty.types.organization_data_source_configurations_result

        out["dataSources"] = (
            capo_guardduty.types.organization_data_source_configurations_result.serialize_json(
                value["data_sources"]
            )
        )
    if "features" in value:
        import capo_guardduty.types.organization_features_configurations_results

        out["features"] = (
            capo_guardduty.types.organization_features_configurations_results.serialize_json(
                value["features"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "auto_enable_organization_members" in value:
        import capo_guardduty.types.auto_enable_members

        out["autoEnableOrganizationMembers"] = (
            capo_guardduty.types.auto_enable_members.serialize_json(
                value["auto_enable_organization_members"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeOrganizationConfigurationResponse:
    out: DescribeOrganizationConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "autoEnable" in data:
        out["auto_enable"] = data["autoEnable"]
    if "memberAccountLimitReached" in data:
        out["member_account_limit_reached"] = data["memberAccountLimitReached"]
    if "dataSources" in data:
        import capo_guardduty.types.organization_data_source_configurations_result

        out["data_sources"] = (
            capo_guardduty.types.organization_data_source_configurations_result.deserialize_json(
                data["dataSources"]
            )
        )
    if "features" in data:
        import capo_guardduty.types.organization_features_configurations_results

        out["features"] = (
            capo_guardduty.types.organization_features_configurations_results.deserialize_json(
                data["features"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "autoEnableOrganizationMembers" in data:
        import capo_guardduty.types.auto_enable_members

        out["auto_enable_organization_members"] = (
            capo_guardduty.types.auto_enable_members.deserialize_json(
                data["autoEnableOrganizationMembers"]
            )
        )
    return out
