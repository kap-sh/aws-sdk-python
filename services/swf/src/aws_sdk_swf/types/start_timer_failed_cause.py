"""Generated from Smithy shape ``com.amazonaws.swf#StartTimerFailedCause``."""

from typing import Literal, TypeAlias, cast

StartTimerFailedCause: TypeAlias = Literal[
    "TIMER_ID_ALREADY_IN_USE",
    "OPEN_TIMERS_LIMIT_EXCEEDED",
    "TIMER_CREATION_RATE_EXCEEDED",
    "OPERATION_NOT_PERMITTED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartTimerFailedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StartTimerFailedCause:
    return cast(StartTimerFailedCause, data)
