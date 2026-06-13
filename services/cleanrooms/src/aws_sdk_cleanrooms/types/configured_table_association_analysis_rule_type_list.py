"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAssociationAnalysisRuleTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type

ConfiguredTableAssociationAnalysisRuleTypeList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableAssociationAnalysisRuleTypeList) -> list:
    import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConfiguredTableAssociationAnalysisRuleTypeList:
    import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type

    out: ConfiguredTableAssociationAnalysisRuleTypeList = []
    for item in data:
        out.append(
            aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type.deserialize_json(
                item
            )
        )
    return out
