"""Generated from Smithy shape ``com.amazonaws.groundstation#AntennaListItem``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_groundstation.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_groundstation.types.antenna_name
    import aws_sdk_groundstation.types.aws_region
    import aws_sdk_groundstation.types.ground_station_name

class AntennaListItem(TypedDict):
    ground_station_name: "aws_sdk_groundstation.types.ground_station_name.GroundStationName"
    """<p>Name of the ground station the antenna is associated with.</p>"""
    antenna_name: "aws_sdk_groundstation.types.antenna_name.AntennaName"
    """<p>Name of the antenna.</p>"""
    region: "aws_sdk_groundstation.types.aws_region.AWSRegion"
    """<p>Region of the antenna.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AntennaListItem) -> dict:
    out: dict = {}
    out["groundStationName"] = value["ground_station_name"]
    out["antennaName"] = value["antenna_name"]
    out["region"] = value["region"]
    return out


def deserialize_json(data: dict) -> AntennaListItem:
    out: AntennaListItem = {}  # type: ignore[typeddict-item]
    if "groundStationName" in data:
        out["ground_station_name"] = data["groundStationName"]
    else:
        raise DeserializationError("AntennaListItem.ground_station_name required")
    if "antennaName" in data:
        out["antenna_name"] = data["antennaName"]
    else:
        raise DeserializationError("AntennaListItem.antenna_name required")
    if "region" in data:
        out["region"] = data["region"]
    else:
        raise DeserializationError("AntennaListItem.region required")
    return out