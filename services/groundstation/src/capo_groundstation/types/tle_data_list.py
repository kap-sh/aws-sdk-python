"""Generated from Smithy shape ``com.amazonaws.groundstation#TLEDataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_groundstation.types.tle_data

TLEDataList: TypeAlias = list["capo_groundstation.types.tle_data.TLEData"]


# --- restJson1 ser/de ---
def serialize_json(value: TLEDataList) -> list:
    import capo_groundstation.types.tle_data

    out: list = []
    for item in value:
        out.append(capo_groundstation.types.tle_data.serialize_json(item))
    return out


def deserialize_json(data: list) -> TLEDataList:
    import capo_groundstation.types.tle_data

    out: TLEDataList = []
    for item in data:
        out.append(capo_groundstation.types.tle_data.deserialize_json(item))
    return out
