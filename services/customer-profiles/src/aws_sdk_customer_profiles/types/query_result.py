"""Generated from Smithy shape ``com.amazonaws.customerprofiles#QueryResult``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

QueryResult: TypeAlias = Literal[
    "PRESENT",
    "ABSENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRESENT",
        "ABSENT",
    )
)


def serialize_json(value: QueryResult) -> str:
    return value


def deserialize_json(data: str) -> QueryResult:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryResult value: {data!r}")
    return cast(QueryResult, data)
