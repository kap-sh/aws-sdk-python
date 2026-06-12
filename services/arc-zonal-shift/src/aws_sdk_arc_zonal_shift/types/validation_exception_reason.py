"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_zonal_shift.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "InvalidExpiresIn",
    "InvalidStatus",
    "MissingValue",
    "InvalidToken",
    "InvalidResourceIdentifier",
    "InvalidAz",
    "UnsupportedAz",
    "InvalidAlarmCondition",
    "InvalidConditionType",
    "InvalidPracticeBlocker",
    "FISExperimentUpdateNotAllowed",
    "AutoshiftUpdateNotAllowed",
    "UnsupportedPracticeCancelShiftType",
    "InvalidPracticeAllowedWindow",
    "InvalidPracticeWindows",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InvalidExpiresIn",
        "InvalidStatus",
        "MissingValue",
        "InvalidToken",
        "InvalidResourceIdentifier",
        "InvalidAz",
        "UnsupportedAz",
        "InvalidAlarmCondition",
        "InvalidConditionType",
        "InvalidPracticeBlocker",
        "FISExperimentUpdateNotAllowed",
        "AutoshiftUpdateNotAllowed",
        "UnsupportedPracticeCancelShiftType",
        "InvalidPracticeAllowedWindow",
        "InvalidPracticeWindows",
    )
)


def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
