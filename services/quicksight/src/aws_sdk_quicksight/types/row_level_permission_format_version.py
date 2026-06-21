"""Generated from Smithy shape ``com.amazonaws.quicksight#RowLevelPermissionFormatVersion``."""

from typing import Literal, TypeAlias, cast

RowLevelPermissionFormatVersion: TypeAlias = Literal[
    "VERSION_1",
    "VERSION_2",
]


# --- restJson1 ser/de ---
def serialize_json(value: RowLevelPermissionFormatVersion) -> str:
    return value


def deserialize_json(data: str) -> RowLevelPermissionFormatVersion:
    return cast(RowLevelPermissionFormatVersion, data)
