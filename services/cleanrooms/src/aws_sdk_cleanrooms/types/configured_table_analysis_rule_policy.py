"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAnalysisRulePolicy``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_table_analysis_rule_policy_v1


class _ConfiguredTableAnalysisRulePolicy_v1(TypedDict, closed=True):
    v1: "aws_sdk_cleanrooms.types.configured_table_analysis_rule_policy_v1.ConfiguredTableAnalysisRulePolicyV1"


ConfiguredTableAnalysisRulePolicy: TypeAlias = _ConfiguredTableAnalysisRulePolicy_v1


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableAnalysisRulePolicy) -> dict:
    if "v1" in value:
        import aws_sdk_cleanrooms.types.configured_table_analysis_rule_policy_v1

        return {
            "v1": aws_sdk_cleanrooms.types.configured_table_analysis_rule_policy_v1.serialize_json(
                value["v1"]
            )
        }
    else:
        raise SerializationError(
            "ConfiguredTableAnalysisRulePolicy: no variant present"
        )


def deserialize_json(data: dict) -> ConfiguredTableAnalysisRulePolicy:
    if "v1" in data:
        import aws_sdk_cleanrooms.types.configured_table_analysis_rule_policy_v1

        return {
            "v1": aws_sdk_cleanrooms.types.configured_table_analysis_rule_policy_v1.deserialize_json(
                data["v1"]
            )
        }
    else:
        raise DeserializationError(
            "ConfiguredTableAnalysisRulePolicy: no recognized variant key"
        )
