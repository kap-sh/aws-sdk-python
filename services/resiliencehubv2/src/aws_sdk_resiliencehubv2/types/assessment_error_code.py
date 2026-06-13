"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AssessmentErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

AssessmentErrorCode: TypeAlias = Literal[
    "INVALID_PERMISSIONS",
    "CMK_ACCESS_DENIED",
    "AGENT_ERROR",
    "INTERNAL_ERROR",
    "DESIGN_FILE_ACCESS_DENIED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVALID_PERMISSIONS",
        "CMK_ACCESS_DENIED",
        "AGENT_ERROR",
        "INTERNAL_ERROR",
        "DESIGN_FILE_ACCESS_DENIED",
    )
)


def serialize_json(value: AssessmentErrorCode) -> str:
    return value


def deserialize_json(data: str) -> AssessmentErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssessmentErrorCode value: {data!r}")
    return cast(AssessmentErrorCode, data)
