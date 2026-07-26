"""Generated from Smithy shape ``com.amazonaws.waf#UpdateRuleGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_waf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf.types.change_token
    import capo_waf.types.resource_id
    import capo_waf.types.rule_group_updates


class UpdateRuleGroupRequest(TypedDict, closed=True):
    rule_group_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The <code>RuleGroupId</code> of the <a>RuleGroup</a> that you want to update. <code>RuleGroupId</code> is returned by <a>CreateRuleGroup</a> and by <a>ListRuleGroups</a>.</p>"""
    updates: "capo_waf.types.rule_group_updates.RuleGroupUpdates"
    """<p>An array of <code>RuleGroupUpdate</code> objects that you want to insert into or delete from a <a>RuleGroup</a>.</p> <p>You can only insert <code>REGULAR</code> rules into a rule group.</p> <p> <code>ActivatedRule|OverrideAction</code> applies only when updating or adding a <code>RuleGroup</code> to a <code>WebACL</code>. In this case you do not use <code>ActivatedRule|Action</code>. For all other update requests, <code>ActivatedRule|Action</code> is used instead of <code>ActivatedRule|OverrideAction</code>.</p>"""
    change_token: "capo_waf.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRuleGroupRequest) -> dict:
    out: dict = {}
    out["RuleGroupId"] = value["rule_group_id"]
    import capo_waf.types.rule_group_updates

    out["Updates"] = capo_waf.types.rule_group_updates.serialize_aws_json_1_1(
        value["updates"]
    )
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRuleGroupRequest:
    out: UpdateRuleGroupRequest = {}  # type: ignore[typeddict-item]
    if "RuleGroupId" in data:
        out["rule_group_id"] = data["RuleGroupId"]
    else:
        raise DeserializationError("UpdateRuleGroupRequest.rule_group_id required")
    if "Updates" in data:
        import capo_waf.types.rule_group_updates

        out["updates"] = capo_waf.types.rule_group_updates.deserialize_aws_json_1_1(
            data["Updates"]
        )
    else:
        raise DeserializationError("UpdateRuleGroupRequest.updates required")
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    else:
        raise DeserializationError("UpdateRuleGroupRequest.change_token required")
    return out
