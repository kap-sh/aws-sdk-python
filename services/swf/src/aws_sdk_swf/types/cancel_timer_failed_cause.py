"""Generated from Smithy shape ``com.amazonaws.swf#CancelTimerFailedCause``."""

from typing import Literal, TypeAlias, cast

CancelTimerFailedCause: TypeAlias = Literal[
    "TIMER_ID_UNKNOWN",
    "OPERATION_NOT_PERMITTED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelTimerFailedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CancelTimerFailedCause:
    return cast(CancelTimerFailedCause, data)
