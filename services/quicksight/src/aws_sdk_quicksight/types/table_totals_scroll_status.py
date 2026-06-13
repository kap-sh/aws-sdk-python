"""Generated from Smithy shape ``com.amazonaws.quicksight#TableTotalsScrollStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TableTotalsScrollStatus: TypeAlias = Literal[
    "PINNED",
    "SCROLLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PINNED",
        "SCROLLED",
    )
)


def serialize_json(value: TableTotalsScrollStatus) -> str:
    return value


def deserialize_json(data: str) -> TableTotalsScrollStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TableTotalsScrollStatus value: {data!r}")
    return cast(TableTotalsScrollStatus, data)
