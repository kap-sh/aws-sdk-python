"""Generated from Smithy shape ``com.amazonaws.workdocs#SearchCollectionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

SearchCollectionType: TypeAlias = Literal[
    "OWNED",
    "SHARED_WITH_ME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OWNED",
        "SHARED_WITH_ME",
    )
)


def serialize_json(value: SearchCollectionType) -> str:
    return value


def deserialize_json(data: str) -> SearchCollectionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SearchCollectionType value: {data!r}")
    return cast(SearchCollectionType, data)
