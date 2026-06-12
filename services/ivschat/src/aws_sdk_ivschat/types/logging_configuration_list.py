"""Generated from Smithy shape ``com.amazonaws.ivschat#LoggingConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivschat.types.logging_configuration_summary

LoggingConfigurationList: TypeAlias = list[
    "aws_sdk_ivschat.types.logging_configuration_summary.LoggingConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: LoggingConfigurationList) -> list:
    import aws_sdk_ivschat.types.logging_configuration_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ivschat.types.logging_configuration_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> LoggingConfigurationList:
    import aws_sdk_ivschat.types.logging_configuration_summary

    out: LoggingConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_ivschat.types.logging_configuration_summary.deserialize_json(item)
        )
    return out
