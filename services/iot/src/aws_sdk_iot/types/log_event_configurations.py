"""Generated from Smithy shape ``com.amazonaws.iot#LogEventConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.log_event_configuration

LogEventConfigurations: TypeAlias = list[
    "aws_sdk_iot.types.log_event_configuration.LogEventConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: LogEventConfigurations) -> list:
    import aws_sdk_iot.types.log_event_configuration

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.log_event_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> LogEventConfigurations:
    import aws_sdk_iot.types.log_event_configuration

    out: LogEventConfigurations = []
    for item in data:
        out.append(aws_sdk_iot.types.log_event_configuration.deserialize_json(item))
    return out
