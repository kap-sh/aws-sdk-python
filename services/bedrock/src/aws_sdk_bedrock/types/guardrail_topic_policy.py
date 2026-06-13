"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailTopicPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_topics
    import aws_sdk_bedrock.types.guardrail_topics_tier


class GuardrailTopicPolicy(TypedDict):
    topics: "aws_sdk_bedrock.types.guardrail_topics.GuardrailTopics"
    """<p>A list of policies related to topics that the guardrail should deny.</p>"""
    tier: NotRequired["aws_sdk_bedrock.types.guardrail_topics_tier.GuardrailTopicsTier"]
    """<p>The tier that your guardrail uses for denied topic filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopicPolicy) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.guardrail_topics

    out["topics"] = aws_sdk_bedrock.types.guardrail_topics.serialize_json(
        value["topics"]
    )
    if "tier" in value:
        import aws_sdk_bedrock.types.guardrail_topics_tier

        out["tier"] = aws_sdk_bedrock.types.guardrail_topics_tier.serialize_json(
            value["tier"]
        )
    return out


def deserialize_json(data: dict) -> GuardrailTopicPolicy:
    out: GuardrailTopicPolicy = {}  # type: ignore[typeddict-item]
    if "topics" in data:
        import aws_sdk_bedrock.types.guardrail_topics

        out["topics"] = aws_sdk_bedrock.types.guardrail_topics.deserialize_json(
            data["topics"]
        )
    else:
        raise DeserializationError("GuardrailTopicPolicy.topics required")
    if "tier" in data:
        import aws_sdk_bedrock.types.guardrail_topics_tier

        out["tier"] = aws_sdk_bedrock.types.guardrail_topics_tier.deserialize_json(
            data["tier"]
        )
    return out
