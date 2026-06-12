"""Generated from Smithy shape ``com.amazonaws.iot#ReplaceTopicRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.rule_name
    import aws_sdk_iot.types.topic_rule_payload


class ReplaceTopicRuleRequest(TypedDict):
    rule_name: "aws_sdk_iot.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    topic_rule_payload: "aws_sdk_iot.types.topic_rule_payload.TopicRulePayload"
    """<p>The rule payload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplaceTopicRuleRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.topic_rule_payload

    out["topicRulePayload"] = aws_sdk_iot.types.topic_rule_payload.serialize_json(
        value["topic_rule_payload"]
    )
    return out


def deserialize_json(data: dict) -> ReplaceTopicRuleRequest:
    out: ReplaceTopicRuleRequest = {}  # type: ignore[typeddict-item]
    if "topicRulePayload" in data:
        import aws_sdk_iot.types.topic_rule_payload

        out["topic_rule_payload"] = (
            aws_sdk_iot.types.topic_rule_payload.deserialize_json(
                data["topicRulePayload"]
            )
        )
    else:
        raise DeserializationError(
            "ReplaceTopicRuleRequest.topic_rule_payload required"
        )
    return out
