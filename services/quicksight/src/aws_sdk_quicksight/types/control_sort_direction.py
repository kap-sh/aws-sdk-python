"""Generated from Smithy shape ``com.amazonaws.quicksight#ControlSortDirection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ControlSortDirection: TypeAlias = Literal[
    "ASC",
    "DESC",
    "USER_DEFINED_ORDER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASC",
        "DESC",
        "USER_DEFINED_ORDER",
    )
)


def serialize_json(value: ControlSortDirection) -> str:
    return value


def deserialize_json(data: str) -> ControlSortDirection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ControlSortDirection value: {data!r}")
    return cast(ControlSortDirection, data)
