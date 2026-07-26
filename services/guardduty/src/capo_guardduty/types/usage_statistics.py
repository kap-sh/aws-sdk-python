"""Generated from Smithy shape ``com.amazonaws.guardduty#UsageStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.usage_account_result_list
    import capo_guardduty.types.usage_data_source_result_list
    import capo_guardduty.types.usage_feature_result_list
    import capo_guardduty.types.usage_resource_result_list
    import capo_guardduty.types.usage_top_accounts_result_list


class UsageStatistics(TypedDict, closed=True):
    sum_by_account: NotRequired[
        "capo_guardduty.types.usage_account_result_list.UsageAccountResultList"
    ]
    """<p>The usage statistic sum organized by account ID.</p>"""
    top_accounts_by_feature: NotRequired[
        "capo_guardduty.types.usage_top_accounts_result_list.UsageTopAccountsResultList"
    ]
    """<p>Lists the top 50 accounts by feature that have generated the most GuardDuty usage, in the order from most to least expensive.</p> <p>Currently, this doesn't support <code>RDS_LOGIN_EVENTS</code>.</p>"""
    sum_by_data_source: NotRequired[
        "capo_guardduty.types.usage_data_source_result_list.UsageDataSourceResultList"
    ]
    """<p>The usage statistic sum organized by on data source.</p>"""
    sum_by_resource: NotRequired[
        "capo_guardduty.types.usage_resource_result_list.UsageResourceResultList"
    ]
    """<p>The usage statistic sum organized by resource.</p>"""
    top_resources: NotRequired[
        "capo_guardduty.types.usage_resource_result_list.UsageResourceResultList"
    ]
    """<p>Lists the top 50 resources that have generated the most GuardDuty usage, in order from most to least expensive.</p>"""
    sum_by_feature: NotRequired[
        "capo_guardduty.types.usage_feature_result_list.UsageFeatureResultList"
    ]
    """<p>The usage statistic sum organized by feature.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsageStatistics) -> dict:
    out: dict = {}
    if "sum_by_account" in value:
        import capo_guardduty.types.usage_account_result_list

        out["sumByAccount"] = (
            capo_guardduty.types.usage_account_result_list.serialize_json(
                value["sum_by_account"]
            )
        )
    if "top_accounts_by_feature" in value:
        import capo_guardduty.types.usage_top_accounts_result_list

        out["topAccountsByFeature"] = (
            capo_guardduty.types.usage_top_accounts_result_list.serialize_json(
                value["top_accounts_by_feature"]
            )
        )
    if "sum_by_data_source" in value:
        import capo_guardduty.types.usage_data_source_result_list

        out["sumByDataSource"] = (
            capo_guardduty.types.usage_data_source_result_list.serialize_json(
                value["sum_by_data_source"]
            )
        )
    if "sum_by_resource" in value:
        import capo_guardduty.types.usage_resource_result_list

        out["sumByResource"] = (
            capo_guardduty.types.usage_resource_result_list.serialize_json(
                value["sum_by_resource"]
            )
        )
    if "top_resources" in value:
        import capo_guardduty.types.usage_resource_result_list

        out["topResources"] = (
            capo_guardduty.types.usage_resource_result_list.serialize_json(
                value["top_resources"]
            )
        )
    if "sum_by_feature" in value:
        import capo_guardduty.types.usage_feature_result_list

        out["sumByFeature"] = (
            capo_guardduty.types.usage_feature_result_list.serialize_json(
                value["sum_by_feature"]
            )
        )
    return out


def deserialize_json(data: dict) -> UsageStatistics:
    out: UsageStatistics = {}  # type: ignore[typeddict-item]
    if "sumByAccount" in data:
        import capo_guardduty.types.usage_account_result_list

        out["sum_by_account"] = (
            capo_guardduty.types.usage_account_result_list.deserialize_json(
                data["sumByAccount"]
            )
        )
    if "topAccountsByFeature" in data:
        import capo_guardduty.types.usage_top_accounts_result_list

        out["top_accounts_by_feature"] = (
            capo_guardduty.types.usage_top_accounts_result_list.deserialize_json(
                data["topAccountsByFeature"]
            )
        )
    if "sumByDataSource" in data:
        import capo_guardduty.types.usage_data_source_result_list

        out["sum_by_data_source"] = (
            capo_guardduty.types.usage_data_source_result_list.deserialize_json(
                data["sumByDataSource"]
            )
        )
    if "sumByResource" in data:
        import capo_guardduty.types.usage_resource_result_list

        out["sum_by_resource"] = (
            capo_guardduty.types.usage_resource_result_list.deserialize_json(
                data["sumByResource"]
            )
        )
    if "topResources" in data:
        import capo_guardduty.types.usage_resource_result_list

        out["top_resources"] = (
            capo_guardduty.types.usage_resource_result_list.deserialize_json(
                data["topResources"]
            )
        )
    if "sumByFeature" in data:
        import capo_guardduty.types.usage_feature_result_list

        out["sum_by_feature"] = (
            capo_guardduty.types.usage_feature_result_list.deserialize_json(
                data["sumByFeature"]
            )
        )
    return out
