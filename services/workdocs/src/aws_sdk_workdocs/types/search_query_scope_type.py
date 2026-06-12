"""Generated from Smithy shape ``com.amazonaws.workdocs#SearchQueryScopeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

SearchQueryScopeType: TypeAlias = Literal[
    "NAME",
    "CONTENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NAME",
        "CONTENT",
    )
)


def serialize_json(value: SearchQueryScopeType) -> str:
    return value


def deserialize_json(data: str) -> SearchQueryScopeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SearchQueryScopeType value: {data!r}")
    return cast(SearchQueryScopeType, data)
