"""Generated from Smithy shape ``com.amazonaws.batch#JobStateTimeLimitActionsAction``."""

from typing import Literal, TypeAlias, cast

JobStateTimeLimitActionsAction: TypeAlias = Literal[
    "CANCEL",
    "TERMINATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobStateTimeLimitActionsAction) -> str:
    return value


def deserialize_json(data: str) -> JobStateTimeLimitActionsAction:
    return cast(JobStateTimeLimitActionsAction, data)
