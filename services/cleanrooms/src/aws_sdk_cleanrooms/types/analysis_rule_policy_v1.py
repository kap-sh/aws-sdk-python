"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisRulePolicyV1``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_rule_aggregation
    import aws_sdk_cleanrooms.types.analysis_rule_custom
    import aws_sdk_cleanrooms.types.analysis_rule_id_mapping_table
    import aws_sdk_cleanrooms.types.analysis_rule_list


class _AnalysisRulePolicyV1_list(TypedDict):
    list: "aws_sdk_cleanrooms.types.analysis_rule_list.AnalysisRuleList"


class _AnalysisRulePolicyV1_aggregation(TypedDict):
    aggregation: (
        "aws_sdk_cleanrooms.types.analysis_rule_aggregation.AnalysisRuleAggregation"
    )


class _AnalysisRulePolicyV1_custom(TypedDict):
    custom: "aws_sdk_cleanrooms.types.analysis_rule_custom.AnalysisRuleCustom"


class _AnalysisRulePolicyV1_idMappingTable(TypedDict):
    idMappingTable: "aws_sdk_cleanrooms.types.analysis_rule_id_mapping_table.AnalysisRuleIdMappingTable"


AnalysisRulePolicyV1: TypeAlias = (
    _AnalysisRulePolicyV1_list
    | _AnalysisRulePolicyV1_aggregation
    | _AnalysisRulePolicyV1_custom
    | _AnalysisRulePolicyV1_idMappingTable
)


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisRulePolicyV1) -> dict:
    if "list" in value:
        import aws_sdk_cleanrooms.types.analysis_rule_list

        return {
            "list": aws_sdk_cleanrooms.types.analysis_rule_list.serialize_json(
                value["list"]
            )
        }
    elif "aggregation" in value:
        import aws_sdk_cleanrooms.types.analysis_rule_aggregation

        return {
            "aggregation": aws_sdk_cleanrooms.types.analysis_rule_aggregation.serialize_json(
                value["aggregation"]
            )
        }
    elif "custom" in value:
        import aws_sdk_cleanrooms.types.analysis_rule_custom

        return {
            "custom": aws_sdk_cleanrooms.types.analysis_rule_custom.serialize_json(
                value["custom"]
            )
        }
    elif "idMappingTable" in value:
        import aws_sdk_cleanrooms.types.analysis_rule_id_mapping_table

        return {
            "idMappingTable": aws_sdk_cleanrooms.types.analysis_rule_id_mapping_table.serialize_json(
                value["idMappingTable"]
            )
        }
    else:
        raise SerializationError("AnalysisRulePolicyV1: no variant present")


def deserialize_json(data: dict) -> AnalysisRulePolicyV1:
    if "list" in data:
        import aws_sdk_cleanrooms.types.analysis_rule_list

        return {
            "list": aws_sdk_cleanrooms.types.analysis_rule_list.deserialize_json(
                data["list"]
            )
        }
    elif "aggregation" in data:
        import aws_sdk_cleanrooms.types.analysis_rule_aggregation

        return {
            "aggregation": aws_sdk_cleanrooms.types.analysis_rule_aggregation.deserialize_json(
                data["aggregation"]
            )
        }
    elif "custom" in data:
        import aws_sdk_cleanrooms.types.analysis_rule_custom

        return {
            "custom": aws_sdk_cleanrooms.types.analysis_rule_custom.deserialize_json(
                data["custom"]
            )
        }
    elif "idMappingTable" in data:
        import aws_sdk_cleanrooms.types.analysis_rule_id_mapping_table

        return {
            "idMappingTable": aws_sdk_cleanrooms.types.analysis_rule_id_mapping_table.deserialize_json(
                data["idMappingTable"]
            )
        }
    else:
        raise DeserializationError("AnalysisRulePolicyV1: no recognized variant key")
