"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

AnalysisMethod: TypeAlias = Literal[
    "DIRECT_QUERY",
    "DIRECT_JOB",
    "MULTIPLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DIRECT_QUERY",
        "DIRECT_JOB",
        "MULTIPLE",
    )
)


def serialize_json(value: AnalysisMethod) -> str:
    return value


def deserialize_json(data: str) -> AnalysisMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalysisMethod value: {data!r}")
    return cast(AnalysisMethod, data)
