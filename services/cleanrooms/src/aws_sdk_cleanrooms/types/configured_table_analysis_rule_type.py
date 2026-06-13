"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAnalysisRuleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

ConfiguredTableAnalysisRuleType: TypeAlias = Literal[
    "AGGREGATION",
    "LIST",
    "CUSTOM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AGGREGATION",
        "LIST",
        "CUSTOM",
    )
)


def serialize_json(value: ConfiguredTableAnalysisRuleType) -> str:
    return value


def deserialize_json(data: str) -> ConfiguredTableAnalysisRuleType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ConfiguredTableAnalysisRuleType value: {data!r}"
        )
    return cast(ConfiguredTableAnalysisRuleType, data)
