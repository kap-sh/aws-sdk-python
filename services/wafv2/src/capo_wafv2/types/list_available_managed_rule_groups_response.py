"""Generated from Smithy shape ``com.amazonaws.wafv2#ListAvailableManagedRuleGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.managed_rule_group_summaries
    import capo_wafv2.types.next_marker


class ListAvailableManagedRuleGroupsResponse(TypedDict, closed=True):
    next_marker: NotRequired["capo_wafv2.types.next_marker.NextMarker"]
    """<p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>"""
    managed_rule_groups: NotRequired[
        "capo_wafv2.types.managed_rule_group_summaries.ManagedRuleGroupSummaries"
    ]
    """<p>Array of managed rule groups that you can use. If you specified a <code>Limit</code> in your request, this might not be the full list. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAvailableManagedRuleGroupsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "managed_rule_groups" in value:
        import capo_wafv2.types.managed_rule_group_summaries

        out["ManagedRuleGroups"] = (
            capo_wafv2.types.managed_rule_group_summaries.serialize_aws_json_1_1(
                value["managed_rule_groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAvailableManagedRuleGroupsResponse:
    out: ListAvailableManagedRuleGroupsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "ManagedRuleGroups" in data:
        import capo_wafv2.types.managed_rule_group_summaries

        out["managed_rule_groups"] = (
            capo_wafv2.types.managed_rule_group_summaries.deserialize_aws_json_1_1(
                data["ManagedRuleGroups"]
            )
        )
    return out
