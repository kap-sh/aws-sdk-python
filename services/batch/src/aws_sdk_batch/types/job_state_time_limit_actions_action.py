"""Generated from Smithy shape ``com.amazonaws.batch#JobStateTimeLimitActionsAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

JobStateTimeLimitActionsAction: TypeAlias = Literal[
    "CANCEL",
    "TERMINATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CANCEL",
        "TERMINATE",
    )
)


def serialize_json(value: JobStateTimeLimitActionsAction) -> str:
    return value


def deserialize_json(data: str) -> JobStateTimeLimitActionsAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown JobStateTimeLimitActionsAction value: {data!r}"
        )
    return cast(JobStateTimeLimitActionsAction, data)
