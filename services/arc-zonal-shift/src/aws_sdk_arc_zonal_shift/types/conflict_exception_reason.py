"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ConflictExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_zonal_shift.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: ConflictExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ConflictExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConflictExceptionReason value: {data!r}")
    return cast(ConflictExceptionReason, data)
