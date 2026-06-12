"""Generated from Smithy shape ``com.amazonaws.swf#CancelTimerFailedCause``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_swf.errors import DeserializationError

CancelTimerFailedCause: TypeAlias = Literal[
    "TIMER_ID_UNKNOWN",
    "OPERATION_NOT_PERMITTED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TIMER_ID_UNKNOWN",
        "OPERATION_NOT_PERMITTED",
    )
)


def serialize_aws_json_1_0(value: CancelTimerFailedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CancelTimerFailedCause:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CancelTimerFailedCause value: {data!r}")
    return cast(CancelTimerFailedCause, data)
