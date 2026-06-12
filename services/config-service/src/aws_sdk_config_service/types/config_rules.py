"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.config_rule

ConfigRules: TypeAlias = list["aws_sdk_config_service.types.config_rule.ConfigRule"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigRules) -> list:
    import aws_sdk_config_service.types.config_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.config_rule.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConfigRules:
    import aws_sdk_config_service.types.config_rule

    out: ConfigRules = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.config_rule.deserialize_aws_json_1_1(item)
        )
    return out
