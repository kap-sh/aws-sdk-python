"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotFileSheetSelectionScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SnapshotFileSheetSelectionScope: TypeAlias = Literal[
    "ALL_VISUALS",
    "SELECTED_VISUALS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL_VISUALS",
        "SELECTED_VISUALS",
    )
)


def serialize_json(value: SnapshotFileSheetSelectionScope) -> str:
    return value


def deserialize_json(data: str) -> SnapshotFileSheetSelectionScope:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SnapshotFileSheetSelectionScope value: {data!r}"
        )
    return cast(SnapshotFileSheetSelectionScope, data)
