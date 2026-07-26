"""Generated from Smithy shape ``com.amazonaws.wafregional#ListSubscribedRuleGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.next_marker
    import capo_waf_regional.types.subscribed_rule_group_summaries


class ListSubscribedRuleGroupsResponse(TypedDict, closed=True):
    next_marker: NotRequired["capo_waf_regional.types.next_marker.NextMarker"]
    """<p>If you have more objects than the number that you specified for <code>Limit</code> in the request, the response includes a <code>NextMarker</code> value. To list more objects, submit another <code>ListSubscribedRuleGroups</code> request, and specify the <code>NextMarker</code> value from the response in the <code>NextMarker</code> value in the next request.</p>"""
    rule_groups: NotRequired[
        "capo_waf_regional.types.subscribed_rule_group_summaries.SubscribedRuleGroupSummaries"
    ]
    """<p>An array of <a>RuleGroup</a> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSubscribedRuleGroupsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "rule_groups" in value:
        import capo_waf_regional.types.subscribed_rule_group_summaries

        out["RuleGroups"] = (
            capo_waf_regional.types.subscribed_rule_group_summaries.serialize_aws_json_1_1(
                value["rule_groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSubscribedRuleGroupsResponse:
    out: ListSubscribedRuleGroupsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "RuleGroups" in data:
        import capo_waf_regional.types.subscribed_rule_group_summaries

        out["rule_groups"] = (
            capo_waf_regional.types.subscribed_rule_group_summaries.deserialize_aws_json_1_1(
                data["RuleGroups"]
            )
        )
    return out
