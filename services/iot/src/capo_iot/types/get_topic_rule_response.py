"""Generated from Smithy shape ``com.amazonaws.iot#GetTopicRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.rule_arn
    import capo_iot.types.topic_rule


class GetTopicRuleResponse(TypedDict, closed=True):
    rule_arn: NotRequired["capo_iot.types.rule_arn.RuleArn"]
    """<p>The rule ARN.</p>"""
    rule: NotRequired["capo_iot.types.topic_rule.TopicRule"]
    """<p>The rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTopicRuleResponse) -> dict:
    out: dict = {}
    if "rule_arn" in value:
        out["ruleArn"] = value["rule_arn"]
    if "rule" in value:
        import capo_iot.types.topic_rule

        out["rule"] = capo_iot.types.topic_rule.serialize_json(value["rule"])
    return out


def deserialize_json(data: dict) -> GetTopicRuleResponse:
    out: GetTopicRuleResponse = {}  # type: ignore[typeddict-item]
    if "ruleArn" in data:
        out["rule_arn"] = data["ruleArn"]
    if "rule" in data:
        import capo_iot.types.topic_rule

        out["rule"] = capo_iot.types.topic_rule.deserialize_json(data["rule"])
    return out
