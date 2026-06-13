"""Generated from Smithy shape ``com.amazonaws.quicksight#TableTotalsPlacement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TableTotalsPlacement: TypeAlias = Literal[
    "START",
    "END",
    "AUTO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "START",
        "END",
        "AUTO",
    )
)


def serialize_json(value: TableTotalsPlacement) -> str:
    return value


def deserialize_json(data: str) -> TableTotalsPlacement:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TableTotalsPlacement value: {data!r}")
    return cast(TableTotalsPlacement, data)
