"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailTopicPolicyConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_topics_config
    import aws_sdk_bedrock.types.guardrail_topics_tier_config


class GuardrailTopicPolicyConfig(TypedDict):
    topics_config: "aws_sdk_bedrock.types.guardrail_topics_config.GuardrailTopicsConfig"
    """<p>A list of policies related to topics that the guardrail should deny.</p>"""
    tier_config: NotRequired[
        "aws_sdk_bedrock.types.guardrail_topics_tier_config.GuardrailTopicsTierConfig"
    ]
    """<p>The tier that your guardrail uses for denied topic filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopicPolicyConfig) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.guardrail_topics_config

    out["topicsConfig"] = aws_sdk_bedrock.types.guardrail_topics_config.serialize_json(
        value["topics_config"]
    )
    if "tier_config" in value:
        import aws_sdk_bedrock.types.guardrail_topics_tier_config

        out["tierConfig"] = (
            aws_sdk_bedrock.types.guardrail_topics_tier_config.serialize_json(
                value["tier_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailTopicPolicyConfig:
    out: GuardrailTopicPolicyConfig = {}  # type: ignore[typeddict-item]
    if "topicsConfig" in data:
        import aws_sdk_bedrock.types.guardrail_topics_config

        out["topics_config"] = (
            aws_sdk_bedrock.types.guardrail_topics_config.deserialize_json(
                data["topicsConfig"]
            )
        )
    else:
        raise DeserializationError("GuardrailTopicPolicyConfig.topics_config required")
    if "tierConfig" in data:
        import aws_sdk_bedrock.types.guardrail_topics_tier_config

        out["tier_config"] = (
            aws_sdk_bedrock.types.guardrail_topics_tier_config.deserialize_json(
                data["tierConfig"]
            )
        )
    return out
