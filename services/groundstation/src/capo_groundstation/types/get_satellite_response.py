"""Generated from Smithy shape ``com.amazonaws.groundstation#GetSatelliteResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.ephemeris_meta_data
    import capo_groundstation.types.ground_station_id_list
    import capo_groundstation.types.norad_satellite_id
    import capo_groundstation.types.satellite_arn
    import capo_groundstation.types.uuid


class GetSatelliteResponse(TypedDict, closed=True):
    satellite_id: NotRequired["capo_groundstation.types.uuid.Uuid"]
    """<p>UUID of a satellite.</p>"""
    satellite_arn: NotRequired["capo_groundstation.types.satellite_arn.satelliteArn"]
    """<p>ARN of a satellite.</p>"""
    norad_satellite_id: "capo_groundstation.types.norad_satellite_id.noradSatelliteID"
    """<p>NORAD satellite ID number.</p>"""
    ground_stations: NotRequired[
        "capo_groundstation.types.ground_station_id_list.GroundStationIdList"
    ]
    """<p>A list of ground stations to which the satellite is on-boarded.</p>"""
    current_ephemeris: NotRequired[
        "capo_groundstation.types.ephemeris_meta_data.EphemerisMetaData"
    ]
    """<p>The current ephemeris being used to compute the trajectory of the satellite.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSatelliteResponse) -> dict:
    out: dict = {}
    if "satellite_id" in value:
        out["satelliteId"] = value["satellite_id"]
    if "satellite_arn" in value:
        out["satelliteArn"] = value["satellite_arn"]
    out["noradSatelliteID"] = value.get("norad_satellite_id", 0)
    if "ground_stations" in value:
        import capo_groundstation.types.ground_station_id_list

        out["groundStations"] = (
            capo_groundstation.types.ground_station_id_list.serialize_json(
                value["ground_stations"]
            )
        )
    if "current_ephemeris" in value:
        import capo_groundstation.types.ephemeris_meta_data

        out["currentEphemeris"] = (
            capo_groundstation.types.ephemeris_meta_data.serialize_json(
                value["current_ephemeris"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSatelliteResponse:
    out: GetSatelliteResponse = {}  # type: ignore[typeddict-item]
    if "satelliteId" in data:
        out["satellite_id"] = data["satelliteId"]
    if "satelliteArn" in data:
        out["satellite_arn"] = data["satelliteArn"]
    if "noradSatelliteID" in data:
        out["norad_satellite_id"] = data["noradSatelliteID"]
    else:
        out["norad_satellite_id"] = 0
    if "groundStations" in data:
        import capo_groundstation.types.ground_station_id_list

        out["ground_stations"] = (
            capo_groundstation.types.ground_station_id_list.deserialize_json(
                data["groundStations"]
            )
        )
    if "currentEphemeris" in data:
        import capo_groundstation.types.ephemeris_meta_data

        out["current_ephemeris"] = (
            capo_groundstation.types.ephemeris_meta_data.deserialize_json(
                data["currentEphemeris"]
            )
        )
    return out
