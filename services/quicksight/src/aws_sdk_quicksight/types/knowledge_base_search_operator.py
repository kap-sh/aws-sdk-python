"""Generated from Smithy shape ``com.amazonaws.quicksight#KnowledgeBaseSearchOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

KnowledgeBaseSearchOperator: TypeAlias = Literal[
    "STRING_EQUALS",
    "STRING_LIKE",
    "GREATER_THAN_OR_EQUALS",
    "LESS_THAN_OR_EQUALS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRING_EQUALS",
        "STRING_LIKE",
        "GREATER_THAN_OR_EQUALS",
        "LESS_THAN_OR_EQUALS",
    )
)


def serialize_json(value: KnowledgeBaseSearchOperator) -> str:
    return value


def deserialize_json(data: str) -> KnowledgeBaseSearchOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown KnowledgeBaseSearchOperator value: {data!r}"
        )
    return cast(KnowledgeBaseSearchOperator, data)
