"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeStreamStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connecthealth.errors import DeserializationError

MedicalScribeStreamStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "PAUSED",
    "FAILED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "PAUSED",
        "FAILED",
        "COMPLETED",
    )
)


def serialize_json(value: MedicalScribeStreamStatus) -> str:
    return value


def deserialize_json(data: str) -> MedicalScribeStreamStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MedicalScribeStreamStatus value: {data!r}")
    return cast(MedicalScribeStreamStatus, data)
