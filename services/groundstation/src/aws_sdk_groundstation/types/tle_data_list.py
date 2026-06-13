"""Generated from Smithy shape ``com.amazonaws.groundstation#TLEDataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.tle_data

TLEDataList: TypeAlias = list["aws_sdk_groundstation.types.tle_data.TLEData"]


# --- restJson1 ser/de ---
def serialize_json(value: TLEDataList) -> list:
    import aws_sdk_groundstation.types.tle_data

    out: list = []
    for item in value:
        out.append(aws_sdk_groundstation.types.tle_data.serialize_json(item))
    return out


def deserialize_json(data: list) -> TLEDataList:
    import aws_sdk_groundstation.types.tle_data

    out: TLEDataList = []
    for item in data:
        out.append(aws_sdk_groundstation.types.tle_data.deserialize_json(item))
    return out
