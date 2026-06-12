"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

AssessmentStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_json(value: AssessmentStatus) -> str:
    return value


def deserialize_json(data: str) -> AssessmentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssessmentStatus value: {data!r}")
    return cast(AssessmentStatus, data)
