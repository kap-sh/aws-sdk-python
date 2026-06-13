"""Generated from Smithy shape ``com.amazonaws.qconnect#GuardrailTopicExamples``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.guardrail_topic_example

GuardrailTopicExamples: TypeAlias = list[
    "aws_sdk_qconnect.types.guardrail_topic_example.GuardrailTopicExample"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopicExamples) -> list:
    return list(value)


def deserialize_json(data: list) -> GuardrailTopicExamples:
    return list(data)
