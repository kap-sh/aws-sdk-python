"""Generated from Smithy shape ``com.amazonaws.swf#StartTimerFailedCause``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_swf.errors import DeserializationError

StartTimerFailedCause: TypeAlias = Literal[
    "TIMER_ID_ALREADY_IN_USE",
    "OPEN_TIMERS_LIMIT_EXCEEDED",
    "TIMER_CREATION_RATE_EXCEEDED",
    "OPERATION_NOT_PERMITTED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TIMER_ID_ALREADY_IN_USE",
        "OPEN_TIMERS_LIMIT_EXCEEDED",
        "TIMER_CREATION_RATE_EXCEEDED",
        "OPERATION_NOT_PERMITTED",
    )
)


def serialize_aws_json_1_0(value: StartTimerFailedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StartTimerFailedCause:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StartTimerFailedCause value: {data!r}")
    return cast(StartTimerFailedCause, data)
