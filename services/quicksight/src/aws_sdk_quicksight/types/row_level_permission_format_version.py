"""Generated from Smithy shape ``com.amazonaws.quicksight#RowLevelPermissionFormatVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

RowLevelPermissionFormatVersion: TypeAlias = Literal[
    "VERSION_1",
    "VERSION_2",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VERSION_1",
        "VERSION_2",
    )
)


def serialize_json(value: RowLevelPermissionFormatVersion) -> str:
    return value


def deserialize_json(data: str) -> RowLevelPermissionFormatVersion:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RowLevelPermissionFormatVersion value: {data!r}"
        )
    return cast(RowLevelPermissionFormatVersion, data)
