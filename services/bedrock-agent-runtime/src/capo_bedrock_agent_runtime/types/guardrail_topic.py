"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailTopic``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.guardrail_topic_policy_action
    import capo_bedrock_agent_runtime.types.guardrail_topic_type


class GuardrailTopic(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name details on a specific topic in the Guardrail.</p>"""
    type: NotRequired[
        "capo_bedrock_agent_runtime.types.guardrail_topic_type.GuardrailTopicType"
    ]
    """<p>The type details on a specific topic in the Guardrail.</p>"""
    action: NotRequired[
        "capo_bedrock_agent_runtime.types.guardrail_topic_policy_action.GuardrailTopicPolicyAction"
    ]
    """<p>The action details on a specific topic in the Guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopic) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        import capo_bedrock_agent_runtime.types.guardrail_topic_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.guardrail_topic_type.serialize_json(
                value["type"]
            )
        )
    if "action" in value:
        import capo_bedrock_agent_runtime.types.guardrail_topic_policy_action

        out["action"] = (
            capo_bedrock_agent_runtime.types.guardrail_topic_policy_action.serialize_json(
                value["action"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailTopic:
    out: GuardrailTopic = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        import capo_bedrock_agent_runtime.types.guardrail_topic_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.guardrail_topic_type.deserialize_json(
                data["type"]
            )
        )
    if "action" in data:
        import capo_bedrock_agent_runtime.types.guardrail_topic_policy_action

        out["action"] = (
            capo_bedrock_agent_runtime.types.guardrail_topic_policy_action.deserialize_json(
                data["action"]
            )
        )
    return out
