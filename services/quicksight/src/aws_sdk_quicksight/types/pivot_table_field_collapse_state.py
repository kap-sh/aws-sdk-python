"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableFieldCollapseState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

PivotTableFieldCollapseState: TypeAlias = Literal[
    "COLLAPSED",
    "EXPANDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COLLAPSED",
        "EXPANDED",
    )
)


def serialize_json(value: PivotTableFieldCollapseState) -> str:
    return value


def deserialize_json(data: str) -> PivotTableFieldCollapseState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PivotTableFieldCollapseState value: {data!r}"
        )
    return cast(PivotTableFieldCollapseState, data)
