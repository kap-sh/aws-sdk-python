"""Generated from Smithy shape ``com.amazonaws.waf#DeleteRuleGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_waf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf.types.change_token
    import capo_waf.types.resource_id


class DeleteRuleGroupRequest(TypedDict, closed=True):
    rule_group_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The <code>RuleGroupId</code> of the <a>RuleGroup</a> that you want to delete. <code>RuleGroupId</code> is returned by <a>CreateRuleGroup</a> and by <a>ListRuleGroups</a>.</p>"""
    change_token: "capo_waf.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRuleGroupRequest) -> dict:
    out: dict = {}
    out["RuleGroupId"] = value["rule_group_id"]
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRuleGroupRequest:
    out: DeleteRuleGroupRequest = {}  # type: ignore[typeddict-item]
    if "RuleGroupId" in data:
        out["rule_group_id"] = data["RuleGroupId"]
    else:
        raise DeserializationError("DeleteRuleGroupRequest.rule_group_id required")
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    else:
        raise DeserializationError("DeleteRuleGroupRequest.change_token required")
    return out
