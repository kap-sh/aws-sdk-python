"""Generated from Smithy shape ``com.amazonaws.bedrock#ApplicationType``."""

from typing import Literal, TypeAlias, cast

ApplicationType: TypeAlias = Literal[
    "ModelEvaluation",
    "RagEvaluation",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationType) -> str:
    return value


def deserialize_json(data: str) -> ApplicationType:
    return cast(ApplicationType, data)
