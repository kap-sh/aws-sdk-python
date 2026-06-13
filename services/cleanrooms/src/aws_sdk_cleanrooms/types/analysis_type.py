"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

AnalysisType: TypeAlias = Literal[
    "DIRECT_ANALYSIS",
    "ADDITIONAL_ANALYSIS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DIRECT_ANALYSIS",
        "ADDITIONAL_ANALYSIS",
    )
)


def serialize_json(value: AnalysisType) -> str:
    return value


def deserialize_json(data: str) -> AnalysisType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalysisType value: {data!r}")
    return cast(AnalysisType, data)
