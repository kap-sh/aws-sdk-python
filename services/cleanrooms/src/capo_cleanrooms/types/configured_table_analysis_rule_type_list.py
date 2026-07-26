"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAnalysisRuleTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.configured_table_analysis_rule_type

ConfiguredTableAnalysisRuleTypeList: TypeAlias = list[
    "capo_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableAnalysisRuleTypeList) -> list:
    import capo_cleanrooms.types.configured_table_analysis_rule_type

    out: list = []
    for item in value:
        out.append(
            capo_cleanrooms.types.configured_table_analysis_rule_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConfiguredTableAnalysisRuleTypeList:
    import capo_cleanrooms.types.configured_table_analysis_rule_type

    out: ConfiguredTableAnalysisRuleTypeList = []
    for item in data:
        out.append(
            capo_cleanrooms.types.configured_table_analysis_rule_type.deserialize_json(
                item
            )
        )
    return out
