"""Generated from Smithy shape ``com.amazonaws.wafregional#RuleGroupUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.activated_rule
    import aws_sdk_waf_regional.types.change_action


class RuleGroupUpdate(TypedDict, closed=True):
    action: "aws_sdk_waf_regional.types.change_action.ChangeAction"
    """<p>Specify <code>INSERT</code> to add an <code>ActivatedRule</code> to a <code>RuleGroup</code>. Use <code>DELETE</code> to remove an <code>ActivatedRule</code> from a <code>RuleGroup</code>.</p>"""
    activated_rule: "aws_sdk_waf_regional.types.activated_rule.ActivatedRule"
    """<p>The <code>ActivatedRule</code> object specifies a <code>Rule</code> that you want to insert or delete, the priority of the <code>Rule</code> in the <code>WebACL</code>, and the action that you want AWS WAF to take when a web request matches the <code>Rule</code> (<code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleGroupUpdate) -> dict:
    out: dict = {}
    import aws_sdk_waf_regional.types.change_action

    out["Action"] = aws_sdk_waf_regional.types.change_action.serialize_aws_json_1_1(
        value["action"]
    )
    import aws_sdk_waf_regional.types.activated_rule

    out["ActivatedRule"] = (
        aws_sdk_waf_regional.types.activated_rule.serialize_aws_json_1_1(
            value["activated_rule"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleGroupUpdate:
    out: RuleGroupUpdate = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_waf_regional.types.change_action

        out["action"] = (
            aws_sdk_waf_regional.types.change_action.deserialize_aws_json_1_1(
                data["Action"]
            )
        )
    else:
        raise DeserializationError("RuleGroupUpdate.action required")
    if "ActivatedRule" in data:
        import aws_sdk_waf_regional.types.activated_rule

        out["activated_rule"] = (
            aws_sdk_waf_regional.types.activated_rule.deserialize_aws_json_1_1(
                data["ActivatedRule"]
            )
        )
    else:
        raise DeserializationError("RuleGroupUpdate.activated_rule required")
    return out
