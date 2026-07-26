"""Generated from Smithy shape ``com.amazonaws.iot#TopicRuleListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.created_at_date
    import capo_iot.types.is_disabled
    import capo_iot.types.rule_arn
    import capo_iot.types.rule_name
    import capo_iot.types.topic_pattern


class TopicRuleListItem(TypedDict, closed=True):
    rule_arn: NotRequired["capo_iot.types.rule_arn.RuleArn"]
    """<p>The rule ARN.</p>"""
    rule_name: NotRequired["capo_iot.types.rule_name.RuleName"]
    """<p>The name of the rule.</p>"""
    topic_pattern: NotRequired["capo_iot.types.topic_pattern.TopicPattern"]
    """<p>The pattern for the topic names that apply.</p>"""
    created_at: NotRequired["capo_iot.types.created_at_date.CreatedAtDate"]
    """<p>The date and time the rule was created.</p>"""
    rule_disabled: NotRequired["capo_iot.types.is_disabled.IsDisabled"]
    """<p>Specifies whether the rule is disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicRuleListItem) -> dict:
    out: dict = {}
    if "rule_arn" in value:
        out["ruleArn"] = value["rule_arn"]
    if "rule_name" in value:
        out["ruleName"] = value["rule_name"]
    if "topic_pattern" in value:
        out["topicPattern"] = value["topic_pattern"]
    if "created_at" in value:
        import capo_iot.types.created_at_date

        out["createdAt"] = capo_iot.types.created_at_date.serialize_json(
            value["created_at"]
        )
    if "rule_disabled" in value:
        out["ruleDisabled"] = value["rule_disabled"]
    return out


def deserialize_json(data: dict) -> TopicRuleListItem:
    out: TopicRuleListItem = {}  # type: ignore[typeddict-item]
    if "ruleArn" in data:
        out["rule_arn"] = data["ruleArn"]
    if "ruleName" in data:
        out["rule_name"] = data["ruleName"]
    if "topicPattern" in data:
        out["topic_pattern"] = data["topicPattern"]
    if "createdAt" in data:
        import capo_iot.types.created_at_date

        out["created_at"] = capo_iot.types.created_at_date.deserialize_json(
            data["createdAt"]
        )
    if "ruleDisabled" in data:
        out["rule_disabled"] = data["ruleDisabled"]
    return out
