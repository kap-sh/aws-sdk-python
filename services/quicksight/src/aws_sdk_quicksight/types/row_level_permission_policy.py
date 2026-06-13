"""Generated from Smithy shape ``com.amazonaws.quicksight#RowLevelPermissionPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

RowLevelPermissionPolicy: TypeAlias = Literal[
    "GRANT_ACCESS",
    "DENY_ACCESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GRANT_ACCESS",
        "DENY_ACCESS",
    )
)


def serialize_json(value: RowLevelPermissionPolicy) -> str:
    return value


def deserialize_json(data: str) -> RowLevelPermissionPolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RowLevelPermissionPolicy value: {data!r}")
    return cast(RowLevelPermissionPolicy, data)
