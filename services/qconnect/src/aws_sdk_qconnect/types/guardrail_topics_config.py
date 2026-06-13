"""Generated from Smithy shape ``com.amazonaws.qconnect#GuardrailTopicsConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.guardrail_topic_config

GuardrailTopicsConfig: TypeAlias = list[
    "aws_sdk_qconnect.types.guardrail_topic_config.GuardrailTopicConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopicsConfig) -> list:
    import aws_sdk_qconnect.types.guardrail_topic_config

    out: list = []
    for item in value:
        out.append(aws_sdk_qconnect.types.guardrail_topic_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailTopicsConfig:
    import aws_sdk_qconnect.types.guardrail_topic_config

    out: GuardrailTopicsConfig = []
    for item in data:
        out.append(aws_sdk_qconnect.types.guardrail_topic_config.deserialize_json(item))
    return out
