"""Generated from Smithy shape ``com.amazonaws.medicalimaging#SortField``."""

from typing import Literal, TypeAlias, cast

SortField: TypeAlias = Literal[
    "updatedAt",
    "createdAt",
    "DICOMStudyDateAndTime",
]


# --- restJson1 ser/de ---
def serialize_json(value: SortField) -> str:
    return value


def deserialize_json(data: str) -> SortField:
    return cast(SortField, data)
