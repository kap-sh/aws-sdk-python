"""Generated from Smithy shape ``com.amazonaws.wafregional#LoggingConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf_regional.types.logging_configuration

LoggingConfigurations: TypeAlias = list[
    "capo_waf_regional.types.logging_configuration.LoggingConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoggingConfigurations) -> list:
    import capo_waf_regional.types.logging_configuration

    out: list = []
    for item in value:
        out.append(
            capo_waf_regional.types.logging_configuration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LoggingConfigurations:
    import capo_waf_regional.types.logging_configuration

    out: LoggingConfigurations = []
    for item in data:
        out.append(
            capo_waf_regional.types.logging_configuration.deserialize_aws_json_1_1(item)
        )
    return out
