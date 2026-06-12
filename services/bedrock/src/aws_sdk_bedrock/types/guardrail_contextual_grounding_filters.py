"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContextualGroundingFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_contextual_grounding_filter

GuardrailContextualGroundingFilters: TypeAlias = list[
    "aws_sdk_bedrock.types.guardrail_contextual_grounding_filter.GuardrailContextualGroundingFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContextualGroundingFilters) -> list:
    import aws_sdk_bedrock.types.guardrail_contextual_grounding_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.guardrail_contextual_grounding_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailContextualGroundingFilters:
    import aws_sdk_bedrock.types.guardrail_contextual_grounding_filter

    out: GuardrailContextualGroundingFilters = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.guardrail_contextual_grounding_filter.deserialize_json(
                item
            )
        )
    return out
