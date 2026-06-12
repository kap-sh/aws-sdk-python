"""Generated from Smithy shape ``com.amazonaws.workdocs#OrderByFieldType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

OrderByFieldType: TypeAlias = Literal[
    "RELEVANCE",
    "NAME",
    "SIZE",
    "CREATED_TIMESTAMP",
    "MODIFIED_TIMESTAMP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RELEVANCE",
        "NAME",
        "SIZE",
        "CREATED_TIMESTAMP",
        "MODIFIED_TIMESTAMP",
    )
)


def serialize_json(value: OrderByFieldType) -> str:
    return value


def deserialize_json(data: str) -> OrderByFieldType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrderByFieldType value: {data!r}")
    return cast(OrderByFieldType, data)
