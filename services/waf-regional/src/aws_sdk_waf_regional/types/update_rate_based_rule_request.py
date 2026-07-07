"""Generated from Smithy shape ``com.amazonaws.wafregional#UpdateRateBasedRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.change_token
    import aws_sdk_waf_regional.types.rate_limit
    import aws_sdk_waf_regional.types.resource_id
    import aws_sdk_waf_regional.types.rule_updates


class UpdateRateBasedRuleRequest(TypedDict, closed=True):
    rule_id: "aws_sdk_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>RuleId</code> of the <code>RateBasedRule</code> that you want to update. <code>RuleId</code> is returned by <code>CreateRateBasedRule</code> and by <a>ListRateBasedRules</a>.</p>"""
    change_token: "aws_sdk_waf_regional.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""
    updates: "aws_sdk_waf_regional.types.rule_updates.RuleUpdates"
    """<p>An array of <code>RuleUpdate</code> objects that you want to insert into or delete from a <a>RateBasedRule</a>. </p>"""
    rate_limit: "aws_sdk_waf_regional.types.rate_limit.RateLimit"
    """<p>The maximum number of requests, which have an identical value in the field specified by the <code>RateKey</code>, allowed in a five-minute period. If the number of requests exceeds the <code>RateLimit</code> and the other predicates specified in the rule are also met, AWS WAF triggers the action that is specified for this rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRateBasedRuleRequest) -> dict:
    out: dict = {}
    out["RuleId"] = value["rule_id"]
    out["ChangeToken"] = value["change_token"]
    import aws_sdk_waf_regional.types.rule_updates

    out["Updates"] = aws_sdk_waf_regional.types.rule_updates.serialize_aws_json_1_1(
        value["updates"]
    )
    out["RateLimit"] = value["rate_limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRateBasedRuleRequest:
    out: UpdateRateBasedRuleRequest = {}  # type: ignore[typeddict-item]
    if "RuleId" in data:
        out["rule_id"] = data["RuleId"]
    else:
        raise DeserializationError("UpdateRateBasedRuleRequest.rule_id required")
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    else:
        raise DeserializationError("UpdateRateBasedRuleRequest.change_token required")
    if "Updates" in data:
        import aws_sdk_waf_regional.types.rule_updates

        out["updates"] = (
            aws_sdk_waf_regional.types.rule_updates.deserialize_aws_json_1_1(
                data["Updates"]
            )
        )
    else:
        raise DeserializationError("UpdateRateBasedRuleRequest.updates required")
    if "RateLimit" in data:
        out["rate_limit"] = data["RateLimit"]
    else:
        raise DeserializationError("UpdateRateBasedRuleRequest.rate_limit required")
    return out
