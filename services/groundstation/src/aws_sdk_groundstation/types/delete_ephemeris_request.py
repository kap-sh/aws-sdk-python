"""Generated from Smithy shape ``com.amazonaws.groundstation#DeleteEphemerisRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.uuid


class DeleteEphemerisRequest(TypedDict):
    ephemeris_id: "aws_sdk_groundstation.types.uuid.Uuid"
    """<p>The AWS Ground Station ephemeris ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEphemerisRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEphemerisRequest:
    out: DeleteEphemerisRequest = {}  # type: ignore[typeddict-item]
    return out
