"""Generated from Smithy shape ``com.amazonaws.quicksight#KnowledgeBaseSearchOperator``."""

from typing import Literal, TypeAlias, cast

KnowledgeBaseSearchOperator: TypeAlias = Literal[
    "STRING_EQUALS",
    "STRING_LIKE",
    "GREATER_THAN_OR_EQUALS",
    "LESS_THAN_OR_EQUALS",
]


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseSearchOperator) -> str:
    return value


def deserialize_json(data: str) -> KnowledgeBaseSearchOperator:
    return cast(KnowledgeBaseSearchOperator, data)
