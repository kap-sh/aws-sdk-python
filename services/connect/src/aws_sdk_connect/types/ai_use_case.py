"""Generated from Smithy shape ``com.amazonaws.connect#AiUseCase``."""

from typing import Literal, TypeAlias, cast

AiUseCase: TypeAlias = Literal[
    "AgentAssistance",
    "SelfService",
]


# --- restJson1 ser/de ---
def serialize_json(value: AiUseCase) -> str:
    return value


def deserialize_json(data: str) -> AiUseCase:
    return cast(AiUseCase, data)
