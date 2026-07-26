"""Generated from Smithy shape ``com.amazonaws.groundstation#GroundStationData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.aws_region
    import capo_groundstation.types.ground_station_name


class GroundStationData(TypedDict, closed=True):
    ground_station_id: NotRequired[
        "capo_groundstation.types.ground_station_name.GroundStationName"
    ]
    """<p>ID of a ground station.</p>"""
    ground_station_name: NotRequired[
        "capo_groundstation.types.ground_station_name.GroundStationName"
    ]
    """<p>Name of a ground station.</p>"""
    region: NotRequired["capo_groundstation.types.aws_region.AWSRegion"]
    """<p>Ground station Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroundStationData) -> dict:
    out: dict = {}
    if "ground_station_id" in value:
        out["groundStationId"] = value["ground_station_id"]
    if "ground_station_name" in value:
        out["groundStationName"] = value["ground_station_name"]
    if "region" in value:
        out["region"] = value["region"]
    return out


def deserialize_json(data: dict) -> GroundStationData:
    out: GroundStationData = {}  # type: ignore[typeddict-item]
    if "groundStationId" in data:
        out["ground_station_id"] = data["groundStationId"]
    if "groundStationName" in data:
        out["ground_station_name"] = data["groundStationName"]
    if "region" in data:
        out["region"] = data["region"]
    return out
