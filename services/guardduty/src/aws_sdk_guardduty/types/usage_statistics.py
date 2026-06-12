"""Generated from Smithy shape ``com.amazonaws.guardduty#UsageStatistics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.usage_account_result_list
    import aws_sdk_guardduty.types.usage_data_source_result_list
    import aws_sdk_guardduty.types.usage_feature_result_list
    import aws_sdk_guardduty.types.usage_resource_result_list
    import aws_sdk_guardduty.types.usage_top_accounts_result_list


class UsageStatistics(TypedDict):
    sum_by_account: NotRequired[
        "aws_sdk_guardduty.types.usage_account_result_list.UsageAccountResultList"
    ]
    """<p>The usage statistic sum organized by account ID.</p>"""
    top_accounts_by_feature: NotRequired[
        "aws_sdk_guardduty.types.usage_top_accounts_result_list.UsageTopAccountsResultList"
    ]
    """<p>Lists the top 50 accounts by feature that have generated the most GuardDuty usage, in the order from most to least expensive.</p> <p>Currently, this doesn't support <code>RDS_LOGIN_EVENTS</code>.</p>"""
    sum_by_data_source: NotRequired[
        "aws_sdk_guardduty.types.usage_data_source_result_list.UsageDataSourceResultList"
    ]
    """<p>The usage statistic sum organized by on data source.</p>"""
    sum_by_resource: NotRequired[
        "aws_sdk_guardduty.types.usage_resource_result_list.UsageResourceResultList"
    ]
    """<p>The usage statistic sum organized by resource.</p>"""
    top_resources: NotRequired[
        "aws_sdk_guardduty.types.usage_resource_result_list.UsageResourceResultList"
    ]
    """<p>Lists the top 50 resources that have generated the most GuardDuty usage, in order from most to least expensive.</p>"""
    sum_by_feature: NotRequired[
        "aws_sdk_guardduty.types.usage_feature_result_list.UsageFeatureResultList"
    ]
    """<p>The usage statistic sum organized by feature.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsageStatistics) -> dict:
    out: dict = {}
    if "sum_by_account" in value:
        import aws_sdk_guardduty.types.usage_account_result_list

        out["sumByAccount"] = (
            aws_sdk_guardduty.types.usage_account_result_list.serialize_json(
                value["sum_by_account"]
            )
        )
    if "top_accounts_by_feature" in value:
        import aws_sdk_guardduty.types.usage_top_accounts_result_list

        out["topAccountsByFeature"] = (
            aws_sdk_guardduty.types.usage_top_accounts_result_list.serialize_json(
                value["top_accounts_by_feature"]
            )
        )
    if "sum_by_data_source" in value:
        import aws_sdk_guardduty.types.usage_data_source_result_list

        out["sumByDataSource"] = (
            aws_sdk_guardduty.types.usage_data_source_result_list.serialize_json(
                value["sum_by_data_source"]
            )
        )
    if "sum_by_resource" in value:
        import aws_sdk_guardduty.types.usage_resource_result_list

        out["sumByResource"] = (
            aws_sdk_guardduty.types.usage_resource_result_list.serialize_json(
                value["sum_by_resource"]
            )
        )
    if "top_resources" in value:
        import aws_sdk_guardduty.types.usage_resource_result_list

        out["topResources"] = (
            aws_sdk_guardduty.types.usage_resource_result_list.serialize_json(
                value["top_resources"]
            )
        )
    if "sum_by_feature" in value:
        import aws_sdk_guardduty.types.usage_feature_result_list

        out["sumByFeature"] = (
            aws_sdk_guardduty.types.usage_feature_result_list.serialize_json(
                value["sum_by_feature"]
            )
        )
    return out


def deserialize_json(data: dict) -> UsageStatistics:
    out: UsageStatistics = {}  # type: ignore[typeddict-item]
    if "sumByAccount" in data:
        import aws_sdk_guardduty.types.usage_account_result_list

        out["sum_by_account"] = (
            aws_sdk_guardduty.types.usage_account_result_list.deserialize_json(
                data["sumByAccount"]
            )
        )
    if "topAccountsByFeature" in data:
        import aws_sdk_guardduty.types.usage_top_accounts_result_list

        out["top_accounts_by_feature"] = (
            aws_sdk_guardduty.types.usage_top_accounts_result_list.deserialize_json(
                data["topAccountsByFeature"]
            )
        )
    if "sumByDataSource" in data:
        import aws_sdk_guardduty.types.usage_data_source_result_list

        out["sum_by_data_source"] = (
            aws_sdk_guardduty.types.usage_data_source_result_list.deserialize_json(
                data["sumByDataSource"]
            )
        )
    if "sumByResource" in data:
        import aws_sdk_guardduty.types.usage_resource_result_list

        out["sum_by_resource"] = (
            aws_sdk_guardduty.types.usage_resource_result_list.deserialize_json(
                data["sumByResource"]
            )
        )
    if "topResources" in data:
        import aws_sdk_guardduty.types.usage_resource_result_list

        out["top_resources"] = (
            aws_sdk_guardduty.types.usage_resource_result_list.deserialize_json(
                data["topResources"]
            )
        )
    if "sumByFeature" in data:
        import aws_sdk_guardduty.types.usage_feature_result_list

        out["sum_by_feature"] = (
            aws_sdk_guardduty.types.usage_feature_result_list.deserialize_json(
                data["sumByFeature"]
            )
        )
    return out
