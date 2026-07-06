"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAssociationAnalysisRulePolicyV1``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_aggregation
    import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_custom
    import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_list


class _ConfiguredTableAssociationAnalysisRulePolicyV1_list(TypedDict, closed=True):
    list: "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_list.ConfiguredTableAssociationAnalysisRuleList"


class _ConfiguredTableAssociationAnalysisRulePolicyV1_aggregation(
    TypedDict, closed=True
):
    aggregation: "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_aggregation.ConfiguredTableAssociationAnalysisRuleAggregation"


class _ConfiguredTableAssociationAnalysisRulePolicyV1_custom(TypedDict, closed=True):
    custom: "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_custom.ConfiguredTableAssociationAnalysisRuleCustom"


ConfiguredTableAssociationAnalysisRulePolicyV1: TypeAlias = (
    _ConfiguredTableAssociationAnalysisRulePolicyV1_list
    | _ConfiguredTableAssociationAnalysisRulePolicyV1_aggregation
    | _ConfiguredTableAssociationAnalysisRulePolicyV1_custom
)


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableAssociationAnalysisRulePolicyV1) -> dict:
    if "list" in value:
        import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_list

        return {
            "list": aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_list.serialize_json(
                value["list"]
            )
        }
    elif "aggregation" in value:
        import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_aggregation

        return {
            "aggregation": aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_aggregation.serialize_json(
                value["aggregation"]
            )
        }
    elif "custom" in value:
        import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_custom

        return {
            "custom": aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_custom.serialize_json(
                value["custom"]
            )
        }
    else:
        raise SerializationError(
            "ConfiguredTableAssociationAnalysisRulePolicyV1: no variant present"
        )


def deserialize_json(data: dict) -> ConfiguredTableAssociationAnalysisRulePolicyV1:
    if "list" in data:
        import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_list

        return {
            "list": aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_list.deserialize_json(
                data["list"]
            )
        }
    elif "aggregation" in data:
        import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_aggregation

        return {
            "aggregation": aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_aggregation.deserialize_json(
                data["aggregation"]
            )
        }
    elif "custom" in data:
        import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_custom

        return {
            "custom": aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_custom.deserialize_json(
                data["custom"]
            )
        }
    else:
        raise DeserializationError(
            "ConfiguredTableAssociationAnalysisRulePolicyV1: no recognized variant key"
        )
