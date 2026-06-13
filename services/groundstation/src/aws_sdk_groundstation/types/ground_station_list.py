"""Generated from Smithy shape ``com.amazonaws.groundstation#GroundStationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.ground_station_data

GroundStationList: TypeAlias = list[
    "aws_sdk_groundstation.types.ground_station_data.GroundStationData"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroundStationList) -> list:
    import aws_sdk_groundstation.types.ground_station_data

    out: list = []
    for item in value:
        out.append(aws_sdk_groundstation.types.ground_station_data.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroundStationList:
    import aws_sdk_groundstation.types.ground_station_data

    out: GroundStationList = []
    for item in data:
        out.append(
            aws_sdk_groundstation.types.ground_station_data.deserialize_json(item)
        )
    return out
