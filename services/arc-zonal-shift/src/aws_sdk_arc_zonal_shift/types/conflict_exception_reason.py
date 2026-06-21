"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ConflictExceptionReason``."""

from typing import Literal, TypeAlias, cast

ConflictExceptionReason: TypeAlias = Literal[
    "ZonalShiftAlreadyExists",
    "ZonalShiftStatusNotActive",
    "SimultaneousZonalShiftsConflict",
    "PracticeConfigurationAlreadyExists",
    "AutoShiftEnabled",
    "PracticeConfigurationDoesNotExist",
    "ZonalAutoshiftActive",
    "PracticeOutcomeAlarmsRed",
    "PracticeBlockingAlarmsRed",
    "PracticeInBlockedDates",
    "PracticeInBlockedWindows",
    "PracticeOutsideAllowedWindows",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConflictExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ConflictExceptionReason:
    return cast(ConflictExceptionReason, data)
