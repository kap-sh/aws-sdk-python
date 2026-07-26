"""Generated from Smithy shape ``com.amazonaws.iotwireless#ServiceProfileList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.service_profile

ServiceProfileList: TypeAlias = list[
    "capo_iot_wireless.types.service_profile.ServiceProfile"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceProfileList) -> list:
    import capo_iot_wireless.types.service_profile

    out: list = []
    for item in value:
        out.append(capo_iot_wireless.types.service_profile.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceProfileList:
    import capo_iot_wireless.types.service_profile

    out: ServiceProfileList = []
    for item in data:
        out.append(capo_iot_wireless.types.service_profile.deserialize_json(item))
    return out
