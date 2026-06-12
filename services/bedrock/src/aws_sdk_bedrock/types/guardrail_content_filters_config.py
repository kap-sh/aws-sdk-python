"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContentFiltersConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_content_filter_config

GuardrailContentFiltersConfig: TypeAlias = list[
    "aws_sdk_bedrock.types.guardrail_content_filter_config.GuardrailContentFilterConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentFiltersConfig) -> list:
    import aws_sdk_bedrock.types.guardrail_content_filter_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.guardrail_content_filter_config.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GuardrailContentFiltersConfig:
    import aws_sdk_bedrock.types.guardrail_content_filter_config

    out: GuardrailContentFiltersConfig = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.guardrail_content_filter_config.deserialize_json(item)
        )
    return out
