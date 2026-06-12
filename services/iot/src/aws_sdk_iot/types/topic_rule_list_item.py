"""Generated from Smithy shape ``com.amazonaws.iot#TopicRuleListItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.created_at_date
    import aws_sdk_iot.types.is_disabled
    import aws_sdk_iot.types.rule_arn
    import aws_sdk_iot.types.rule_name
    import aws_sdk_iot.types.topic_pattern


class TopicRuleListItem(TypedDict):
    rule_arn: NotRequired["aws_sdk_iot.types.rule_arn.RuleArn"]
    """<p>The rule ARN.</p>"""
    rule_name: NotRequired["aws_sdk_iot.types.rule_name.RuleName"]
    """<p>The name of the rule.</p>"""
    topic_pattern: NotRequired["aws_sdk_iot.types.topic_pattern.TopicPattern"]
    """<p>The pattern for the topic names that apply.</p>"""
    created_at: NotRequired["aws_sdk_iot.types.created_at_date.CreatedAtDate"]
    """<p>The date and time the rule was created.</p>"""
    rule_disabled: NotRequired["aws_sdk_iot.types.is_disabled.IsDisabled"]
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
        import aws_sdk_iot.types.created_at_date

        out["createdAt"] = aws_sdk_iot.types.created_at_date.serialize_json(
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
        import aws_sdk_iot.types.created_at_date

        out["created_at"] = aws_sdk_iot.types.created_at_date.deserialize_json(
            data["createdAt"]
        )
    if "ruleDisabled" in data:
        out["rule_disabled"] = data["ruleDisabled"]
    return out
