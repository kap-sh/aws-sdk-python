"""Generated from Smithy shape ``com.amazonaws.quicksight#AnalysisErrorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AnalysisErrorType: TypeAlias = Literal[
    "ACCESS_DENIED",
    "SOURCE_NOT_FOUND",
    "DATA_SET_NOT_FOUND",
    "INTERNAL_FAILURE",
    "PARAMETER_VALUE_INCOMPATIBLE",
    "PARAMETER_TYPE_INVALID",
    "PARAMETER_NOT_FOUND",
    "COLUMN_TYPE_MISMATCH",
    "COLUMN_GEOGRAPHIC_ROLE_MISMATCH",
    "COLUMN_REPLACEMENT_MISSING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCESS_DENIED",
        "SOURCE_NOT_FOUND",
        "DATA_SET_NOT_FOUND",
        "INTERNAL_FAILURE",
        "PARAMETER_VALUE_INCOMPATIBLE",
        "PARAMETER_TYPE_INVALID",
        "PARAMETER_NOT_FOUND",
        "COLUMN_TYPE_MISMATCH",
        "COLUMN_GEOGRAPHIC_ROLE_MISMATCH",
        "COLUMN_REPLACEMENT_MISSING",
    )
)


def serialize_json(value: AnalysisErrorType) -> str:
    return value


def deserialize_json(data: str) -> AnalysisErrorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalysisErrorType value: {data!r}")
    return cast(AnalysisErrorType, data)
