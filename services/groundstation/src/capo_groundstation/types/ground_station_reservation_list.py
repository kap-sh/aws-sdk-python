"""Generated from Smithy shape ``com.amazonaws.groundstation#GroundStationReservationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_groundstation.types.ground_station_reservation_list_item

GroundStationReservationList: TypeAlias = list[
    "capo_groundstation.types.ground_station_reservation_list_item.GroundStationReservationListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroundStationReservationList) -> list:
    import capo_groundstation.types.ground_station_reservation_list_item

    out: list = []
    for item in value:
        out.append(
            capo_groundstation.types.ground_station_reservation_list_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GroundStationReservationList:
    import capo_groundstation.types.ground_station_reservation_list_item

    out: GroundStationReservationList = []
    for item in data:
        out.append(
            capo_groundstation.types.ground_station_reservation_list_item.deserialize_json(
                item
            )
        )
    return out
