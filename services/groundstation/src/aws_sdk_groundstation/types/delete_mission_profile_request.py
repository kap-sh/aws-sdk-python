"""Generated from Smithy shape ``com.amazonaws.groundstation#DeleteMissionProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.uuid


class DeleteMissionProfileRequest(TypedDict):
    mission_profile_id: "aws_sdk_groundstation.types.uuid.Uuid"
    """<p>UUID of a mission profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMissionProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMissionProfileRequest:
    out: DeleteMissionProfileRequest = {}  # type: ignore[typeddict-item]
    return out
