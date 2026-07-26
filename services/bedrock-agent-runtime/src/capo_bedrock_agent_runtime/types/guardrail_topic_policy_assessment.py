"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailTopicPolicyAssessment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.guardrail_topic_list


class GuardrailTopicPolicyAssessment(TypedDict, closed=True):
    topics: NotRequired[
        "capo_bedrock_agent_runtime.types.guardrail_topic_list.GuardrailTopicList"
    ]
    """<p>The topic details of the policy assessment used in the Guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopicPolicyAssessment) -> dict:
    out: dict = {}
    if "topics" in value:
        import capo_bedrock_agent_runtime.types.guardrail_topic_list

        out["topics"] = (
            capo_bedrock_agent_runtime.types.guardrail_topic_list.serialize_json(
                value["topics"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailTopicPolicyAssessment:
    out: GuardrailTopicPolicyAssessment = {}  # type: ignore[typeddict-item]
    if "topics" in data:
        import capo_bedrock_agent_runtime.types.guardrail_topic_list

        out["topics"] = (
            capo_bedrock_agent_runtime.types.guardrail_topic_list.deserialize_json(
                data["topics"]
            )
        )
    return out
