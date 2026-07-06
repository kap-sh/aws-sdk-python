"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailTopic``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_topic_policy_action
    import aws_sdk_bedrock_runtime.types.guardrail_topic_type


class GuardrailTopic(TypedDict, closed=True):
    name: "str"
    """<p>The name for the guardrail.</p>"""
    type: "aws_sdk_bedrock_runtime.types.guardrail_topic_type.GuardrailTopicType"
    """<p>The type behavior that the guardrail should perform when the model detects the topic.</p>"""
    action: "aws_sdk_bedrock_runtime.types.guardrail_topic_policy_action.GuardrailTopicPolicyAction"
    """<p>The action the guardrail should take when it intervenes on a topic.</p>"""
    detected: NotRequired["bool"]
    """<p>Indicates whether topic content that breaches the guardrail configuration is detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopic) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_bedrock_runtime.types.guardrail_topic_type

    out["type"] = aws_sdk_bedrock_runtime.types.guardrail_topic_type.serialize_json(
        value["type"]
    )
    import aws_sdk_bedrock_runtime.types.guardrail_topic_policy_action

    out["action"] = (
        aws_sdk_bedrock_runtime.types.guardrail_topic_policy_action.serialize_json(
            value["action"]
        )
    )
    if "detected" in value:
        out["detected"] = value["detected"]
    return out


def deserialize_json(data: dict) -> GuardrailTopic:
    out: GuardrailTopic = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GuardrailTopic.name required")
    if "type" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_topic_type

        out["type"] = (
            aws_sdk_bedrock_runtime.types.guardrail_topic_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("GuardrailTopic.type required")
    if "action" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_topic_policy_action

        out["action"] = (
            aws_sdk_bedrock_runtime.types.guardrail_topic_policy_action.deserialize_json(
                data["action"]
            )
        )
    else:
        raise DeserializationError("GuardrailTopic.action required")
    if "detected" in data:
        out["detected"] = data["detected"]
    return out
