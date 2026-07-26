"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.config_rule

ConfigRules: TypeAlias = list["capo_config_service.types.config_rule.ConfigRule"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigRules) -> list:
    import capo_config_service.types.config_rule

    out: list = []
    for item in value:
        out.append(capo_config_service.types.config_rule.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ConfigRules:
    import capo_config_service.types.config_rule

    out: ConfigRules = []
    for item in data:
        out.append(capo_config_service.types.config_rule.deserialize_aws_json_1_1(item))
    return out
