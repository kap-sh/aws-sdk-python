"""Generated from Smithy shape ``com.amazonaws.ivschat#LoggingConfigurationIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivschat.types.logging_configuration_identifier

LoggingConfigurationIdentifierList: TypeAlias = list[
    "aws_sdk_ivschat.types.logging_configuration_identifier.LoggingConfigurationIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: LoggingConfigurationIdentifierList) -> list:
    return list(value)


def deserialize_json(data: list) -> LoggingConfigurationIdentifierList:
    return list(data)
