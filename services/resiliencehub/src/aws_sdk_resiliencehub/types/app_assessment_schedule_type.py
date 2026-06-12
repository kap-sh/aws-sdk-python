"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppAssessmentScheduleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

AppAssessmentScheduleType: TypeAlias = Literal[
    "Disabled",
    "Daily",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Disabled",
        "Daily",
    )
)


def serialize_json(value: AppAssessmentScheduleType) -> str:
    return value


def deserialize_json(data: str) -> AppAssessmentScheduleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AppAssessmentScheduleType value: {data!r}")
    return cast(AppAssessmentScheduleType, data)
