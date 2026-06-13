"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisTemplateValidationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

AnalysisTemplateValidationStatus: TypeAlias = Literal[
    "VALID",
    "INVALID",
    "UNABLE_TO_VALIDATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VALID",
        "INVALID",
        "UNABLE_TO_VALIDATE",
    )
)


def serialize_json(value: AnalysisTemplateValidationStatus) -> str:
    return value


def deserialize_json(data: str) -> AnalysisTemplateValidationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AnalysisTemplateValidationStatus value: {data!r}"
        )
    return cast(AnalysisTemplateValidationStatus, data)
