"""Generated from Smithy shape ``com.amazonaws.groundstation#AzElProgramTrackSettings``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_groundstation.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_groundstation.types.uuid

class AzElProgramTrackSettings(TypedDict):
    ephemeris_id: "aws_sdk_groundstation.types.uuid.Uuid"
    """<p>Unique identifier of the azimuth elevation ephemeris.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AzElProgramTrackSettings) -> dict:
    out: dict = {}
    out["ephemerisId"] = value["ephemeris_id"]
    return out


def deserialize_json(data: dict) -> AzElProgramTrackSettings:
    out: AzElProgramTrackSettings = {}  # type: ignore[typeddict-item]
    if "ephemerisId" in data:
        out["ephemeris_id"] = data["ephemerisId"]
    else:
        raise DeserializationError("AzElProgramTrackSettings.ephemeris_id required")
    return out