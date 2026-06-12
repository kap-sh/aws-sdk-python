"""Generated from Smithy shape ``com.amazonaws.wafv2#ListRuleGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.next_marker
    import aws_sdk_wafv2.types.rule_group_summaries


class ListRuleGroupsResponse(TypedDict):
    next_marker: NotRequired["aws_sdk_wafv2.types.next_marker.NextMarker"]
    """<p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>"""
    rule_groups: NotRequired[
        "aws_sdk_wafv2.types.rule_group_summaries.RuleGroupSummaries"
    ]
    """<p>Array of rule groups. If you specified a <code>Limit</code> in your request, this might not be the full list. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRuleGroupsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "rule_groups" in value:
        import aws_sdk_wafv2.types.rule_group_summaries

        out["RuleGroups"] = (
            aws_sdk_wafv2.types.rule_group_summaries.serialize_aws_json_1_1(
                value["rule_groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRuleGroupsResponse:
    out: ListRuleGroupsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "RuleGroups" in data:
        import aws_sdk_wafv2.types.rule_group_summaries

        out["rule_groups"] = (
            aws_sdk_wafv2.types.rule_group_summaries.deserialize_aws_json_1_1(
                data["RuleGroups"]
            )
        )
    return out
