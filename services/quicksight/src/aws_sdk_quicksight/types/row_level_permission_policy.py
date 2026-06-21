"""Generated from Smithy shape ``com.amazonaws.quicksight#RowLevelPermissionPolicy``."""

from typing import Literal, TypeAlias, cast

RowLevelPermissionPolicy: TypeAlias = Literal[
    "GRANT_ACCESS",
    "DENY_ACCESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: RowLevelPermissionPolicy) -> str:
    return value


def deserialize_json(data: str) -> RowLevelPermissionPolicy:
    return cast(RowLevelPermissionPolicy, data)
