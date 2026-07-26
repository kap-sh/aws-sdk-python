"""Generated from Smithy shape ``com.amazonaws.osis#ChangeProgressStageStatuses``."""

from typing import Literal, TypeAlias, cast

ChangeProgressStageStatuses: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeProgressStageStatuses) -> str:
    return value


def deserialize_json(data: str) -> ChangeProgressStageStatuses:
    return cast(ChangeProgressStageStatuses, data)
