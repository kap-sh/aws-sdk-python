"""Generated from Smithy shape ``com.amazonaws.medicalimaging#SortField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medical_imaging.errors import DeserializationError

SortField: TypeAlias = Literal[
    "updatedAt",
    "createdAt",
    "DICOMStudyDateAndTime",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "updatedAt",
        "createdAt",
        "DICOMStudyDateAndTime",
    )
)


def serialize_json(value: SortField) -> str:
    return value


def deserialize_json(data: str) -> SortField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortField value: {data!r}")
    return cast(SortField, data)
