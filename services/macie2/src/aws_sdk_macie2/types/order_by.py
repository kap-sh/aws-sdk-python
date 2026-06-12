"""Generated from Smithy shape ``com.amazonaws.macie2#OrderBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

OrderBy: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASC",
        "DESC",
    )
)


def serialize_json(value: OrderBy) -> str:
    return value


def deserialize_json(data: str) -> OrderBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrderBy value: {data!r}")
    return cast(OrderBy, data)
