"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

AnalysisFormat: TypeAlias = Literal[
    "SQL",
    "PYSPARK_1_0",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SQL",
        "PYSPARK_1_0",
    )
)


def serialize_json(value: AnalysisFormat) -> str:
    return value


def deserialize_json(data: str) -> AnalysisFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalysisFormat value: {data!r}")
    return cast(AnalysisFormat, data)
