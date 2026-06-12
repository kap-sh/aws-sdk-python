"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AssessmentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

AssessmentStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Failed",
    "Success",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "InProgress",
        "Failed",
        "Success",
    )
)


def serialize_json(value: AssessmentStatus) -> str:
    return value


def deserialize_json(data: str) -> AssessmentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssessmentStatus value: {data!r}")
    return cast(AssessmentStatus, data)
