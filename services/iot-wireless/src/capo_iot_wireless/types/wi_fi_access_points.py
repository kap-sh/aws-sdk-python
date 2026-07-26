"""Generated from Smithy shape ``com.amazonaws.iotwireless#WiFiAccessPoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.wi_fi_access_point

WiFiAccessPoints: TypeAlias = list[
    "capo_iot_wireless.types.wi_fi_access_point.WiFiAccessPoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: WiFiAccessPoints) -> list:
    import capo_iot_wireless.types.wi_fi_access_point

    out: list = []
    for item in value:
        out.append(capo_iot_wireless.types.wi_fi_access_point.serialize_json(item))
    return out


def deserialize_json(data: list) -> WiFiAccessPoints:
    import capo_iot_wireless.types.wi_fi_access_point

    out: WiFiAccessPoints = []
    for item in data:
        out.append(capo_iot_wireless.types.wi_fi_access_point.deserialize_json(item))
    return out
