"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailStatusReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_status_reason

GuardrailStatusReasons: TypeAlias = list[
    "aws_sdk_bedrock.types.guardrail_status_reason.GuardrailStatusReason"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailStatusReasons) -> list:
    return list(value)


def deserialize_json(data: list) -> GuardrailStatusReasons:
    return list(data)
