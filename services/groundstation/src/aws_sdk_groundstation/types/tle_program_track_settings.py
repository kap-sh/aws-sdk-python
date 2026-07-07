"""Generated from Smithy shape ``com.amazonaws.groundstation#TleProgramTrackSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.uuid


class TleProgramTrackSettings(TypedDict, closed=True):
    ephemeris_id: "aws_sdk_groundstation.types.uuid.Uuid"
    """<p>Unique identifier of the TLE ephemeris.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TleProgramTrackSettings) -> dict:
    out: dict = {}
    out["ephemerisId"] = value["ephemeris_id"]
    return out


def deserialize_json(data: dict) -> TleProgramTrackSettings:
    out: TleProgramTrackSettings = {}  # type: ignore[typeddict-item]
    if "ephemerisId" in data:
        out["ephemeris_id"] = data["ephemerisId"]
    else:
        raise DeserializationError("TleProgramTrackSettings.ephemeris_id required")
    return out
