"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContextualGroundingFilterType``."""

from typing import Literal, TypeAlias, cast

GuardrailContextualGroundingFilterType: TypeAlias = Literal[
    "GROUNDING",
    "RELEVANCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContextualGroundingFilterType) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContextualGroundingFilterType:
    return cast(GuardrailContextualGroundingFilterType, data)
