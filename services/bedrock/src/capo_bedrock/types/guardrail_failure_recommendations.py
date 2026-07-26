"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailFailureRecommendations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_failure_recommendation

GuardrailFailureRecommendations: TypeAlias = list[
    "capo_bedrock.types.guardrail_failure_recommendation.GuardrailFailureRecommendation"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailFailureRecommendations) -> list:
    return list(value)


def deserialize_json(data: list) -> GuardrailFailureRecommendations:
    return list(data)
