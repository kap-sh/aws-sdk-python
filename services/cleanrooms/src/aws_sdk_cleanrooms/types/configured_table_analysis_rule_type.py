"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAnalysisRuleType``."""

from typing import Literal, TypeAlias, cast

ConfiguredTableAnalysisRuleType: TypeAlias = Literal[
    "AGGREGATION",
    "LIST",
    "CUSTOM",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableAnalysisRuleType) -> str:
    return value


def deserialize_json(data: str) -> ConfiguredTableAnalysisRuleType:
    return cast(ConfiguredTableAnalysisRuleType, data)
