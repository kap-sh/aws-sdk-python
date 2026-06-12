"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#AnalysisType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeguru_reviewer.errors import DeserializationError

AnalysisType: TypeAlias = Literal[
    "Security",
    "CodeQuality",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Security",
        "CodeQuality",
    )
)


def serialize_json(value: AnalysisType) -> str:
    return value


def deserialize_json(data: str) -> AnalysisType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalysisType value: {data!r}")
    return cast(AnalysisType, data)
