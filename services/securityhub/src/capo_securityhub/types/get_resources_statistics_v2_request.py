"""Generated from Smithy shape ``com.amazonaws.securityhub#GetResourcesStatisticsV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.max_statistic_results
    import capo_securityhub.types.resource_group_by_rules
    import capo_securityhub.types.resource_scopes
    import capo_securityhub.types.sort_order


class GetResourcesStatisticsV2Request(TypedDict, closed=True):
    group_by_rules: NotRequired[
        "capo_securityhub.types.resource_group_by_rules.ResourceGroupByRules"
    ]
    """<p>How resource statistics should be aggregated and organized in the response.</p>"""
    scopes: NotRequired["capo_securityhub.types.resource_scopes.ResourceScopes"]
    """<p>Limits the results to resources from specific organizational units or from the delegated administrator's organization. Only the delegated administrator account can use this parameter. Other accounts receive an <code>AccessDeniedException</code>.</p> <p>This parameter is optional. If you omit it, the delegated administrator sees statistics from all accounts across the entire organization. Other accounts see only statistics for their own resources.</p> <p>You can specify up to 10 entries in <code>Scopes.AwsOrganizations</code>. If multiple entries are specified, the entries are combined using OR logic.</p>"""
    sort_order: NotRequired["capo_securityhub.types.sort_order.SortOrder"]
    """<p>Sorts aggregated statistics.</p>"""
    max_statistic_results: NotRequired[
        "capo_securityhub.types.max_statistic_results.MaxStatisticResults"
    ]
    """<p>The maximum number of results to be returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcesStatisticsV2Request) -> dict:
    out: dict = {}
    if "group_by_rules" in value:
        import capo_securityhub.types.resource_group_by_rules

        out["GroupByRules"] = (
            capo_securityhub.types.resource_group_by_rules.serialize_json(
                value["group_by_rules"]
            )
        )
    if "scopes" in value:
        import capo_securityhub.types.resource_scopes

        out["Scopes"] = capo_securityhub.types.resource_scopes.serialize_json(
            value["scopes"]
        )
    if "sort_order" in value:
        import capo_securityhub.types.sort_order

        out["SortOrder"] = capo_securityhub.types.sort_order.serialize_json(
            value["sort_order"]
        )
    if "max_statistic_results" in value:
        out["MaxStatisticResults"] = value["max_statistic_results"]
    return out


def deserialize_json(data: dict) -> GetResourcesStatisticsV2Request:
    out: GetResourcesStatisticsV2Request = {}  # type: ignore[typeddict-item]
    if "GroupByRules" in data:
        import capo_securityhub.types.resource_group_by_rules

        out["group_by_rules"] = (
            capo_securityhub.types.resource_group_by_rules.deserialize_json(
                data["GroupByRules"]
            )
        )
    if "Scopes" in data:
        import capo_securityhub.types.resource_scopes

        out["scopes"] = capo_securityhub.types.resource_scopes.deserialize_json(
            data["Scopes"]
        )
    if "SortOrder" in data:
        import capo_securityhub.types.sort_order

        out["sort_order"] = capo_securityhub.types.sort_order.deserialize_json(
            data["SortOrder"]
        )
    if "MaxStatisticResults" in data:
        out["max_statistic_results"] = data["MaxStatisticResults"]
    return out
