"""Generated from Smithy shape ``com.amazonaws.batch#JobStateTimeLimitActionsState``."""

from typing import Literal, TypeAlias, cast

JobStateTimeLimitActionsState: TypeAlias = Literal["RUNNABLE",]


# --- restJson1 ser/de ---
def serialize_json(value: JobStateTimeLimitActionsState) -> str:
    return value


def deserialize_json(data: str) -> JobStateTimeLimitActionsState:
    return cast(JobStateTimeLimitActionsState, data)
