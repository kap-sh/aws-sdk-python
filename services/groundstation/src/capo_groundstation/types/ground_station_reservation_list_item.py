"""Generated from Smithy shape ``com.amazonaws.groundstation#GroundStationReservationListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_groundstation.types.antenna_name
    import capo_groundstation.types.ground_station_name
    import capo_groundstation.types.reservation_details
    import capo_groundstation.types.reservation_type


class GroundStationReservationListItem(TypedDict, closed=True):
    reservation_type: "capo_groundstation.types.reservation_type.ReservationType"
    """<p>Type of a ground station reservation.</p>"""
    ground_station_id: "capo_groundstation.types.ground_station_name.GroundStationName"
    """<p>ID of a ground station.</p>"""
    antenna_name: "capo_groundstation.types.antenna_name.AntennaName"
    """<p>Name of an antenna.</p>"""
    start_time: "datetime.datetime"
    """<p>Start time of a ground station reservation in UTC.</p>"""
    end_time: "datetime.datetime"
    """<p>End time of a ground station reservation in UTC.</p>"""
    reservation_details: (
        "capo_groundstation.types.reservation_details.ReservationDetails"
    )
    """<p>Details of a ground station reservation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroundStationReservationListItem) -> dict:
    out: dict = {}
    import capo_groundstation.types.reservation_type

    out["reservationType"] = capo_groundstation.types.reservation_type.serialize_json(
        value["reservation_type"]
    )
    out["groundStationId"] = value["ground_station_id"]
    out["antennaName"] = value["antenna_name"]
    import capo_groundstation.types._prelude.timestamp

    out["startTime"] = capo_groundstation.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    import capo_groundstation.types._prelude.timestamp

    out["endTime"] = capo_groundstation.types._prelude.timestamp.serialize_json(
        value["end_time"]
    )
    import capo_groundstation.types.reservation_details

    out["reservationDetails"] = (
        capo_groundstation.types.reservation_details.serialize_json(
            value["reservation_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> GroundStationReservationListItem:
    out: GroundStationReservationListItem = {}  # type: ignore[typeddict-item]
    if "reservationType" in data:
        import capo_groundstation.types.reservation_type

        out["reservation_type"] = (
            capo_groundstation.types.reservation_type.deserialize_json(
                data["reservationType"]
            )
        )
    else:
        raise DeserializationError(
            "GroundStationReservationListItem.reservation_type required"
        )
    if "groundStationId" in data:
        out["ground_station_id"] = data["groundStationId"]
    else:
        raise DeserializationError(
            "GroundStationReservationListItem.ground_station_id required"
        )
    if "antennaName" in data:
        out["antenna_name"] = data["antennaName"]
    else:
        raise DeserializationError(
            "GroundStationReservationListItem.antenna_name required"
        )
    if "startTime" in data:
        import capo_groundstation.types._prelude.timestamp

        out["start_time"] = (
            capo_groundstation.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError(
            "GroundStationReservationListItem.start_time required"
        )
    if "endTime" in data:
        import capo_groundstation.types._prelude.timestamp

        out["end_time"] = capo_groundstation.types._prelude.timestamp.deserialize_json(
            data["endTime"]
        )
    else:
        raise DeserializationError("GroundStationReservationListItem.end_time required")
    if "reservationDetails" in data:
        import capo_groundstation.types.reservation_details

        out["reservation_details"] = (
            capo_groundstation.types.reservation_details.deserialize_json(
                data["reservationDetails"]
            )
        )
    else:
        raise DeserializationError(
            "GroundStationReservationListItem.reservation_details required"
        )
    return out
