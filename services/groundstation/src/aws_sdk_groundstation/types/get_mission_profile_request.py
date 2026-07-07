"""Generated from Smithy shape ``com.amazonaws.groundstation#GetMissionProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.uuid


class GetMissionProfileRequest(TypedDict, closed=True):
    mission_profile_id: "aws_sdk_groundstation.types.uuid.Uuid"
    """<p>UUID of a mission profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMissionProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMissionProfileRequest:
    out: GetMissionProfileRequest = {}  # type: ignore[typeddict-item]
    return out
