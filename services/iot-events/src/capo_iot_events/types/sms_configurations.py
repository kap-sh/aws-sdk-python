"""Generated from Smithy shape ``com.amazonaws.iotevents#SMSConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_events.types.sms_configuration

SMSConfigurations: TypeAlias = list[
    "capo_iot_events.types.sms_configuration.SMSConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: SMSConfigurations) -> list:
    import capo_iot_events.types.sms_configuration

    out: list = []
    for item in value:
        out.append(capo_iot_events.types.sms_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> SMSConfigurations:
    import capo_iot_events.types.sms_configuration

    out: SMSConfigurations = []
    for item in data:
        out.append(capo_iot_events.types.sms_configuration.deserialize_json(item))
    return out
