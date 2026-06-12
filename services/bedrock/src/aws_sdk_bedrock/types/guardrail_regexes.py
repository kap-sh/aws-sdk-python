"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailRegexes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_regex

GuardrailRegexes: TypeAlias = list[
    "aws_sdk_bedrock.types.guardrail_regex.GuardrailRegex"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailRegexes) -> list:
    import aws_sdk_bedrock.types.guardrail_regex

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock.types.guardrail_regex.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailRegexes:
    import aws_sdk_bedrock.types.guardrail_regex

    out: GuardrailRegexes = []
    for item in data:
        out.append(aws_sdk_bedrock.types.guardrail_regex.deserialize_json(item))
    return out
