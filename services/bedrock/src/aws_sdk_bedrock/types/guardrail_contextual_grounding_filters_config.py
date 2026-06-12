"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContextualGroundingFiltersConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_contextual_grounding_filter_config

GuardrailContextualGroundingFiltersConfig: TypeAlias = list[
    "aws_sdk_bedrock.types.guardrail_contextual_grounding_filter_config.GuardrailContextualGroundingFilterConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContextualGroundingFiltersConfig) -> list:
    import aws_sdk_bedrock.types.guardrail_contextual_grounding_filter_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.guardrail_contextual_grounding_filter_config.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailContextualGroundingFiltersConfig:
    import aws_sdk_bedrock.types.guardrail_contextual_grounding_filter_config

    out: GuardrailContextualGroundingFiltersConfig = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.guardrail_contextual_grounding_filter_config.deserialize_json(
                item
            )
        )
    return out
