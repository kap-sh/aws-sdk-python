"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigRuleEvaluationStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.config_rule_evaluation_status

ConfigRuleEvaluationStatusList: TypeAlias = list[
    "capo_config_service.types.config_rule_evaluation_status.ConfigRuleEvaluationStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigRuleEvaluationStatusList) -> list:
    import capo_config_service.types.config_rule_evaluation_status

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.config_rule_evaluation_status.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConfigRuleEvaluationStatusList:
    import capo_config_service.types.config_rule_evaluation_status

    out: ConfigRuleEvaluationStatusList = []
    for item in data:
        out.append(
            capo_config_service.types.config_rule_evaluation_status.deserialize_aws_json_1_1(
                item
            )
        )
    return out
