"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)
