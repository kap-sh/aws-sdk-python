"""Generated from Smithy shape ``com.amazonaws.iotevents#SMSConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.sms_configuration

SMSConfigurations: TypeAlias = list[
    "aws_sdk_iot_events.types.sms_configuration.SMSConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: SMSConfigurations) -> list:
    import aws_sdk_iot_events.types.sms_configuration

    out: list = []
    for item in value:
        out.append(aws_sdk_iot_events.types.sms_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> SMSConfigurations:
    import aws_sdk_iot_events.types.sms_configuration

    out: SMSConfigurations = []
    for item in data:
        out.append(aws_sdk_iot_events.types.sms_configuration.deserialize_json(item))
    return out
