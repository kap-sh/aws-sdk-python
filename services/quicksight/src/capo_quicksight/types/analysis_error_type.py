"""Generated from Smithy shape ``com.amazonaws.quicksight#AnalysisErrorType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: AnalysisErrorType) -> str:
    return value


def deserialize_json(data: str) -> AnalysisErrorType:
    return cast(AnalysisErrorType, data)
