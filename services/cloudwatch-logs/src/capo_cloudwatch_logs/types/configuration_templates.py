"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ConfigurationTemplates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.configuration_template

ConfigurationTemplates: TypeAlias = list[
    "capo_cloudwatch_logs.types.configuration_template.ConfigurationTemplate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationTemplates) -> list:
    import capo_cloudwatch_logs.types.configuration_template

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.configuration_template.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConfigurationTemplates:
    import capo_cloudwatch_logs.types.configuration_template

    out: ConfigurationTemplates = []
    for item in data:
        out.append(
            capo_cloudwatch_logs.types.configuration_template.deserialize_aws_json_1_1(
                item
            )
        )
    return out
