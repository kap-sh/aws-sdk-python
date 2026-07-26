"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisIdResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.uuid


class EphemerisIdResponse(TypedDict, closed=True):
    ephemeris_id: NotRequired["capo_groundstation.types.uuid.Uuid"]
    """<p>The AWS Ground Station ephemeris ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EphemerisIdResponse) -> dict:
    out: dict = {}
    if "ephemeris_id" in value:
        out["ephemerisId"] = value["ephemeris_id"]
    return out


def deserialize_json(data: dict) -> EphemerisIdResponse:
    out: EphemerisIdResponse = {}  # type: ignore[typeddict-item]
    if "ephemerisId" in data:
        out["ephemeris_id"] = data["ephemerisId"]
    return out
