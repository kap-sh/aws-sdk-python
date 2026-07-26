"""Generated from Smithy shape ``com.amazonaws.location#WiFiAccessPointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.wi_fi_access_point

WiFiAccessPointList: TypeAlias = list[
    "capo_location.types.wi_fi_access_point.WiFiAccessPoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: WiFiAccessPointList) -> list:
    import capo_location.types.wi_fi_access_point

    out: list = []
    for item in value:
        out.append(capo_location.types.wi_fi_access_point.serialize_json(item))
    return out


def deserialize_json(data: list) -> WiFiAccessPointList:
    import capo_location.types.wi_fi_access_point

    out: WiFiAccessPointList = []
    for item in data:
        out.append(capo_location.types.wi_fi_access_point.deserialize_json(item))
    return out
