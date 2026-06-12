"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_summary

GuardrailSummaries: TypeAlias = list[
    "aws_sdk_bedrock.types.guardrail_summary.GuardrailSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailSummaries) -> list:
    import aws_sdk_bedrock.types.guardrail_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock.types.guardrail_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailSummaries:
    import aws_sdk_bedrock.types.guardrail_summary

    out: GuardrailSummaries = []
    for item in data:
        out.append(aws_sdk_bedrock.types.guardrail_summary.deserialize_json(item))
    return out
