"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAssociationAnalysisRuleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

ConfiguredTableAssociationAnalysisRuleType: TypeAlias = Literal[
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


def serialize_json(value: ConfiguredTableAssociationAnalysisRuleType) -> str:
    return value


def deserialize_json(data: str) -> ConfiguredTableAssociationAnalysisRuleType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ConfiguredTableAssociationAnalysisRuleType value: {data!r}"
        )
    return cast(ConfiguredTableAssociationAnalysisRuleType, data)
