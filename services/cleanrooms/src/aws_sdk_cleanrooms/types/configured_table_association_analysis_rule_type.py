"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAssociationAnalysisRuleType``."""

from typing import Literal, TypeAlias, cast

ConfiguredTableAssociationAnalysisRuleType: TypeAlias = Literal[
    "AGGREGATION",
    "LIST",
    "CUSTOM",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableAssociationAnalysisRuleType) -> str:
    return value


def deserialize_json(data: str) -> ConfiguredTableAssociationAnalysisRuleType:
    return cast(ConfiguredTableAssociationAnalysisRuleType, data)
