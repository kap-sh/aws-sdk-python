"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAnalysisRuleTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_table_analysis_rule_type

ConfiguredTableAnalysisRuleTypeList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableAnalysisRuleTypeList) -> list:
    import aws_sdk_cleanrooms.types.configured_table_analysis_rule_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanrooms.types.configured_table_analysis_rule_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConfiguredTableAnalysisRuleTypeList:
    import aws_sdk_cleanrooms.types.configured_table_analysis_rule_type

    out: ConfiguredTableAnalysisRuleTypeList = []
    for item in data:
        out.append(
            aws_sdk_cleanrooms.types.configured_table_analysis_rule_type.deserialize_json(
                item
            )
        )
    return out
