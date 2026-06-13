"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisRuleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

AnalysisRuleType: TypeAlias = Literal[
    "AGGREGATION",
    "LIST",
    "CUSTOM",
    "ID_MAPPING_TABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AGGREGATION",
        "LIST",
        "CUSTOM",
        "ID_MAPPING_TABLE",
    )
)


def serialize_json(value: AnalysisRuleType) -> str:
    return value


def deserialize_json(data: str) -> AnalysisRuleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalysisRuleType value: {data!r}")
    return cast(AnalysisRuleType, data)
