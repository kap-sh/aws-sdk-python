"""Generated from Smithy shape ``com.amazonaws.quicksight#KnowledgeBaseSortByField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

KnowledgeBaseSortByField: TypeAlias = Literal[
    "KNOWLEDGE_BASE_SIZE_BYTES",
    "CREATED_AT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "KNOWLEDGE_BASE_SIZE_BYTES",
        "CREATED_AT",
    )
)


def serialize_json(value: KnowledgeBaseSortByField) -> str:
    return value


def deserialize_json(data: str) -> KnowledgeBaseSortByField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KnowledgeBaseSortByField value: {data!r}")
    return cast(KnowledgeBaseSortByField, data)
