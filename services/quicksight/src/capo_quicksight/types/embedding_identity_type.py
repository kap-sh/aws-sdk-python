"""Generated from Smithy shape ``com.amazonaws.quicksight#EmbeddingIdentityType``."""

from typing import Literal, TypeAlias, cast

EmbeddingIdentityType: TypeAlias = Literal[
    "IAM",
    "QUICKSIGHT",
    "ANONYMOUS",
]


# --- restJson1 ser/de ---
def serialize_json(value: EmbeddingIdentityType) -> str:
    return value


def deserialize_json(data: str) -> EmbeddingIdentityType:
    return cast(EmbeddingIdentityType, data)
