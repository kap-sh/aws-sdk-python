"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardUIState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DashboardUIState: TypeAlias = Literal[
    "EXPANDED",
    "COLLAPSED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXPANDED",
        "COLLAPSED",
    )
)


def serialize_json(value: DashboardUIState) -> str:
    return value


def deserialize_json(data: str) -> DashboardUIState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DashboardUIState value: {data!r}")
    return cast(DashboardUIState, data)
