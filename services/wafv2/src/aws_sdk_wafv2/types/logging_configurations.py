"""Generated from Smithy shape ``com.amazonaws.wafv2#LoggingConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.logging_configuration

LoggingConfigurations: TypeAlias = list[
    "aws_sdk_wafv2.types.logging_configuration.LoggingConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoggingConfigurations) -> list:
    import aws_sdk_wafv2.types.logging_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_wafv2.types.logging_configuration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LoggingConfigurations:
    import aws_sdk_wafv2.types.logging_configuration

    out: LoggingConfigurations = []
    for item in data:
        out.append(
            aws_sdk_wafv2.types.logging_configuration.deserialize_aws_json_1_1(item)
        )
    return out
