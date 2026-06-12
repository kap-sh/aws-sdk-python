"""Generated from Smithy shape ``com.amazonaws.waf#ListRuleGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_waf.types.next_marker
    import aws_sdk_waf.types.rule_group_summaries


class ListRuleGroupsResponse(TypedDict):
    next_marker: NotRequired["aws_sdk_waf.types.next_marker.NextMarker"]
    """<p>If you have more <code>RuleGroups</code> than the number that you specified for <code>Limit</code> in the request, the response includes a <code>NextMarker</code> value. To list more <code>RuleGroups</code>, submit another <code>ListRuleGroups</code> request, and specify the <code>NextMarker</code> value from the response in the <code>NextMarker</code> value in the next request.</p>"""
    rule_groups: NotRequired[
        "aws_sdk_waf.types.rule_group_summaries.RuleGroupSummaries"
    ]
    """<p>An array of <a>RuleGroup</a> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRuleGroupsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "rule_groups" in value:
        import aws_sdk_waf.types.rule_group_summaries

        out["RuleGroups"] = (
            aws_sdk_waf.types.rule_group_summaries.serialize_aws_json_1_1(
                value["rule_groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRuleGroupsResponse:
    out: ListRuleGroupsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "RuleGroups" in data:
        import aws_sdk_waf.types.rule_group_summaries

        out["rule_groups"] = (
            aws_sdk_waf.types.rule_group_summaries.deserialize_aws_json_1_1(
                data["RuleGroups"]
            )
        )
    return out
