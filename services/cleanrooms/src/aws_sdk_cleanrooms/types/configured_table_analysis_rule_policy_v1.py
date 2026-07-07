"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAnalysisRulePolicyV1``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_rule_aggregation
    import aws_sdk_cleanrooms.types.analysis_rule_custom
    import aws_sdk_cleanrooms.types.analysis_rule_list


class _ConfiguredTableAnalysisRulePolicyV1_list(TypedDict, closed=True):
    list: "aws_sdk_cleanrooms.types.analysis_rule_list.AnalysisRuleList"


class _ConfiguredTableAnalysisRulePolicyV1_aggregation(TypedDict, closed=True):
    aggregation: (
        "aws_sdk_cleanrooms.types.analysis_rule_aggregation.AnalysisRuleAggregation"
    )


class _ConfiguredTableAnalysisRulePolicyV1_custom(TypedDict, closed=True):
    custom: "aws_sdk_cleanrooms.types.analysis_rule_custom.AnalysisRuleCustom"


ConfiguredTableAnalysisRulePolicyV1: TypeAlias = (
    _ConfiguredTableAnalysisRulePolicyV1_list
    | _ConfiguredTableAnalysisRulePolicyV1_aggregation
    | _ConfiguredTableAnalysisRulePolicyV1_custom
)


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableAnalysisRulePolicyV1) -> dict:
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
    else:
        raise SerializationError(
            "ConfiguredTableAnalysisRulePolicyV1: no variant present"
        )


def deserialize_json(data: dict) -> ConfiguredTableAnalysisRulePolicyV1:
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
    else:
        raise DeserializationError(
            "ConfiguredTableAnalysisRulePolicyV1: no recognized variant key"
        )
