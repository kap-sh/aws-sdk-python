"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailTopicPolicyAssessment``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_topic_list


class GuardrailTopicPolicyAssessment(TypedDict):
    topics: "aws_sdk_bedrock_runtime.types.guardrail_topic_list.GuardrailTopicList"
    """<p>The topics in the assessment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopicPolicyAssessment) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.guardrail_topic_list

    out["topics"] = aws_sdk_bedrock_runtime.types.guardrail_topic_list.serialize_json(
        value["topics"]
    )
    return out


def deserialize_json(data: dict) -> GuardrailTopicPolicyAssessment:
    out: GuardrailTopicPolicyAssessment = {}  # type: ignore[typeddict-item]
    if "topics" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_topic_list

        out["topics"] = (
            aws_sdk_bedrock_runtime.types.guardrail_topic_list.deserialize_json(
                data["topics"]
            )
        )
    else:
        raise DeserializationError("GuardrailTopicPolicyAssessment.topics required")
    return out
