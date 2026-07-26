"""Generated from Smithy shape ``com.amazonaws.waf#ListActivatedRulesInRuleGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf.types.activated_rules
    import capo_waf.types.next_marker


class ListActivatedRulesInRuleGroupResponse(TypedDict, closed=True):
    next_marker: NotRequired["capo_waf.types.next_marker.NextMarker"]
    """<p>If you have more <code>ActivatedRules</code> than the number that you specified for <code>Limit</code> in the request, the response includes a <code>NextMarker</code> value. To list more <code>ActivatedRules</code>, submit another <code>ListActivatedRulesInRuleGroup</code> request, and specify the <code>NextMarker</code> value from the response in the <code>NextMarker</code> value in the next request.</p>"""
    activated_rules: NotRequired["capo_waf.types.activated_rules.ActivatedRules"]
    """<p>An array of <code>ActivatedRules</code> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListActivatedRulesInRuleGroupResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "activated_rules" in value:
        import capo_waf.types.activated_rules

        out["ActivatedRules"] = capo_waf.types.activated_rules.serialize_aws_json_1_1(
            value["activated_rules"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListActivatedRulesInRuleGroupResponse:
    out: ListActivatedRulesInRuleGroupResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "ActivatedRules" in data:
        import capo_waf.types.activated_rules

        out["activated_rules"] = (
            capo_waf.types.activated_rules.deserialize_aws_json_1_1(
                data["ActivatedRules"]
            )
        )
    return out
