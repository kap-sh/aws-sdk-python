"""Generated from Smithy shape ``com.amazonaws.osis#ChangeProgressStatuses``."""

from typing import Literal, TypeAlias, cast

ChangeProgressStatuses: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeProgressStatuses) -> str:
    return value


def deserialize_json(data: str) -> ChangeProgressStatuses:
    return cast(ChangeProgressStatuses, data)
