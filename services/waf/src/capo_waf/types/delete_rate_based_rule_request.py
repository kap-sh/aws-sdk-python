"""Generated from Smithy shape ``com.amazonaws.waf#DeleteRateBasedRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_waf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf.types.change_token
    import capo_waf.types.resource_id


class DeleteRateBasedRuleRequest(TypedDict, closed=True):
    rule_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The <code>RuleId</code> of the <a>RateBasedRule</a> that you want to delete. <code>RuleId</code> is returned by <a>CreateRateBasedRule</a> and by <a>ListRateBasedRules</a>.</p>"""
    change_token: "capo_waf.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRateBasedRuleRequest) -> dict:
    out: dict = {}
    out["RuleId"] = value["rule_id"]
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRateBasedRuleRequest:
    out: DeleteRateBasedRuleRequest = {}  # type: ignore[typeddict-item]
    if "RuleId" in data:
        out["rule_id"] = data["RuleId"]
    else:
        raise DeserializationError("DeleteRateBasedRuleRequest.rule_id required")
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    else:
        raise DeserializationError("DeleteRateBasedRuleRequest.change_token required")
    return out
