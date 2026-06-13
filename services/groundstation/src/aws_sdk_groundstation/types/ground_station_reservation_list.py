"""Generated from Smithy shape ``com.amazonaws.groundstation#GroundStationReservationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.ground_station_reservation_list_item

GroundStationReservationList: TypeAlias = list[
    "aws_sdk_groundstation.types.ground_station_reservation_list_item.GroundStationReservationListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroundStationReservationList) -> list:
    import aws_sdk_groundstation.types.ground_station_reservation_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_groundstation.types.ground_station_reservation_list_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GroundStationReservationList:
    import aws_sdk_groundstation.types.ground_station_reservation_list_item

    out: GroundStationReservationList = []
    for item in data:
        out.append(
            aws_sdk_groundstation.types.ground_station_reservation_list_item.deserialize_json(
                item
            )
        )
    return out
