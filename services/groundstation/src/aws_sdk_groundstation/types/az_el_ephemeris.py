"""Generated from Smithy shape ``com.amazonaws.groundstation#AzElEphemeris``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.az_el_segments_data
    import aws_sdk_groundstation.types.ground_station_name


class AzElEphemeris(TypedDict, closed=True):
    ground_station: "aws_sdk_groundstation.types.ground_station_name.GroundStationName"
    """<p>The ground station name for which you're providing azimuth elevation data.</p> <p>This ephemeris is specific to this ground station and can't be used at other locations.</p>"""
    data: "aws_sdk_groundstation.types.az_el_segments_data.AzElSegmentsData"
    """<p>Azimuth elevation segment data.</p> <p>You can provide data inline in the request or through an Amazon S3 object reference.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzElEphemeris) -> dict:
    out: dict = {}
    out["groundStation"] = value["ground_station"]
    import aws_sdk_groundstation.types.az_el_segments_data

    out["data"] = aws_sdk_groundstation.types.az_el_segments_data.serialize_json(
        value["data"]
    )
    return out


def deserialize_json(data: dict) -> AzElEphemeris:
    out: AzElEphemeris = {}  # type: ignore[typeddict-item]
    if "groundStation" in data:
        out["ground_station"] = data["groundStation"]
    else:
        raise DeserializationError("AzElEphemeris.ground_station required")
    if "data" in data:
        import aws_sdk_groundstation.types.az_el_segments_data

        out["data"] = aws_sdk_groundstation.types.az_el_segments_data.deserialize_json(
            data["data"]
        )
    else:
        raise DeserializationError("AzElEphemeris.data required")
    return out
