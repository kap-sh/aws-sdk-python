"""Generated from Smithy shape ``com.amazonaws.groundstation#GetSatelliteRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.uuid


class GetSatelliteRequest(TypedDict):
    satellite_id: "aws_sdk_groundstation.types.uuid.Uuid"
    """<p>UUID of a satellite.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSatelliteRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSatelliteRequest:
    out: GetSatelliteRequest = {}  # type: ignore[typeddict-item]
    return out
