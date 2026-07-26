"""Generated from Smithy shape ``com.amazonaws.iotevents#EmailConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_events.types.email_configuration

EmailConfigurations: TypeAlias = list[
    "capo_iot_events.types.email_configuration.EmailConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: EmailConfigurations) -> list:
    import capo_iot_events.types.email_configuration

    out: list = []
    for item in value:
        out.append(capo_iot_events.types.email_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> EmailConfigurations:
    import capo_iot_events.types.email_configuration

    out: EmailConfigurations = []
    for item in data:
        out.append(capo_iot_events.types.email_configuration.deserialize_json(item))
    return out
