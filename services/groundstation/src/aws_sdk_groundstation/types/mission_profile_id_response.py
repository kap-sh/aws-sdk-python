"""Generated from Smithy shape ``com.amazonaws.groundstation#MissionProfileIdResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.uuid


class MissionProfileIdResponse(TypedDict):
    mission_profile_id: NotRequired["aws_sdk_groundstation.types.uuid.Uuid"]
    """<p>UUID of a mission profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MissionProfileIdResponse) -> dict:
    out: dict = {}
    if "mission_profile_id" in value:
        out["missionProfileId"] = value["mission_profile_id"]
    return out


def deserialize_json(data: dict) -> MissionProfileIdResponse:
    out: MissionProfileIdResponse = {}  # type: ignore[typeddict-item]
    if "missionProfileId" in data:
        out["mission_profile_id"] = data["missionProfileId"]
    return out
