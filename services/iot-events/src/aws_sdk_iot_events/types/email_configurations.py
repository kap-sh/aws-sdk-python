"""Generated from Smithy shape ``com.amazonaws.iotevents#EmailConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.email_configuration

EmailConfigurations: TypeAlias = list[
    "aws_sdk_iot_events.types.email_configuration.EmailConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: EmailConfigurations) -> list:
    import aws_sdk_iot_events.types.email_configuration

    out: list = []
    for item in value:
        out.append(aws_sdk_iot_events.types.email_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> EmailConfigurations:
    import aws_sdk_iot_events.types.email_configuration

    out: EmailConfigurations = []
    for item in data:
        out.append(aws_sdk_iot_events.types.email_configuration.deserialize_json(item))
    return out
