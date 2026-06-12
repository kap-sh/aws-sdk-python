"""Generated from Smithy shape ``com.amazonaws.batch#JobStateTimeLimitActionsState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

JobStateTimeLimitActionsState: TypeAlias = Literal["RUNNABLE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("RUNNABLE",))


def serialize_json(value: JobStateTimeLimitActionsState) -> str:
    return value


def deserialize_json(data: str) -> JobStateTimeLimitActionsState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown JobStateTimeLimitActionsState value: {data!r}"
        )
    return cast(JobStateTimeLimitActionsState, data)
