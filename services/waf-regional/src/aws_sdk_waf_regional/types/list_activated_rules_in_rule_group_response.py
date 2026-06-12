"""Generated from Smithy shape ``com.amazonaws.wafregional#ListActivatedRulesInRuleGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.activated_rules
    import aws_sdk_waf_regional.types.next_marker


class ListActivatedRulesInRuleGroupResponse(TypedDict):
    next_marker: NotRequired["aws_sdk_waf_regional.types.next_marker.NextMarker"]
    """<p>If you have more <code>ActivatedRules</code> than the number that you specified for <code>Limit</code> in the request, the response includes a <code>NextMarker</code> value. To list more <code>ActivatedRules</code>, submit another <code>ListActivatedRulesInRuleGroup</code> request, and specify the <code>NextMarker</code> value from the response in the <code>NextMarker</code> value in the next request.</p>"""
    activated_rules: NotRequired[
        "aws_sdk_waf_regional.types.activated_rules.ActivatedRules"
    ]
    """<p>An array of <code>ActivatedRules</code> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListActivatedRulesInRuleGroupResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "activated_rules" in value:
        import aws_sdk_waf_regional.types.activated_rules

        out["ActivatedRules"] = (
            aws_sdk_waf_regional.types.activated_rules.serialize_aws_json_1_1(
                value["activated_rules"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListActivatedRulesInRuleGroupResponse:
    out: ListActivatedRulesInRuleGroupResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "ActivatedRules" in data:
        import aws_sdk_waf_regional.types.activated_rules

        out["activated_rules"] = (
            aws_sdk_waf_regional.types.activated_rules.deserialize_aws_json_1_1(
                data["ActivatedRules"]
            )
        )
    return out
