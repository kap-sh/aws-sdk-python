"""Generated from Smithy shape ``com.amazonaws.iotwireless#Applications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.application_config

Applications: TypeAlias = list[
    "capo_iot_wireless.types.application_config.ApplicationConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: Applications) -> list:
    import capo_iot_wireless.types.application_config

    out: list = []
    for item in value:
        out.append(capo_iot_wireless.types.application_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> Applications:
    import capo_iot_wireless.types.application_config

    out: Applications = []
    for item in data:
        out.append(capo_iot_wireless.types.application_config.deserialize_json(item))
    return out
