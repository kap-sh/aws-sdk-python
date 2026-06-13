"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAssociationAnalysisRulePolicy``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy_v1


class _ConfiguredTableAssociationAnalysisRulePolicy_v1(TypedDict):
    v1: "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy_v1.ConfiguredTableAssociationAnalysisRulePolicyV1"


ConfiguredTableAssociationAnalysisRulePolicy: TypeAlias = (
    _ConfiguredTableAssociationAnalysisRulePolicy_v1
)


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableAssociationAnalysisRulePolicy) -> dict:
    if "v1" in value:
        import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy_v1

        return {
            "v1": aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy_v1.serialize_json(
                value["v1"]
            )
        }
    else:
        raise SerializationError(
            "ConfiguredTableAssociationAnalysisRulePolicy: no variant present"
        )


def deserialize_json(data: dict) -> ConfiguredTableAssociationAnalysisRulePolicy:
    if "v1" in data:
        import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy_v1

        return {
            "v1": aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy_v1.deserialize_json(
                data["v1"]
            )
        }
    else:
        raise DeserializationError(
            "ConfiguredTableAssociationAnalysisRulePolicy: no recognized variant key"
        )
